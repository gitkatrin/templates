import time
import json
import paho.mqtt.client as mqtt

# MQTT Broker Adresse and Port
broker_address = "broker.hshl.com"
broker_port = 1883
mqtt_topic = "inyo/mock"

# create MQTT Client
client = mqtt.Client()

# connect to Broker
client.connect(broker_address, broker_port)

# count message
message_count = 1

try:
    while True:
        # create message
        message = {
            "count": message_count,
            "message": "Pedestrians detected!"
        }
        
        # format message to json
        json_message = json.dumps(message)
        
        # Nachricht veröffentlichen
        client.publish(mqtt_topic, json_message)
        print("Published: {}".format(json_message))
        
        # count message
        message_count += 1
        
        # wait 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    #print("Script ended.")
    client.disconnect()