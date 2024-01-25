#!/usr/bin/env python

import asyncio
import aiomqtt

import topics
import credentials
import typer

async def write_to_topic(write_topic, payload, read_topic = None, timeout = 5):
    reconnect_interval_s = 5
    while True:
        try:
            async with aiomqtt.Client(hostname=credentials.host, port=credentials.port, username=credentials.username, password=credentials.password) as client:
                if read_topic is not None:
                    await client.subscribe(read_topic)
                    await client.publish(write_topic, payload=payload)
                    async with asyncio.timeout(timeout):
                        async for message in client.messages:
                            return message.payload.decode()
                else:
                    await client.publish(topic=write_topic, payload=payload)
        except aiomqtt.MqttError as error:
            print(f'Error "{error}". Reconnecting in {reconnect_interval_s} seconds.')
            await asyncio.sleep(reconnect_interval_s)
        except TimeoutError:
            print(f"Timeout for message[{read_topic}].")
            return None

app = typer.Typer()

@app.command()
def list_rooms():
    for room in topics.get_rooms():
        print(f"[{room.name.name}] {room.name.value}")

@app.command()
def list_devices():
    for device in topics.get_devices():
        print(f"[{device.device.name:5s}] {device.device.value}")

@app.command()
def describe_room(room_name: str):
    room = topics.get_room_by_name(room_name)
    if room is not None:
        print(f"[{room.name.name}] {room.name.value}")
        print("  Lights:")
        for light in room.lights:
            print(f"    {light}")
        print("  Rollers:")
        for roller in room.rollers:
            print(f"    {roller}")
        print("  Sensors:")
        for sensor in room.sensors:
            print(f"    {sensor}")
    else:
        print("No such room")

@app.command()
def turn_light(room_name: str, group: int, index: int, state: int):
    room = topics.get_room_by_name(room_name)
    if room is not None:
        light = topics.get_light_by_group_and_index(room.lights, group, index)
        if light is not None:
            topic = light.get_room_topic(room)
            payload = asyncio.run(write_to_topic(topics.Direction.write(topic), state, topics.Direction.read(topic)))
            if payload is not None:
                print(f"Received: {topics.Direction.read(topic)} -> {payload}")
        else:
            print(f"No such light[{group}, {index}] in room[{room_name}]]")
    else:
        print(f"No such room[{room_name}]")

@app.command()
def get_version(device_name: str):
    device = topics.get_device_by_name(device_name)
    if device is not None:
        topic = device.version.get_mac_topic()
        payload = asyncio.run(write_to_topic(topics.Direction.write(topic), "request", topics.Direction.read(topic)))
        if payload is not None:
            print(f"Received: {topics.Direction.read(topic)} -> {payload}")
    else:
        print(f"No such device[{device_name}]")

@app.command()
def get_version_all():
    for device in topics.get_devices():
        print(f"Device[{device.device.name}]")
        topic = device.version.get_mac_topic()
        payload = asyncio.run(write_to_topic(topics.Direction.write(topic), "request", topics.Direction.read(topic), timeout = 2))
        if payload is not None:
            print(f"Received: {topics.Direction.read(topic)} -> {payload}")
            
@app.callback()
def main():
    pass

if __name__ == "__main__":
    app()
