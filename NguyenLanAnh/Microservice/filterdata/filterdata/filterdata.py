import os, os.path
#!/usr/bin/env python
import pika

url = "/config/config.cfg"
openFile = open(url)
lines = openFile.readlines()
lineUrl1 = lines[1]
lineUrl2 = lines[3]
strLineUrl1 = str(lineUrl1)
strLineUrl2 = str(lineUrl2)
url1 = strLineUrl1[4:14]
url2 = strLineUrl2[4:14]
#url1 = "'" + url1 + "'"
#url2 = "'" + url2 + "'"
print url1
print url2

connection1 = pika.BlockingConnection(pika.connection.ConnectionParameters(host= url1))
channel1 = connection1.channel()
connection2 = pika.BlockingConnection(pika.connection.ConnectionParameters(host= url2))
channel2 = connection2.channel()
def callback(ch, method, properties, body):
    print("Received %r" % body)
    print "filtering continuously ...",body
    newstr = ""
    for i in body:
        if i == "1":
         newstr += "1"
        else:
         continue
    print "du lieu sau khi loc: ",newstr
    print "-----------"
    channel2.basic_publish(exchange='test1.exchange',
                           routing_key='111',
                           body= newstr)
    
    # loc du lieu tu body, duoi, not done
    # tiep
channel1.basic_consume(callback,
                      queue='test',
                      no_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel1.start_consuming()


