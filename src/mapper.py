#!/usr/bin/env python3

import topics
import mqtt

topics_map = topics.get_topics()

def on_connect(mqtt):
    mqtt.subscribe("#")

def on_msg_received(mqtt, topic, payload):
    new_topic = topics_map.get(topic)
    if new_topic is not None:
        mqtt.publish(new_topic, payload)
    else:
        if not topic.startswith("k"):
            print(f"topic not in topics_map {topic}")

if __name__ == "__main__":
    mqtt = mqtt.MqttClient()
    mqtt.register_on_connect_listener(on_connect)
    mqtt.register_on_message_listener(on_msg_received)
    mqtt.blocking()
