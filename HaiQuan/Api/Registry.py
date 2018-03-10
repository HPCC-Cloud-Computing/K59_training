import paho.mqtt.client as mqtt
import json
import uuid
import MySQLdb
import ast
import time
import threading
from mysql.connector.pooling import MySQLConnectionPool

dbconfig = {
  "database": "Registry_DB",
  "user":     "root",
  "host":     "192.168.60.248",
  "passwd":   "root",
  "autocommit": "True"
}

cnxpool = MySQLConnectionPool(pool_name = "mypool", pool_size = 32, **dbconfig)

# broker_address = "127.0.0.1"
broker_address = "iot.eclipse.org"
clientMQTT = mqtt.Client("Registry")  # create new instance
clientMQTT.connect(broker_address)  # connect to broker


def update_config_changes_by_platform_id(platform_id):
    cnx_1 = get_con("update_config_changes_by_platform_id cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""SELECT last_response FROM Platform WHERE platform_id = %s""", (platform_id,))
    last_response = cursor_1.fetchone()
    if time.time() - last_response[0] < 600:
        # ĐK kiểm tra xem còn available không?
        message = {
            'caller': 'registry'
        }

        def handle_configuration_changes(client, userdata, msg):
            cnx_2 = get_con("handle_configuration_changes cnx_2")
            cursor_2 = cnx_2.cursor()
            response = ast.literal_eval(msg.payload.decode('utf-8'))
            cursor_2.execute("""UPDATE Platform SET last_response= %s WHERE platform_id=%s""", (time.time(), platform_id))
            cnx_2.commit()
            if response[0] == True:
                print('Platform have Id: {} no changes'.format(platform_id))
                cursor_2.close()
                cnx_2.close()
                return
            else:
                print('Platform have Id: {} changed the configuration file'.format(platform_id))
                now_info = response[1]
                delete_old_thing_and_item(str(platform_id))
                for thing in now_info:

                    cursor_2.execute("""INSERT INTO Thing VALUES (%s,%s,%s,%s,%s,%s)""", (thing['thing_global_id'], platform_id, thing['thing_name'], thing['thing_type'], thing['thing_local_id'], thing['location']))
                    print('Updated Things')
                    for item in thing['items']:
                        print(item)
                        print("{}".format(item['item_global_id']))
                        cursor_2.execute("""INSERT INTO Item VALUES (%s,%s,%s,%s,%s,%s)""", (item['item_global_id'], thing['thing_global_id'], item['item_name'], item['item_type'], item['item_local_id'], item['can_set_state']))
                        print('Updated Items')

            cnx_2.commit()
            cursor_2.close()
            cnx_2.close()

        clientMQTT.subscribe('{}/response/registry/api_check_configuration_changes'.format(platform_id))
        clientMQTT.message_callback_add('{}/response/registry/api_check_configuration_changes'.format(platform_id), handle_configuration_changes)
        clientMQTT.publish('{}/request/api_check_configuration_changes'.format(platform_id), json.dumps(message))

    else:
        delete_old_thing_and_item(str(platform_id))
        cursor_1.execute("""DELETE FROM Platform WHERE platform_id = %s""", (platform_id,))
        print('Delete Platform have Id: ', str(platform_id))
        clientMQTT.unsubscribe('{}/response/registry/api_check_configuration_changes'.format(platform_id))
        send_notification_to_collector()

    cnx_1.commit()
    cursor_1.close()
    cnx_1.close()


def delete_old_thing_and_item(platform_id):

    print ('Delete Old Thing and Item')
    cnx_1 = get_con("delete_old_thing_and_item cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""SELECT thing_global_id FROM Thing WHERE platform_id = %s""", (str(platform_id),))
    list_thing_global_id = cursor_1.fetchall()
    for thing_global_id in list_thing_global_id:
        cursor_1.execute("""DELETE FROM Item WHERE thing_global_id = %s""", (str(thing_global_id),))

    cursor_1.execute("""DELETE FROM Thing WHERE platform_id = %s""", (str(platform_id),))
    cnx_1.commit()
    cursor_1.close()
    cnx_1.close()


def update_all_config_changes():
    print('Run Update All Configuration Changes')
    cnx_1 = get_con("update_all_config_changes cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""SELECT platform_id FROM Platform""")
    rows = cursor_1.fetchall()
    cursor_1.close()
    cnx_1.close()
    print (rows)
    for row in rows:
        update_config_changes_by_platform_id(row[0])

    threading.Timer(2, update_all_config_changes).start()


def send_notification_to_collector():
    print('Send notification to Collector')
    message = {
        'notification': 'Have Platform_id change'
    }
    clientMQTT.publish('collector/request/notification', json.dumps(message))


def api_get_list_platforms(client, userdata, msg):
    print('Get list platforms')
    caller = json.loads(msg.payload.decode('utf-8'))['caller']
    cnx_1 = get_con("api_get_list_platforms cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""SELECT platform_id FROM Platform""")
    rows = cursor_1.fetchall()
    list_platforms = []
    for row in rows:
        list_platforms.append(row[0])
    print(list_platforms)
    cursor_1.close()
    cnx_1.close()
    clientMQTT.publish('registry/response/{}/api_get_list_platforms'.format(caller), str(list_platforms))


def api_add_platform(client, userdata, msg):

    platform_id = str(uuid.uuid4())
    host = json.loads(msg.payload.decode('utf-8'))['host']
    port = json.loads(msg.payload.decode('utf-8'))['port']
    platform_name = json.loads(msg.payload.decode('utf-8'))['platform']

    print ('Add {} have address {}:{} to system '.format(platform_name, host, port))
    print ('Generate id for this platform : ', platform_id)

    message = {
        'platform_id': platform_id
    }
    clientMQTT.publish('registry/response/{}/{}'.format(host,port), json.dumps(message))
    cnx_1 = get_con("api_add_platform cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""USE Registry_DB""")
    cursor_1.execute("""INSERT INTO Platform VALUES (%s,%s,%s,%s,%s)""", (platform_id, platform_name, host, port, time.time()))
    cnx_1.commit()
    cursor_1.close()
    send_notification_to_collector()


def get_con(ten_ham):

    while True:
        print('Ham goi: ', ten_ham)
        try:
            print("Get connection DB")
            cnx_1 = cnxpool.get_connection()
            cursor_1 = cnx_1.cursor()
            return cnx_1

        except:
            pass


def api_get_things(client, userdata, msg):
    print('Get All Things')
    caller = json.loads(msg.payload.decode('utf-8'))['caller']
    cnx_1 = get_con("api_get_things cnx_1")
    cursor_1 = cnx_1.cursor()
    cursor_1.execute("""SELECT Thing.platform_id, Thing.thing_global_id, Thing.thing_name,
                            Thing.thing_type, Thing.location, Thing.thing_local_id
                      FROM  Thing; """)
    thing_rows = cursor_1.fetchall()

    cursor_1.execute("""SELECT Item.thing_global_id, Item.item_global_id, 
                             Item.item_name, Item.item_type, Item.can_set_state, Item.item_local_id
                      FROM Item ;""")
    item_rows = cursor_1.fetchall()
    cursor_1.close()
    cnx_1.close()
    things = []
    for thing in thing_rows:
        temp_thing = {
            'platform_id': thing[0],
            'thing_global_id': thing[1],
            'thing_name': thing[2],
            'thing_type': thing[3],
            'thing_location': thing[4],
            'thing_local_id': thing[5],
            'items': []
        }

        for item in item_rows:
            if item[0] == thing[1]:
                temp_item = {
                    'item_global_id': item[1],
                    'item_name': item[2],
                    'item_type': item[3],
                    'can_set_state': item[4],
                    'item_local_id': item[5]
                }
                temp_thing['items'].append(temp_item)
        things.append(temp_thing)

    clientMQTT.publish('registry/response/{}/api_get_things'.format(caller), str(things))


update_all_config_changes()

clientMQTT.subscribe('registry/request/api_add_platform')
clientMQTT.message_callback_add('registry/request/api_add_platform',api_add_platform)

clientMQTT.subscribe('registry/request/api_get_list_platforms')
clientMQTT.message_callback_add('registry/request/api_get_list_platforms', api_get_list_platforms)

clientMQTT.subscribe('registry/request/api_get_things')
clientMQTT.message_callback_add('registry/request/api_get_things', api_get_things)

clientMQTT.loop_forever()