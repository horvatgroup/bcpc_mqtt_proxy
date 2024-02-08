#!/usr/bin/env python

import json
import topics

def export_to_json(data, path):
    with open(path, 'w') as fp:
        json.dump(data, fp, indent=2, sort_keys=True)
        
def generate_group(item_type = "Group", label = None, group_names = None, tags = None, category = None, base_item_type = None, function_name = None, function_params = None):
    data = {}
    data["class"] = "org.openhab.core.items.ManagedItemProvider$PersistedItem"
    data["value"] = {}
    if group_names is not None:
        data["value"]["groupNames"] = group_names
    if item_type is not None:
        data["value"]["itemType"] = item_type
    if tags is not None:
        data["value"]["tags"] = tags
    if label is not None:
        data["value"]["label"] = label
    if category is not None:
        data["value"]["category"] = category
    if base_item_type is not None:
        data["value"]["baseItemType"] = base_item_type
    if function_name is not None:
        data["value"]["functionName"] = function_name
    #else:
    #    data["value"]["functionName"] = None
    if function_params is not None:
        data["value"]["functionParams"] = function_params
    #data["value"]["groupType"] = "None"
    return data

def generate_group_locations():
    data = {}
    data["bcpc"] = generate_group(label="BCPC")
    data["dvoriste"] = generate_group(label="Dvorište", group_names=["bcpc"], tags = ["Location"])
    data["pastoralni"] = generate_group(label="Pastoralni centar", group_names=["bcpc"], tags = ["Location"])
    data["skola"] = generate_group(label="Škola", group_names=["bcpc"], tags = ["Location"])
    data["k0"] = generate_group(label="K0 Prizemlje", group_names=["skola"], tags = ["Location"], category="groundfloor")
    data["k1"] = generate_group(label="K1 Prvi kat", group_names=["skola"], tags = ["Location"], category="firstfloor")
    data["k2"] = generate_group(label="K2 Drugi kat", group_names=["skola"], tags = ["Location"], category="attic")
    for room in topics.RoomName:
        label = f"{room.id[:2].upper()}-{room.id[2:4]} {room.label}"
        data[room.id] = generate_group(label=label, group_names=[room.id[:2]], tags = ["Location"], category=room.category)
    return data

def generate_other_groups():
    data = {}
    data["glights"] = generate_group(label="Svjetla", group_names=["skola"], tags=["Lightbulb"], category="lightbulb", base_item_type="Switch", function_name="OR", function_params=["ON", "OFF"])
    data["gpodno_k0"] = generate_group(label="K0 Podno grijanje", group_names=["k0"], tags=["RadiatorControl"], category="heating", base_item_type="Switch", function_name="OR", function_params=["ON", "OFF"])
    data["gpodno_k1"] = generate_group(label="K1 Podno grijanje", group_names=["k1"], tags=["RadiatorControl"], category="heating", base_item_type="Switch", function_name="OR", function_params=["ON", "OFF"])
    data["gpodno_k2"] = generate_group(label="K2 Podno grijanje", group_names=["k2"], tags=["RadiatorControl"], category="heating", base_item_type="Switch", function_name="OR", function_params=["ON", "OFF"])
    data["grollers"] = generate_group(label="Sva sjenila", group_names=["skola"], tags=["Blinds"], category="rollershutter", base_item_type="Rollershutter", function_name="OR", function_params=["ON", "OFF"])
    data["grollersE"] = generate_group(label="Sjenila istok", group_names=["skola"], tags=["Blinds"], category="rollershutter", base_item_type="Rollershutter", function_name="OR", function_params=["ON", "OFF"])
    data["grollersS"] = generate_group(label="Sjenila jug", group_names=["skola"], tags=["Blinds"], category="rollershutter", base_item_type="Rollershutter", function_name="OR", function_params=["ON", "OFF"])
    data["grollersW"] = generate_group(label="Sjenila zapad", group_names=["skola"], tags=["Blinds"], category="rollershutter", base_item_type="Rollershutter", function_name="OR", function_params=["ON", "OFF"])
    data["gheartbeats"] = generate_group(label="Heartbeat", group_names=["skola"], tags=["Duration", "Point"], category="qualityofservice", base_item_type="Number", function_name="OR", function_params=["ON", "OFF"])
    data["galarms"] = generate_group(label="CO2 Alarm", group_names=["skola"], tags=["Alarm", "CO2"], category="alarm", base_item_type="Switch", function_name="OR", function_params=["ON", "OFF"])
    return data

def generate_groups():
    data = {}
    export_to_json(data, "groups.json")

def generate_item_lights():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for e,light in enumerate(room.lights):
            id = f"{room.name.id}_light_{e + 1}"
            group_names = [room.name.id, "glights"]
            item_type = "Switch"
            tags = ["Lightbulb"]
            if len(room.lights) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Svjetlo {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Svjetlo"
            category = "lightbulb"
            data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_item_heating_valves():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for e,heating_valve in enumerate(room.heating_valves):
            floor = room.name.id[:2]
            id = f"{room.name.id}_heating_valve_{e + 1}"
            group_names = [room.name.id, f"gpodno_{floor}"]
            item_type = "Switch"
            tags = ["RadiatorControl"]
            alias = ""
            if heating_valve.alias is not None:
                alias = f" ({heating_valve.alias})"
            if len(room.heating_valves) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Podno {e + 1}{alias}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Podno{alias}"
            category = "heating"
            data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_item_rollers():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for e,roller in enumerate(room.rollers):
            id = f"{room.name.id}_roller_{e + 1}"
            group_names = [room.name.id, "grollers", f"grollers{roller.group_direction}"]
            item_type = "Rollershutter"
            tags = ["Blinds"]
            if len(room.rollers) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Sjenila {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Sjenila"
            category = "rollershutter"
            data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_item_sensors():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for sensor in room.sensors:
            e = get_sensor_index(room.sensors, sensor)
            id = f"{room.name.id}_sensor_{sensor.stype}_{e + 1}"
            group_names = [room.name.id]
            match sensor.stype:
                case "light":
                    item_type = "Number"
                    tags = ["Point", "Light"]
                    category = "sun"
                case "co2":
                    item_type = "Number"
                    tags = ["Point", "CO2"]
                    category = "CO2"
                case "temperature":
                    item_type = "Number"
                    tags = ["Point", "Temperature"]
                    category = "temperature"
                case "pressure":
                    item_type = "Number"
                    tags = ["Point", "Pressure"]
                    category = "pressure"
                case "humidity":
                    item_type = "Number"
                    tags = ["Point", "Humidity"]
                    category = "humidity"
                case "gas":
                    item_type = "Number"
                    tags = ["Point", "Gas"]
                    category = "Atmosphere"
                case "altitude":
                    item_type = "Number"
                    tags = ["Point", "Altitude"]
                    category = "altitude"
                case "radar":
                    item_type = "Switch"
                    tags = ["MotionDetector"]
                    category = "presence"
            if count_sensors(room.sensors, sensor.stype) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} {sensor.alias} {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} {sensor.alias}"
            data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_item_heartbeats():
    data = {}
    heartbeats = topics.get_heartbeats()
    for heartbeat in heartbeats:
        id = f"{heartbeat.device.name}_heartbeat"
        group_names = ["gheartbeats"]
        label = f"{heartbeat.device.name[:2].upper()}-{heartbeat.device.name[2:].upper()} Heartbeat"
        item_type = "Number"
        tags = ["Point", "Duration"]
        category = "qualityofservice"
        data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_item_alarms():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for e,alarm in enumerate(room.alarms):
            id = f"{room.name.id}_alarm_{e + 1}"
            group_names = [room.name.id, "galarms"]
            item_type = "Switch"
            tags = ["Alarm"]
            if len(room.lights) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} CO2 Alarm {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} CO2 Alarm"
            category = "alarm"
            data[id] = generate_group(item_type=item_type, label=label, group_names=group_names, tags=tags, category=category)
    return data

def generate_items():
    data = {}
    data.update(generate_item_lights())
    data.update(generate_item_heating_valves())
    data.update(generate_item_rollers())
    data.update(generate_item_sensors())
    data.update(generate_item_heartbeats())
    data.update(generate_item_alarms())
    data.update(generate_group_locations())
    data.update(generate_other_groups())
    export_to_json(data, "items.json")

def generate_channel(id, channel_type, label, command_topic, state_topic, values, unit, transformation_pattern):
    lines = []
    lines.append(f'  - id: {id}')
    lines.append(f'    channelTypeUID: mqtt:{channel_type}')
    lines.append(f'    label: {label}')
    lines.append(f'    description: null')
    lines.append(f'    configuration:')
    if command_topic is not None:
        lines.append(f'      commandTopic: {command_topic}') #in
    lines.append(f'      stateTopic: {state_topic}') #out
    for k,v in values.items():
        lines.append(f'      {k}: {v}')
    if unit is not None:
        lines.append(f'      unit: {unit}')
    if transformation_pattern is not None:
        lines.append(f'      transformationPattern: "{transformation_pattern}"')
    return lines

def generate_light_channels():
    lines = []
    rooms = topics.get_rooms()
    for room in rooms:
        for e,light in enumerate(room.lights):
            id = f"{room.name.id}_light_{e + 1}"
            if len(room.lights) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Svjetlo {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Svjetlo"
            command_topic = topics.Direction.write(light.get_mac_topic())
            state_topic = topics.Direction.read(light.get_mac_topic())
            lines += generate_channel(id=id, channel_type="switch", label=label, command_topic=command_topic, state_topic=state_topic, values={"off": '"0"', "on": '"1"'}, unit=None, transformation_pattern=None)
    return lines

def generate_heating_valves_channels():
    lines = []
    rooms = topics.get_rooms()
    for room in rooms:
        for e,heating_valve in enumerate(room.heating_valves):
            id = f"{room.name.id}_heating_valve_{e + 1}"
            alias = ""
            if heating_valve.alias is not None:
                alias = f" ({heating_valve.alias})"
            if len(room.heating_valves) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Podno {e + 1}{alias}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Podno{alias}"
            command_topic = topics.Direction.write(heating_valve.get_mac_topic())
            state_topic = topics.Direction.read(heating_valve.get_mac_topic())
            lines += generate_channel(id=id, channel_type="switch", label=label, command_topic=command_topic, state_topic=state_topic, values={"off": '"0"', "on": '"1"'}, unit=None, transformation_pattern=None)
    return lines

def generate_rollers_channels():
    lines = []
    rooms = topics.get_rooms()
    for room in rooms:
        for e,light in enumerate(room.rollers):
            id = f"{room.name.id}_roller_{e + 1}"
            if len(room.rollers) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Sjenila {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} Sjenila"
            command_topic = topics.Direction.write(light.get_mac_topic())
            state_topic = topics.Direction.read(light.get_mac_topic())
            lines += generate_channel(id=id, channel_type="rollershutter", label=label, command_topic=command_topic, state_topic=state_topic, values={"off": '"0"', "on": '"100"', "stop": "STOP"}, unit=None, transformation_pattern=None)
    return lines

def count_sensors(sensors, stype):
    count = 0
    for s in sensors:
        if s.stype == stype:
            count += 1
    return count

def get_sensor_index(sensors, sensor):
    stype = sensor.stype
    index = 0
    for s in sensors:
        if s == sensor:
            return index
        if s.stype == stype:
            index += 1
    return -1

def generate_sensors_channels():
    lines = []
    rooms = topics.get_rooms()
    for room in rooms:
        for sensor in room.sensors:
            e = get_sensor_index(room.sensors, sensor)
            id = f"{room.name.id}_sensor_{sensor.stype}_{e + 1}"
            if count_sensors(room.sensors, sensor.stype) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} {sensor.alias} {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} {sensor.alias}"
            state_topic = topics.Direction.read(sensor.get_mac_topic())
            transformation_pattern = sensor.transformation_pattern
            if sensor.stype == "radar":
                lines += generate_channel(id=id, channel_type="switch", label=label, command_topic=None, state_topic=state_topic, values={"off": '"0"', "on": '"1"'}, unit=None, transformation_pattern=transformation_pattern)
            else:
                lines += generate_channel(id=id, channel_type="number", label=label, command_topic=None, state_topic=state_topic, values={}, unit=sensor.unit, transformation_pattern=transformation_pattern)
    return lines

def generate_heartbeats_channels():
    lines = []
    heartbeats = topics.get_heartbeats()
    for heartbeat in heartbeats:
        id = f"{heartbeat.device.name}_heartbeat"
        label = f"{heartbeat.device.name[:2].upper()}-{heartbeat.device.name[2:].upper()} Heartbeat"
        state_topic = topics.Direction.read(heartbeat.get_mac_topic())
        lines += generate_channel(id=id, channel_type="number", label=label, command_topic=None, state_topic=state_topic, values={}, unit=None, transformation_pattern=None)
    return lines

def generate_alarms_channels():
    lines = []
    rooms = topics.get_rooms()
    for room in rooms:
        for e,alarm in enumerate(room.alarms):
            id = f"{room.name.id}_alarm_{e + 1}"
            if len(room.alarms) > 1:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} CO2 Alarm {e + 1}"
            else:
                label = f"{room.name.id[:2].upper()}-{room.name.id[2:4]} CO2 Alarm"
            command_topic = topics.Direction.write(alarm.get_mac_topic())
            state_topic = topics.Direction.read(alarm.get_mac_topic())
            lines += generate_channel(id=id, channel_type="switch", label=label, command_topic=command_topic, state_topic=state_topic, values={"off": '"0"', "on": '"1"'}, unit=None, transformation_pattern=None)
    return lines

def generate_channels():
    lines = []
    lines += generate_light_channels()
    lines += generate_heating_valves_channels()
    lines += generate_rollers_channels()
    lines += generate_sensors_channels()
    lines += generate_heartbeats_channels()
    lines += generate_alarms_channels()
    with open('channels.txt', 'w') as the_file:
        the_file.write("\n".join(lines))

def generate_link(id):
    data = {}
    data["class"] = "org.openhab.core.thing.link.ItemChannelLink"
    data["value"] = {}
    data["value"]["channelUID"] = {}
    data["value"]["channelUID"]["segments"] = ["mqtt", "topic", "ac491caaaa", "hg_smartschool", id]
    data["value"]["channelUID"]["uid"] = f"mqtt:topic:ac491caaaa:hg_smartschool:{id}"
    data["value"]["configuration"] = {}
    data["value"]["configuration"]["properties"] = {}
    data["value"]["itemName"] = id
    return data

def generate_links():
    data = {}
    rooms = topics.get_rooms()
    for room in rooms:
        for e,light in enumerate(room.lights):
            id = f"{room.name.id}_light_{e + 1}"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
        for e,heating_valve in enumerate(room.heating_valves):
            id = f"{room.name.id}_heating_valve_{e + 1}"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
        for e,roller in enumerate(room.rollers):
            id = f"{room.name.id}_roller_{e + 1}"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
        for sensor in room.sensors:
            e = get_sensor_index(room.sensors, sensor)
            id = f"{room.name.id}_sensor_{sensor.stype}_{e + 1}"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
        for heartbeat in topics.get_heartbeats():
            id = f"{heartbeat.device.name}_heartbeat"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
        for e,alarm in enumerate(room.alarms):
            id = f"{room.name.id}_alarm_{e + 1}"
            key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
            data[key] = generate_link(id)
    export_to_json(data, "links.json")
    
if __name__ == "__main__":
    generate_channels()
    generate_items()
    generate_links()
