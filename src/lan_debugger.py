import asyncio
from typing import Optional
import aiomqtt
from aiomqtt.topic import Topic
from dataclasses import dataclass
from time import time, strftime, gmtime
import credentials
from topics import get_device_by_address
from topics import Device as TopicDevice

def get_millis():
    return round(time() * 1000)

def millis_passed(timestamp):
    return get_millis() - timestamp

@dataclass
class Device:
    address: str
    alias: str
    bcr: int = 4352
    bsr: int = 30765
    cbln: int = 0
    scsr: int = 4184
    reactivate_counter = 0
    reinit_lwip_counter = 0
    timestamp = -1
    responding = True

devices: list[Device] = []

def get_device(topic: Topic) -> Device:
    address = topic.value.split("/")[0]
    for device in devices:
        if device.address == address:
            return device
    alias = address
    topic_device = get_device_by_address(address)
    if topic_device is not None:
        alias = topic_device.device.name
    devices.append(Device(address, alias))
    devices[-1].timestamp = get_millis()
    print(f"[DEVICE]: adding new device [{alias}]")
    return devices[-1]

@dataclass
class Property:
    name: str
    value: int

def get_bit(byteval, idx):
    return int((byteval & (1 << idx)) != 0)

def parse_bcr(bcr: int):
    parsed = []
    parsed.append(Property("Soft Reset", get_bit(bcr, 15)))
    parsed.append(Property("Loopback", get_bit(bcr, 14)))
    parsed.append(Property("Speed Select", get_bit(bcr, 13)))
    parsed.append(Property("Auto-Negotiation Enable",  get_bit(bcr, 12)))
    parsed.append(Property("Power Down", get_bit(bcr, 11)))
    parsed.append(Property("Isolate", get_bit(bcr, 10)))
    parsed.append(Property("Restart Auto-Negotiate", get_bit(bcr, 9)))
    parsed.append(Property("Duplex Mode", get_bit(bcr, 8)))
    return parsed

def parse_bsr(bsr: int):
    parsed = []
    parsed.append(Property("100BASE-T4",  get_bit(bsr, 15)))
    parsed.append(Property("100BASE-TX Full Duplex", get_bit(bsr, 14)))
    parsed.append(Property("100BASE-TX Half Duplex", get_bit(bsr, 13)))
    parsed.append(Property("10BASE-T Full Duplex", get_bit(bsr, 12)))
    parsed.append(Property("10BASE-T Half Duplex", get_bit(bsr, 11)))
    parsed.append(Property("100BASE-T2 Full Duplex", get_bit(bsr, 10)))
    parsed.append(Property("100BASE-T2 Half Duplex", get_bit(bsr, 9)))
    parsed.append(Property("Extended Status", get_bit(bsr, 8)))
    parsed.append(Property("Auto-Negotiate Complete",  get_bit(bsr, 5)))
    parsed.append(Property("Remote Fault", get_bit(bsr, 4)))
    parsed.append(Property("Auto-Negotiate Ability",  get_bit(bsr, 3)))
    parsed.append(Property("Link Status", get_bit(bsr, 2)))
    parsed.append(Property("Jabber Detect", get_bit(bsr, 1)))
    parsed.append(Property("Extended Capabilities", get_bit(bsr, 0)))
    return parsed

def parse_cbln(cbln: int):
    parsed = []
    value = int("".join([str(get_bit(cbln, 15)), str(get_bit(cbln, 14)), str(get_bit(cbln, 13)), str(get_bit(cbln, 12))]), 2)
    parsed.append(Property("Cable Length", get_estimated_cable_length(value)))
    return parsed

def parse_scsr(scsr: int):
    parsed = []
    parsed.append(Property("Autodone", get_bit(scsr, 12)))
    value = int("".join([str(get_bit(scsr, 4)), str(get_bit(scsr, 3)), str(get_bit(scsr, 2))]), 2)
    parsed.append(Property("Speed Indication (?bit order)", value))
    return parsed

def get_estimated_cable_length(value):
    match value:
        case 0|1|2|3:
            return 0
        case   4:
            return 6
        case   5:
            return 17
        case   6:
            return 27
        case   7:
            return 38
        case   8:
            return 49
        case   9:
            return 59
        case   10:
            return 70
        case   11:
            return 81
        case   12:
            return 91
        case   13:
            return 102
        case   14:
            return 113
        case   15:
            return 123
        case _:
            return -1

def add_lan_property_to_device(topic: str, device: Device):
    #bcr, bsr, cbln, scsr = [int(i) for i in topic[1:-1].split(", ")]
    try:
        topic = eval(topic)
        bcr, bsr, cbln, scsr = topic[0]
        reinit_lwip_counter = topic[1]
        reactivate_counter = topic[2]
        if device.bcr != bcr:
            old_bcr_parsed = parse_bcr(device.bcr)
            new_bcr_parsed = parse_bcr(bcr)
            for i in range(len(old_bcr_parsed)):
                if old_bcr_parsed[i].value != new_bcr_parsed[i].value:
                    print(f"[BCR]: [{device.alias}].[{old_bcr_parsed[i].name}] {old_bcr_parsed[i].value} -> {new_bcr_parsed[i].value}")
            device.bcr = bcr
        if device.bsr != bsr:
            old_bsr_parsed = parse_bsr(device.bsr)
            new_bsr_parsed = parse_bsr(bsr)
            for i in range(len(old_bsr_parsed)):
                if old_bsr_parsed[i].value != new_bsr_parsed[i].value:
                    print(f"[BSR]: [{device.alias}].[{old_bsr_parsed[i].name}] {old_bsr_parsed[i].value} -> {new_bsr_parsed[i].value}")
            device.bsr = bsr
        if device.cbln != cbln:
            old_cbln_parsed = parse_cbln(device.cbln)
            new_cbln_parsed = parse_cbln(cbln)
            for i in range(len(old_cbln_parsed)):
                if old_cbln_parsed[i].value != new_cbln_parsed[i].value:
                    if old_cbln_parsed[i].name == "Cable Length" and old_cbln_parsed[i].value == 0:
                        print(f"[CBLN]: [{device.alias}].[{old_cbln_parsed[i].name}] {new_cbln_parsed[i].value}m")
                    else:
                        print(f"[CBLN]: [{device.alias}].[{old_cbln_parsed[i].name}] {old_cbln_parsed[i].value}m -> {new_cbln_parsed[i].value}m")
            device.cbln = cbln
        if device.scsr != scsr:
            old_scsr_parsed = parse_scsr(device.scsr)
            new_scsr_parsed = parse_scsr(scsr)
            for i in range(len(old_scsr_parsed)):
                if old_scsr_parsed[i].value != new_scsr_parsed[i].value:
                    print(f"[SCSR]: [{device.alias}].[{old_scsr_parsed[i].name}] {old_scsr_parsed[i].value} -> {new_scsr_parsed[i].value}")
            device.scsr = scsr
        if device.reactivate_counter != reactivate_counter:
            device.reactivate_counter = reactivate_counter
            print(f"[LAN]: [{device.alias}] reactivate_counter[{reactivate_counter}]")
        if device.reinit_lwip_counter != reinit_lwip_counter:
            device.reinit_lwip_counter = reinit_lwip_counter
            print(f"[LAN]: [{device.alias}] reinit_lwip_counter[{reinit_lwip_counter}]")
    except:
        pass

def parse_message(topic: Topic, payload: str|bytes|bytearray|int|float):
    if isinstance(payload, bytes):
        payload = payload.decode()
    payload = str(payload)
    device = get_device(topic)
    add_lan_property_to_device(payload, device)
    if not device.responding:
        device.responding = True
        millis_passed_s = int(millis_passed(device.timestamp) / 1000)
        print(f"[TIMEOUT] {device.alias} responded after {strftime('%H:%M:%S', gmtime(millis_passed_s))}")
    device.timestamp = get_millis()

    #print(topic, payload)

def check_device_timeout():
    for device in devices:
        if device.responding and millis_passed(device.timestamp) >= 2 * 60 * 1000:
            print(f"[TIMEOUT]: {device.alias} did not respond on time")
            device.responding = False

async def main():
    print("[MAIN]: start")
    async with aiomqtt.Client(hostname=credentials.host, port=credentials.port, username=credentials.username, password=credentials.password) as client:
        await client.subscribe("+/out/lan_testing")
        async for message in client.messages:
            if message is not None and message.payload is not None:
                parse_message(message.topic, message.payload)
            check_device_timeout()
    print("[MAIN]: end")

if __name__ == "__main__":
    asyncio.run(main())
    pass
