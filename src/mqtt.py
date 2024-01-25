import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, host, port, username, password, debug = False):
        self.mqtt_client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_subscribe = self.on_subscribe
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_publish = self.on_publish
        self.mqtt_client.username_pw_set(username, password)
        self.host = host
        self.port = port
        self.callback_connect_func = None
        self.callback_message_func = None
        self.debug = debug

    def set_debug(self, state):
        self.debug = state

    def on_connect(self, client, userdata, flags, rc, properties=None):
        if self.debug: print(f"[MQTT]: on connect CONNACK received with code {rc}.")
        if self.callback_connect_func is not None:
            self.callback_connect_func(self)

    def on_publish(self, client, userdata, mid, properties=None):
        if self.debug: print(f"[MQTT]: on_publish mid[{mid}]")

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        if self.debug: print(f"[MQTT]: on_subscribe mid[{mid}], granted_qos[{granted_qos}]")

    def on_message(self, client, userdata, msg):
        if self.debug: print(f"[MQTT]: on_message topic[{msg.topic}], qos[{msg.qos}], payload[{msg.payload}]")
        if self.callback_message_func is not None:
            self.callback_message_func(self, msg.topic, msg.payload.decode())

    def subscribe(self, topic):
        self.mqtt_client.subscribe(topic, qos=1)

    def publish(self, topic, payload):
        self.mqtt_client.publish(topic, payload=payload, retain=True, qos=1)

    def register_on_connect_listener(self, func):
        self.callback_connect_func = func

    def register_on_message_listener(self, func):
        self.callback_message_func = func

    def unblocking(self):
        self.mqtt_client.connect(self.host, self.port)
        self.mqtt_client.loop_start()

    def blocking(self):
        self.mqtt_client.connect(self.host, self.port)
        self.mqtt_client.loop_forever()


if __name__ == "__main__":
    import credentials
    mqtt = MqttClient(credentials.host, credentials.port, credentials.username, credentials.password)
    mqtt.set_debug(True)
    def on_connect(mqtt):
        mqtt.subscribe("#")
    mqtt.register_on_connect_listener(on_connect)
    def on_message(mqtt, topic, payload):
        print(topic, payload)
    mqtt.register_on_message_listener(on_message)
    mqtt.blocking()
