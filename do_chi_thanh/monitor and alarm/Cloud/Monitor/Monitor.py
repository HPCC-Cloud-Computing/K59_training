import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import ast
import json
import threading
from kombu import Producer, Connection, Consumer, exceptions, Exchange, Queue, uuid
from kombu.utils.compat import nested

BROKER_CLOUD = "localhost"

producer_connection = Connection(BROKER_CLOUD)
consumer_connection = Connection(BROKER_CLOUD)
MODE = "PUSH" # PUSH or PULL

exchange = Exchange("IoT", type="direct")

TIME_COLLECT = 5

list_platform_id = []
list_past_item = []             # Use to store past items
wait_for_alert = []             # Use as a flag to alert
# list_item_global_id = []        # Use to request past item info
list_current_items = []                 # Use to store current items
n_record = 10
upper_threshold = 1.5
lower_threshold = 0.5

# def monitor(list_current_items):
#     print ("Monitoring...")
#
#     global wait_for_alert
#     # print ("list items: ", list_current_items)
#     for item in list_current_items:
#         index = list_current_items.index(item)
#         # print ("index: ", index)
#         item_global_id = item['item_global_id']
#         item_state = item['item_state']
#         print ("item state: ", item_state)
#
#         # Just monitor for number
#         try:
#             item_state = float(item_state)
#         except:
#             continue
#
#         # get past state
#         list_past_item_state = get_past_item_state_from_item_global_id(item_global_id)
#         if (list_past_item_state == None):
#             continue
#         print ("past_item_state: ", list_past_item_state)
#
#         avg_past_item_state = sum(list_past_item_state) * 1.0 / len(list_past_item_state)
#         if (item_state > threshold * avg_past_item_state):
#             if (wait_for_alert[index] == False):
#                 wait_for_alert[index] = True
#             else:
#                 send_alert(item_global_id, item_state, list_past_item_state)
#                 wait_for_alert[index] = False
#                 list_past_item_state.append(item_state)
#                 list_past_item_state = list_past_item_state[1::]
#
#                 # update value for past state list
#                 global list_past_item
#                 for i in range(len(list_past_item)):
#                     if (list_past_item[i]['item_global_id'] == item_global_id):
#                         list_past_item[i]['item_state'] = list_past_item_state
#         else:
#             print ("item id: " + str(item_global_id) + " normal state!")


def monitor(list_current_items):
    print ("Monitoring...")
    # print ("list items: ", list_current_items)

    for item in list_current_items:
        index = list_current_items.index(item)
        # print ("index: ", index)
        item_global_id = item['item_global_id']
        item_state = item['item_state']


        # Just monitor for number
        try:
            item_state = float(item_state)
        except:
            continue

        print ("item state: ", item)

        # get past state
        list_past_item_state = get_past_item_state_from_item_global_id(item_global_id)
        if (list_past_item_state == []):
            continue
        print ("list_past_item_state: ", list_past_item_state)

        avg_past_item_state = sum(list_past_item_state) * 1.0 / len(list_past_item_state)
        if (item_state < upper_threshold * avg_past_item_state or item_state > lower_threshold * avg_past_item_state):
            send_alert(item_global_id, item_state, list_past_item_state)
        else:
            print ("item id: " + str(item_global_id) + " NORMAL!")


def get_past_item_state_from_item_global_id(item_global_id):
    global list_past_item
    # print ("list past items: ", list_past_item)

    list_past_item_state = []
    for past_item in list_past_item:
        if (past_item['item_global_id'] == item_global_id):
            list_past_item_state.append(past_item['item_state']['item_state'])
    return list_past_item_state


def request_past_things_info(list_item_global_id, n_record):
    message = {
        'n_record' : n_record,
        'reply_to' : 'dbreader.respond.monitor',
        'list_item_global_id': list_item_global_id
    }

    producer_connection.ensure_connection()
    with Producer(producer_connection) as producer:
        producer.publish(
            json.dumps(message),
            exchange=exchange.name,
            routing_key='dbreader.request.api_get_item_state',
            retry=True
        )
    print ("Send request to DBreader")


# def receive_past_things_info():
#     queue_get_past_states = Queue(name='dbreader.respond.monitor', exchange=exchange,
#                                   routing_key='dbreader.respond.monitor')
#
#     try:
#         consumer_connection.ensure_connection(max_retries=1)
#         with nested(Consumer(consumer_connection, queues=queue_get_past_states,
#                              callbacks=[handle_dbreader_notification], no_ack=True)):
#             while True:
#                 consumer_connection.drain_events()
#     except (ConnectionRefusedError, exceptions.OperationalError):
#         print('Connection lost')
#     except consumer_connection.connection_errors:
#         print('Connection error')


def extract_things_info(list_things):
    platform_id = list_things['platform_id']
    list_items = []
    list_item_global_id = []
    # Extract message's information
    for thing in list_things['things']:
        for item in thing['items']:
            record = {
                'item_global_id': item['item_global_id'],
                'item_state' : item['item_state']
            }
            list_item_global_id.append(item['item_global_id'])
            list_items.append(record)

    return platform_id, list_items, list_item_global_id


def send_alert(item_global_id, item_state, past_state):
    message = {
        'item_global_id' : item_global_id,
        'item_state'     : item_state,
        'past_state'     : past_state
    }

    request_queue = Queue(name='monitor.request.alert', exchange=exchange, routing_key='monitor.request.alert')
    request_routing_key = 'monitor.request.alert'
    producer_connection.ensure_connection()

    with Producer(producer_connection) as producer:
        producer.publish(
            json.dumps(message),
            exchange=exchange.name,
            routing_key=request_routing_key,
            declare=[request_queue],
            retry=True
        )

    print ("Send alert!")


def handle_notification(body, message):
    # receive list items
    global list_current_items

    print('Receive message from Collector')
    list_things = json.loads(body)
    platform_id, list_current_items, list_item_global_id = extract_things_info(list_things)

    # past items state
    request_past_things_info(list_item_global_id, n_record)



def handle_dbreader_notification(body, message):
    global list_current_items
    global list_past_item

    print ("Receive message from DBReader!")
    list_past_item = json.loads(body)['items']
    print ("list past items: ", list_past_item)
    monitor(list_current_items)


def run():
    queue_get_states = Queue(name='monitor.request.collector', exchange=exchange,
                             routing_key='monitor.request.collector')
    queue_get_past_states = Queue(name='dbreader.respond.monitor', exchange=exchange,
                             routing_key='dbreader.respond.monitor')

    while 1:
        try:
            consumer_connection.ensure_connection(max_retries=1)
            with nested(Consumer(consumer_connection, queues=queue_get_states,
                                callbacks=[handle_notification], no_ack=True),
                        Consumer(consumer_connection, queues=queue_get_past_states,
                                callbacks=[handle_dbreader_notification], no_ack=True)):
                while True:
                    consumer_connection.drain_events()
        except (ConnectionRefusedError, exceptions.OperationalError):
            print('Connection lost')
        except consumer_connection.connection_errors:
            print('Connection error')


run()





# import json
# import threading
# from kombu import Producer, Connection, Consumer, exceptions, Exchange, Queue, uuid
# from kombu.utils.compat import nested
#
# BROKER_CLOUD = "localhost"
#
# producer_connection = Connection(BROKER_CLOUD)
# consumer_connection = Connection(BROKER_CLOUD)
# MODE = "PUSH" # PUSH or PULL
#
# exchange = Exchange("IoT", type="direct")
#
# TIME_COLLECT = 5
#
# list_platform_id = []
#
#
# def monitor():
#     print("Monitor the states of the devices")
#     for platform_id in list_platform_id:
#         collect_by_platform_id(platform_id)
#     threading.Timer(TIME_COLLECT, monitor).start()
#
#
# def collect_by_platform_id(platform_id):
#     print('Collect data from platform_id: ', str(platform_id))
#     message_request = {
#         'reply_to': 'driver.response.monitor.api_get_states',
#         'platform_id': platform_id
#     }
#
#     request_queue = Queue(name='driver.request.api_get_states', exchange=exchange, routing_key='driver.request.api_get_states')
#     request_routing_key = 'driver.request.api_get_states'
#     producer_connection.ensure_connection()
#     with Producer(producer_connection) as producer:
#         producer.publish(
#             json.dumps(message_request),
#             exchange=exchange.name,
#             routing_key=request_routing_key,
#             declare=[request_queue],
#             retry=True
#         )
#
#
# def handle_collect_by_platform_id(body, message):
#     print('Recived state from platform_id: ', json.loads(body)['platform_id'])
#
#     list_things = json.loads(body)
#     print(list_things)
#     # request_queue = Queue(name='dbwriter.request.api_write_db', exchange=exchange, routing_key='dbwriter.request.api_write_db')
#     # request_routing_key = 'dbwriter.request.api_write_db'
#     # producer_connection.ensure_connection()
#     # with Producer(producer_connection) as producer:
#     #     producer.publish(
#     #         json.dumps(list_things),
#     #         exchange=exchange.name,
#     #         routing_key=request_routing_key,
#     #         declare=[request_queue],
#     #         retry=True
#     #     )
#     #
#     # print('Send new state to Dbwriter')
#
#
# def get_list_platforms():
#     print("Get list platforms from Registry")
#     message = {
#         'reply_to': 'registry.response.monitor.api_get_list_platforms',
#         'platform_status': "active"
#     }
#
#     queue = Queue(name='registry.request.api_get_list_platforms', exchange=exchange, routing_key='registry.request.api_get_list_platforms')
#     routing_key = 'registry.request.api_get_list_platforms'
#     producer_connection.ensure_connection()
#     with Producer(producer_connection) as producer:
#         producer.publish(
#             json.dumps(message),
#             exchange=exchange.name,
#             routing_key=routing_key,
#             declare=[queue],
#             retry=True
#         )
#
#
# def handle_get_list(body, message):
#     global list_platform_id
#     list_platforms = json.loads(body)['list_platforms']
#     temp = []
#     for platform in list_platforms:
#         temp.append(platform['platform_id'])
#
#     list_platform_id = temp
#
#     print('Updated list of platform_id: ', str(list_platform_id))
#
#
# def handle_notification(body, message):
#     print('Have Notification')
#     if json.loads(body)['notification'] == 'Have Platform_id change':
#         get_list_platforms()
#
#
# # def run():
# #     queue_notification = Queue(name='monitor.request.notification', exchange=exchange,
# #                                routing_key='monitor.request.notification')
# #     queue_list_platforms = Queue(name='registry.response.monitor.api_get_list_platforms', exchange=exchange,
# #                                  routing_key='registry.response.monitor.api_get_list_platforms')
# #     queue_get_states = Queue(name='driver.response.monitor.api_get_states', exchange=exchange,
# #                              routing_key='driver.response.monitor.api_get_states')
# #
# #     # if MODE == 'PULL':
# #     #     print("Monitor use Mode: PULL Data")
# #     #     get_list_platforms()
# #     #     monitor()
# #
# #     while 1:
# #         try:
# #             consumer_connection.ensure_connection(max_retries=1)
# #             with nested(Consumer(consumer_connection, queues=queue_notification, callbacks=[handle_notification],
# #                                  no_ack=True),
# #                         Consumer(consumer_connection, queues=queue_list_platforms, callbacks=[handle_get_list],
# #                                  no_ack=True),
# #                         Consumer(consumer_connection, queues=queue_get_states,
# #                                  callbacks=[handle_collect_by_platform_id], no_ack=True)):
# #                 while True:
# #                     consumer_connection.drain_events()
# #         except (ConnectionRefusedError, exceptions.OperationalError):
# #             print('Connection lost')
# #         except consumer_connection.connection_errors:
# #             print('Connection error')
#
#
# def run():
#     queue_get_states = Queue(name='monitor.request.collector', exchange=exchange,
#                              routing_key='monitor.request.collector')
#
#     request_past_things_info(n_record)
#     get_past_info()
#
#
#     while 1:
#         try:
#             consumer_connection.ensure_connection(max_retries=1)
#             with nested(Consumer(consumer_connection, queues=queue_get_states,
#                         callbacks=[handle_notification], no_ack=True)):
#                 while True:
#                     consumer_connection.drain_events()
#         except (ConnectionRefusedError, exceptions.OperationalError):
#             print('Connection lost')
#         except consumer_connection.connection_errors:
#             print('Connection error')
#
#
#
# run()
#
#
#
