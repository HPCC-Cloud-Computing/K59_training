import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import ast
import json
import threading

clientDB = InfluxDBClient('localhost', 8086, 'root', 'root', 'Collector_DB')
clientDB.create_database('Collector_DB')

broker_address = "iot.eclipse.org"
clientMQTT = mqtt.Client("Collector")  # create new instance
clientMQTT.connect(broker_address)  # connect to broker

time_collect = 5
list_platforms = []


def collect():
    print("Collect the states of the devices")
    for platform_id in list_platforms:
        collect_by_platform_id(platform_id)
    threading.Timer(time_collect, collect).start()


def collect_by_platform_id(platform_id):
    print('Collect data from platform_id: ', str(platform_id))
    message = {
        'caller': 'collector'
    }

    def handle_collect_by_platform_id(client, userdata, msg):
        print('Recived state from platform_id: ', platform_id)
        print(msg.payload.decode('utf-8'))
        print(ast.literal_eval(msg.payload.decode('utf-8')))
        list_things = ast.literal_eval(msg.payload.decode('utf-8'))
        data_write_db = []
        for thing in list_things:
            for item in thing['items']:
                record = {
                    'measurement': 'collector',
                    'tags': {
                        'platform_id': platform_id,
                        'thing_type': thing['thing_type'],
                        'thing_name': thing['thing_name'],
                        'thing_global_id': thing['thing_global_id'],
                        'thing_local_id': thing['thing_local_id'],
                        'location': thing['location'],
                        'item_type': item['item_type'],
                        'item_name': item['item_name'],
                        'item_global_id': item['item_global_id'],
                        'item_local_id': item['item_local_id'],
                        'can_set_state': item['can_set_state'],
                    },
                    'fields':{
                        'item_state': item['item_state'],
                    }
                }

                data_write_db.append(record)

        clientDB.write_points(data_write_db)
        print('Updated Database')

    clientMQTT.subscribe('{}/response/collector/api_get_states'.format(platform_id))
    clientMQTT.message_callback_add('{}/response/collector/api_get_states'.format(platform_id), handle_collect_by_platform_id)
    clientMQTT.publish('{}/request/api_get_states'.format(platform_id), json.dumps(message))


def get_thing_by_id(thing_global_id):
    print('Get thing by thing_global_id')
    temp = "SELECT *, item_global_id FROM collector WHERE thing_global_id =\'"+thing_global_id+"\' GROUP BY item_global_id ORDER BY time DESC LIMIT 1"
    query_result = clientDB.query(temp)

    thing = {
        'thing_global_id': thing_global_id,
        'items': []
    }

    for item in query_result:
        temp = {
            'item_global_id': item[0]['item_global_id'],
            'item_type': item[0]['item_type'],
            'item_state': item[0]['item_state']
        }
        thing['items'].append(temp)

    return thing


def get_things(list_thing_global_id):
    things = []
    for thing_global_id in list_thing_global_id:
        things.append(get_thing_by_id(thing_global_id))
    return things


def get_list_platforms():
    print("Get list platforms from Registry")
    message = {
        'caller': 'collector'
    }

    def hand_get_list(client, userdata, msg):
        global list_platforms
        list_platforms = ast.literal_eval(msg.payload.decode('utf-8'))
        print('Updated list of platform_id: ', str(list_platforms))

    clientMQTT.publish('registry/request/api_get_list_platforms', json.dumps(message))
    clientMQTT.subscribe('registry/response/collector/api_get_list_platforms')
    clientMQTT.message_callback_add('registry/response/collector/api_get_list_platforms', hand_get_list)


def handle_notification(client, userdata, msg):
    print('Have Notification')
    if json.loads(msg.payload.decode('utf-8'))['notification'] == 'Have Platform_id change':
        get_list_platforms()


def api_get_things(client, userdata, msg):
    print('API get thing state by id')
    caller = json.loads(msg.payload.decode('utf-8'))['caller']
    list_thing_global_id = json.loads(msg.payload.decode('utf-8'))['list_thing_global_id']
    things = []
    for thing_global_id in list_thing_global_id:
        things.append(get_thing_by_id(thing_global_id))
    clientMQTT.publish('collector/response/{}/api_get_things'.format(caller), str(things))


def api_get_thing_by_id(client,userdata, msg):
    print('Get thing state by id')
    caller = json.loads(msg.payload.decode('utf-8'))['caller']
    thing_global_id = json.loads(msg.payload.decode('utf-8'))['thing_global_id']
    clientMQTT.publish('collector/response/{}/api_get_thing_by_id'.format(caller), json.dumps(get_thing_by_id(thing_global_id)))

clientMQTT.subscribe('collector/request/notification')
clientMQTT.message_callback_add('collector/request/notification', handle_notification)

clientMQTT.subscribe('collector/request/api_get_things')
clientMQTT.message_callback_add('collector/request/api_get_things', api_get_things)

clientMQTT.subscribe('collector/request/api_get_thing_by_id')
clientMQTT.message_callback_add('collector/request/api_get_thing_by_id', api_get_thing_by_id)

get_list_platforms()
collect()
clientMQTT.loop_forever()