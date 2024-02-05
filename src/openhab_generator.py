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

def generate_items():
    data = {}
    data.update(generate_item_lights())
    data.update(generate_item_heating_valves())
    data.update(generate_group_locations())
    data.update(generate_other_groups())
    export_to_json(data, "items.json")

def generate_channel_light(id, label, command_topic, state_topic):
    lines = []
    lines.append(f'  - id: {id}')
    lines.append(f'    channelTypeUID: mqtt:switch')
    lines.append(f'    label: {label}')
    lines.append(f'    description: null')
    lines.append(f'    configuration:')
    lines.append(f'      commandTopic: {command_topic}') #in
    lines.append(f'      stateTopic: {state_topic}') #out
    lines.append(f'      off: "0"')
    lines.append(f'      on: "1"')
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
            lines += generate_channel_light(id, label, command_topic, state_topic)
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
            lines += generate_channel_light(id, label, command_topic, state_topic)
    return lines

def generate_channels():
    lines = []
    lines += generate_light_channels()
    lines += generate_heating_valves_channels()
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
        if room.heating_valves is not None:
            for e,heating_valve in enumerate(room.heating_valves):
                id = f"{room.name.id}_heating_valve_{e + 1}"
                key = f"{id} -\u003e mqtt:topic:ac491caaaa:hg_smartschool:{id}"
                data[key] = generate_link(id)
    export_to_json(data, "links.json")
    



if __name__ == "__main__":
    generate_channels()
    generate_items()
    generate_links()
