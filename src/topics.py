#!/usr/bin/env python

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class Direction(Enum):
    UNDEFINED = "<DIRECTION>"
    WRITE = "in"
    READ = "out"

    @staticmethod
    def write(topic):
        return topic.replace(Direction.UNDEFINED.value, Direction.WRITE.value)

    @staticmethod
    def read(topic):
        return topic.replace(Direction.UNDEFINED.value, Direction.READ.value)

class RoomName(str, Enum):
    k000 = "Ulazni prostor"
    k001 = "Ulazni hal"
    k002 = "WC - invalid"
    k003 = "WC - ženski"
    k004 = "WC - zaposlenici"
    k005 = "WC - muški"
    k006 = "CUSR"
    k007 = "Elektro - soba"
    k008 = "Hodnik"
    k009 = "Biologija"
    k010 = "Informatika"
    k011 = "Kabinet Kem/Bio"
    k012 = "Kabinet Informatika/Mat"
    k013 = "Kabinet (lab. Skladište"
    k014 = "Matematika"
    k015 = "Kemija"
    k016 = "Fizika"
    k017 = "Strojarnica"
    k018 = "Kabinet fizika"
    k019 = "Multimedijska dvorana"
    k020 = "Stubište"
    k100 = "Stubišni hal"
    k101 = "Knjižnica"
    k102 = "Kabinet knjižnice"
    k103 = "WC - ženski"
    k104 = "WC - zaposlenici"
    k105 = "WC - muški"
    k106 = "WC - invalid"
    k107 = "Spremište"
    k108 = "Kabinet Glazbeni / Likovni"
    k109 = "Hrvatski 1"
    k110 = "glazbeni"
    k111 = "Hrvatski 2"
    k112 = "Kabinet Hrvatski"
    k113 = "Društvo"
    k114 = "Geografija"
    k115 = "Kabinet Geo / Pov"
    k116 = "Povijest"
    k117 = "Jezici 2"
    k118 = "Kabinet Strani Jez"
    k119 = "Jezici 1"
    k120 = "Čistačice"
    k121 = "Hodnik"
    k122 = "Hodnik"
    k123 = "Stubište"
    k124 = "Kapelica"
    k200 = "Stubišni hal"
    k201 = "Predprostor zbornice"
    k202 = "Čajna kuhinja"
    k203 = "Predprostor WC"
    k204 = "WC - ženski"
    k205 = "WC - muški"
    k206 = "WC - invalid"
    k207 = "Spremište"
    k208 = "Zbornica"
    k209 = "Hodnik"
    k210 = "Izborni jezik"
    k211 = "Izborni jezik"
    k212 = "Primanje roditelja"
    k213 = "Referada"
    k214 = "Admin/računovodstvo"
    k215 = "Spremište/Arhiv"
    k216 = "Tajnik"
    k217 = "Satničar"
    k218 = "Državna matura"
    k219 = "Pedagog/defektolog"
    k220 = "Prostor za sastanke"
    k221 = "Ravnatelj"
    k222 = "WC - uredi"
    k223 = "Čajna kuhinja ravnatelj"
    k225 = "Hodnik"
    k226 = "Stubište"

class DeviceName(str, Enum):
    tmp = "obrisi"
    k001 = "029773192D9F"
    k007 = "029773191B9F"
    k009 = "0235610921FB"
    k010 = "023561093693"
    k014 = "021991464317"
    k015 = "0297731943AF"
    k016 = "02977319329F"
    k019 = "02977319390F"
    k101a = "02068266447B"
    k101b = "029773193117"
    k109 = "020062033BF7"
    k110 = "020682664A7F"
    k111 = "0206826626E3"
    k113 = "0206826634B3"
    k114 = "020682661AC7"
    k116 = "023561094773"
    k117 = "020682664CC7"
    k119 = "020682663197"
    k208 = "02068266368F"
    k211a = "023561093B73"
    k211b = "0206826652D7"
    k211c = "020682663FE3"
    k218a = "020682663DE3"
    k218b = "02068266355B"
    k218c = "020682662F63"
    k218d = "020682664DC3"


class BoardName(str, Enum):
    s1 = "S1"
    s2 = "S2"

@dataclass
class Version:
    device: DeviceName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/version"

@dataclass
class Heartbeat:
    device: DeviceName
    
    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/heartbeat"

class Device:
    def __init__(self, device: DeviceName):
        self.device = device
        self.version = Version(self.device)
        self.heartbeat = Heartbeat(self.device)

@dataclass
class Light:
    device: DeviceName
    group: int
    index: int

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/lights/{self.group}/{self.index}"

    def get_sufix(self):
        return f"lights/{self.group}/{self.index}"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class Roller:
    device: DeviceName
    index: int

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/rollo/{self.index}"

    def get_sufix(self):
        return f"roller/{self.index}"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class RelayLight:
    device: DeviceName
    relay_index: int
    light_index: int

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/R/relay{self.relay_index}"

    def get_sufix(self):
        return f"lights/3/{self.light_index}"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class LightSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/light"

    def get_sufix(self):
        return f"sensor/light"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class Co2Sensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/co2"

    def get_sufix(self):
        return f"sensor/co2"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class TemperatureSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/env/temperature"

    def get_sufix(self):
        return f"sensor/temperature"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class PressureSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/env/pressure"

    def get_sufix(self):
        return f"sensor/pressure"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class HumiditySensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/env/humidity"

    def get_sufix(self):
        return f"sensor/humidity"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class GasSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/env/gas"

    def get_sufix(self):
        return f"sensor/gas"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class AltitudeSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/env/altitude"

    def get_sufix(self):
        return f"sensor/altitude"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class RadarSensor:
    device: DeviceName
    board: BoardName

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/{self.board.value}/radar"

    def get_sufix(self):
        return f"sensor/radar"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class PowerCounter:
    pass

@dataclass
class Errors:
    pass

@dataclass
class Room:
    name: RoomName
    lights: Optional[List[Light]] | Optional[List[RelayLight]] = None
    rollers: Optional[List[Roller]] = None
    sensors: Optional[List] = None

    def __post_init__(self):
        if self.lights is None:
            self.lights = []
        if self.rollers is None:
            self.rollers = []
        if self.sensors is None:
            self.sensors = []

    def generate_topics(self):
        topics = {}
        rooms = get_rooms()
        for room in rooms:
            for light in room.lights:
                topic_mac = light.get_mac_topic()
                topic_room = light.get_room_topic(room)
                topics[Direction.write(topic_room)] = Direction.write(topic_mac)
                topics[Direction.read(topic_mac)] = Direction.read(topic_room)
            for roller in room.rollers:
                topic_mac = roller.get_mac_topic()
                topic_room = roller.get_room_topic(room)
                topics[Direction.write(topic_room)] = Direction.write(topic_mac)
                topics[Direction.read(topic_mac)] = Direction.read(topic_room)
            for sensor in room.sensors:
                topic_mac = sensor.get_mac_topic()
                topic_room = sensor.get_room_topic(room)
                #topics[Direction.write(topic_room)] = Direction.write(topic_mac)
                topics[Direction.read(topic_mac)] = Direction.read(topic_room)
        return topics

def get_devices():
    devices = []
    for device_name in DeviceName:
        devices.append(Device(device_name))
    return devices

def get_rooms():
    rooms = []
    rooms.append(Room(
        name = RoomName.k000,
        lights = [Light(DeviceName.k001, 1, 1), Light(DeviceName.k001, 1, 2)],
        rollers = [Roller(DeviceName.k001, 1)],
        sensors = [
            LightSensor(DeviceName.k001, BoardName.s1),
            Co2Sensor(DeviceName.k001, BoardName.s1),
            TemperatureSensor(DeviceName.k001, BoardName.s1),
            PressureSensor(DeviceName.k001, BoardName.s1),
            HumiditySensor(DeviceName.k001, BoardName.s1),
            GasSensor(DeviceName.k001, BoardName.s1),
            AltitudeSensor(DeviceName.k001, BoardName.s1),
            RadarSensor(DeviceName.k001, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k001,
        lights = [Light(DeviceName.k001, 2, 1)],
        rollers = [Roller(DeviceName.k001, 2)],
        sensors = [
            LightSensor(DeviceName.k001, BoardName.s2),
            Co2Sensor(DeviceName.k001, BoardName.s2),
            TemperatureSensor(DeviceName.k001, BoardName.s2),
            PressureSensor(DeviceName.k001, BoardName.s2),
            HumiditySensor(DeviceName.k001, BoardName.s2),
            GasSensor(DeviceName.k001, BoardName.s2),
            AltitudeSensor(DeviceName.k001, BoardName.s2),
            RadarSensor(DeviceName.k001, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k002))

    rooms.append(Room(
        name = RoomName.k003))

    rooms.append(Room(
        name = RoomName.k004))

    rooms.append(Room(
        name = RoomName.k005))

    rooms.append(Room(
        name = RoomName.k006))

    rooms.append(Room(
        name = RoomName.k007,
        lights = [RelayLight(DeviceName.k007, 1, 1)]))

    rooms.append(Room(
        name = RoomName.k008,
        lights = [RelayLight(DeviceName.k007, 2, 1)]))

    rooms.append(Room(
        name = RoomName.k009,
        lights = [Light(DeviceName.k009, 1, 1), Light(DeviceName.k009, 1, 2)],
        rollers = [Roller(DeviceName.k009, 1)],
        sensors = [
            LightSensor(DeviceName.k009, BoardName.s1),
            Co2Sensor(DeviceName.k009, BoardName.s1),
            TemperatureSensor(DeviceName.k009, BoardName.s1),
            PressureSensor(DeviceName.k009, BoardName.s1),
            HumiditySensor(DeviceName.k009, BoardName.s1),
            GasSensor(DeviceName.k009, BoardName.s1),
            AltitudeSensor(DeviceName.k009, BoardName.s1),
            RadarSensor(DeviceName.k009, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k010,
        lights = [Light(DeviceName.k010, 1, 1), Light(DeviceName.k010, 1, 2)],
        rollers = [Roller(DeviceName.k010, 1)],
        sensors = [
            LightSensor(DeviceName.k010, BoardName.s1),
            Co2Sensor(DeviceName.k010, BoardName.s1),
            TemperatureSensor(DeviceName.k010, BoardName.s1),
            PressureSensor(DeviceName.k010, BoardName.s1),
            HumiditySensor(DeviceName.k010, BoardName.s1),
            GasSensor(DeviceName.k010, BoardName.s1),
            AltitudeSensor(DeviceName.k010, BoardName.s1),
            RadarSensor(DeviceName.k010, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k011,
        lights = [Light(DeviceName.k009, 2, 1)],
        rollers = [Roller(DeviceName.k009, 2)],
        sensors = [
            LightSensor(DeviceName.k009, BoardName.s2),
            Co2Sensor(DeviceName.k009, BoardName.s2),
            TemperatureSensor(DeviceName.k009, BoardName.s2),
            PressureSensor(DeviceName.k009, BoardName.s2),
            HumiditySensor(DeviceName.k009, BoardName.s2),
            GasSensor(DeviceName.k009, BoardName.s2),
            AltitudeSensor(DeviceName.k009, BoardName.s2),
            RadarSensor(DeviceName.k009, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k012,
        lights = [Light(DeviceName.k014, 2, 1)],
        rollers = [Roller(DeviceName.k014, 2)],
        sensors = [
            LightSensor(DeviceName.k014, BoardName.s2),
            Co2Sensor(DeviceName.k014, BoardName.s2),
            TemperatureSensor(DeviceName.k014, BoardName.s2),
            PressureSensor(DeviceName.k014, BoardName.s2),
            HumiditySensor(DeviceName.k014, BoardName.s2),
            GasSensor(DeviceName.k014, BoardName.s2),
            AltitudeSensor(DeviceName.k014, BoardName.s2),
            RadarSensor(DeviceName.k014, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k013,
        lights = [Light(DeviceName.k015, 2, 1)],
        rollers = [Roller(DeviceName.k015, 2)],
        sensors = [
            LightSensor(DeviceName.k015, BoardName.s2),
            Co2Sensor(DeviceName.k015, BoardName.s2),
            TemperatureSensor(DeviceName.k015, BoardName.s2),
            PressureSensor(DeviceName.k015, BoardName.s2),
            HumiditySensor(DeviceName.k015, BoardName.s2),
            GasSensor(DeviceName.k015, BoardName.s2),
            AltitudeSensor(DeviceName.k015, BoardName.s2),
            RadarSensor(DeviceName.k015, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k014,
        lights = [Light(DeviceName.k014, 1, 1), Light(DeviceName.k014, 1, 2)],
        rollers = [Roller(DeviceName.k014, 1)],
        sensors = [
            LightSensor(DeviceName.k014, BoardName.s1),
            Co2Sensor(DeviceName.k014, BoardName.s1),
            TemperatureSensor(DeviceName.k014, BoardName.s1),
            PressureSensor(DeviceName.k014, BoardName.s1),
            HumiditySensor(DeviceName.k014, BoardName.s1),
            GasSensor(DeviceName.k014, BoardName.s1),
            AltitudeSensor(DeviceName.k014, BoardName.s1),
            RadarSensor(DeviceName.k014, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k015,
        lights = [Light(DeviceName.k015, 1, 1), Light(DeviceName.k015, 1, 2)],
        rollers = [Roller(DeviceName.k015, 1)],
        sensors = [
            LightSensor(DeviceName.k015, BoardName.s1),
            Co2Sensor(DeviceName.k015, BoardName.s1),
            TemperatureSensor(DeviceName.k015, BoardName.s1),
            PressureSensor(DeviceName.k015, BoardName.s1),
            HumiditySensor(DeviceName.k015, BoardName.s1),
            GasSensor(DeviceName.k015, BoardName.s1),
            AltitudeSensor(DeviceName.k015, BoardName.s1),
            RadarSensor(DeviceName.k015, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k016,
        lights = [Light(DeviceName.k016, 1, 1), Light(DeviceName.k016, 1, 2)],
        rollers = [Roller(DeviceName.k016, 1)],
        sensors = [
            LightSensor(DeviceName.k016, BoardName.s1),
            Co2Sensor(DeviceName.k016, BoardName.s1),
            TemperatureSensor(DeviceName.k016, BoardName.s1),
            PressureSensor(DeviceName.k016, BoardName.s1),
            HumiditySensor(DeviceName.k016, BoardName.s1),
            GasSensor(DeviceName.k016, BoardName.s1),
            AltitudeSensor(DeviceName.k016, BoardName.s1),
            RadarSensor(DeviceName.k016, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k017))

    rooms.append(Room(
        name = RoomName.k018,
        lights = [Light(DeviceName.k016, 2, 1)],
        rollers = [Roller(DeviceName.k016, 2)],
        sensors = [
            LightSensor(DeviceName.k016, BoardName.s2),
            Co2Sensor(DeviceName.k016, BoardName.s2),
            TemperatureSensor(DeviceName.k016, BoardName.s2),
            PressureSensor(DeviceName.k016, BoardName.s2),
            HumiditySensor(DeviceName.k016, BoardName.s2),
            GasSensor(DeviceName.k016, BoardName.s2),
            AltitudeSensor(DeviceName.k016, BoardName.s2),
            RadarSensor(DeviceName.k016, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k019,
        lights = [Light(DeviceName.k019, 1, 1), Light(DeviceName.k019, 1, 2)],
        rollers = [Roller(DeviceName.k019, 1)],
        sensors = [
            LightSensor(DeviceName.k019, BoardName.s1),
            Co2Sensor(DeviceName.k019, BoardName.s1),
            TemperatureSensor(DeviceName.k019, BoardName.s1),
            PressureSensor(DeviceName.k019, BoardName.s1),
            HumiditySensor(DeviceName.k019, BoardName.s1),
            GasSensor(DeviceName.k019, BoardName.s1),
            AltitudeSensor(DeviceName.k019, BoardName.s1),
            RadarSensor(DeviceName.k019, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k020))

    rooms.append(Room(
        name = RoomName.k100,
        lights = [Light(DeviceName.k101b, 1, 1), Light(DeviceName.k101b, 1, 2)],
        rollers = [Roller(DeviceName.k101b, 1)],
        sensors = [
            LightSensor(DeviceName.k101b, BoardName.s1),
            Co2Sensor(DeviceName.k101b, BoardName.s1),
            TemperatureSensor(DeviceName.k101b, BoardName.s1),
            PressureSensor(DeviceName.k101b, BoardName.s1),
            HumiditySensor(DeviceName.k101b, BoardName.s1),
            GasSensor(DeviceName.k101b, BoardName.s1),
            AltitudeSensor(DeviceName.k101b, BoardName.s1),
            RadarSensor(DeviceName.k101b, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k101,
        lights = [Light(DeviceName.k101a, 1, 1), Light(DeviceName.k101a, 1, 2)],
        rollers = [Roller(DeviceName.k101a, 1)],
        sensors = [
            LightSensor(DeviceName.k101a, BoardName.s1),
            Co2Sensor(DeviceName.k101a, BoardName.s1),
            TemperatureSensor(DeviceName.k101a, BoardName.s1),
            PressureSensor(DeviceName.k101a, BoardName.s1),
            HumiditySensor(DeviceName.k101a, BoardName.s1),
            GasSensor(DeviceName.k101a, BoardName.s1),
            AltitudeSensor(DeviceName.k101a, BoardName.s1),
            RadarSensor(DeviceName.k101a, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k102,
        lights = [Light(DeviceName.k101b, 2, 1)],
        rollers = [Roller(DeviceName.k101b, 2)],
        sensors = [
            LightSensor(DeviceName.k101b, BoardName.s2),
            Co2Sensor(DeviceName.k101b, BoardName.s2),
            TemperatureSensor(DeviceName.k101b, BoardName.s2),
            PressureSensor(DeviceName.k101b, BoardName.s2),
            HumiditySensor(DeviceName.k101b, BoardName.s2),
            GasSensor(DeviceName.k101b, BoardName.s2),
            AltitudeSensor(DeviceName.k101b, BoardName.s2),
            RadarSensor(DeviceName.k101b, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k103))

    rooms.append(Room(
        name = RoomName.k104))

    rooms.append(Room(
        name = RoomName.k105))

    rooms.append(Room(
        name = RoomName.k106))

    rooms.append(Room(
        name = RoomName.k107))

    rooms.append(Room(
        name = RoomName.k108,
        lights = [Light(DeviceName.k109, 2, 1)],
        rollers = [Roller(DeviceName.k109, 2)],
        sensors = [
            LightSensor(DeviceName.k109, BoardName.s2),
            Co2Sensor(DeviceName.k109, BoardName.s2),
            TemperatureSensor(DeviceName.k109, BoardName.s2),
            PressureSensor(DeviceName.k109, BoardName.s2),
            HumiditySensor(DeviceName.k109, BoardName.s2),
            GasSensor(DeviceName.k109, BoardName.s2),
            AltitudeSensor(DeviceName.k109, BoardName.s2),
            RadarSensor(DeviceName.k109, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k109,
        lights = [Light(DeviceName.k109, 1, 1), Light(DeviceName.k109, 1, 2)],
        rollers = [Roller(DeviceName.k109, 1)],
        sensors = [
            LightSensor(DeviceName.k109, BoardName.s1),
            Co2Sensor(DeviceName.k109, BoardName.s1),
            TemperatureSensor(DeviceName.k109, BoardName.s1),
            PressureSensor(DeviceName.k109, BoardName.s1),
            HumiditySensor(DeviceName.k109, BoardName.s1),
            GasSensor(DeviceName.k109, BoardName.s1),
            AltitudeSensor(DeviceName.k109, BoardName.s1),
            RadarSensor(DeviceName.k109, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k110,
        lights = [Light(DeviceName.k110, 1, 1), Light(DeviceName.k110, 1, 2)],
        rollers = [Roller(DeviceName.k110, 1)],
        sensors = [
            LightSensor(DeviceName.k110, BoardName.s1),
            Co2Sensor(DeviceName.k110, BoardName.s1),
            TemperatureSensor(DeviceName.k110, BoardName.s1),
            PressureSensor(DeviceName.k110, BoardName.s1),
            HumiditySensor(DeviceName.k110, BoardName.s1),
            GasSensor(DeviceName.k110, BoardName.s1),
            AltitudeSensor(DeviceName.k110, BoardName.s1),
            RadarSensor(DeviceName.k110, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k111,
        lights = [Light(DeviceName.k111, 1, 1), Light(DeviceName.k111, 1, 2)],
        rollers = [Roller(DeviceName.k111, 1)],
        sensors = [
            LightSensor(DeviceName.k111, BoardName.s1),
            Co2Sensor(DeviceName.k111, BoardName.s1),
            TemperatureSensor(DeviceName.k111, BoardName.s1),
            PressureSensor(DeviceName.k111, BoardName.s1),
            HumiditySensor(DeviceName.k111, BoardName.s1),
            GasSensor(DeviceName.k111, BoardName.s1),
            AltitudeSensor(DeviceName.k111, BoardName.s1),
            RadarSensor(DeviceName.k111, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k112,
        lights = [Light(DeviceName.k111, 2, 1)],
        rollers = [Roller(DeviceName.k111, 2)],
        sensors = [
            LightSensor(DeviceName.k111, BoardName.s2),
            Co2Sensor(DeviceName.k111, BoardName.s2),
            TemperatureSensor(DeviceName.k111, BoardName.s2),
            PressureSensor(DeviceName.k111, BoardName.s2),
            HumiditySensor(DeviceName.k111, BoardName.s2),
            GasSensor(DeviceName.k111, BoardName.s2),
            AltitudeSensor(DeviceName.k111, BoardName.s2),
            RadarSensor(DeviceName.k111, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k113,
        lights = [Light(DeviceName.k113, 1, 1), Light(DeviceName.k113, 1, 2)],
        rollers = [Roller(DeviceName.k113, 1)],
        sensors = [
            LightSensor(DeviceName.k113, BoardName.s1),
            Co2Sensor(DeviceName.k113, BoardName.s1),
            TemperatureSensor(DeviceName.k113, BoardName.s1),
            PressureSensor(DeviceName.k113, BoardName.s1),
            HumiditySensor(DeviceName.k113, BoardName.s1),
            GasSensor(DeviceName.k113, BoardName.s1),
            AltitudeSensor(DeviceName.k113, BoardName.s1),
            RadarSensor(DeviceName.k113, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k114,
        lights = [Light(DeviceName.k114, 1, 1), Light(DeviceName.k114, 1, 2)],
        rollers = [Roller(DeviceName.k114, 1)],
        sensors = [
            LightSensor(DeviceName.k114, BoardName.s1),
            Co2Sensor(DeviceName.k114, BoardName.s1),
            TemperatureSensor(DeviceName.k114, BoardName.s1),
            PressureSensor(DeviceName.k114, BoardName.s1),
            HumiditySensor(DeviceName.k114, BoardName.s1),
            GasSensor(DeviceName.k114, BoardName.s1),
            AltitudeSensor(DeviceName.k114, BoardName.s1),
            RadarSensor(DeviceName.k114, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k115,
        lights = [Light(DeviceName.k116, 2, 1)],
        rollers = [Roller(DeviceName.k116, 2)],
        sensors = [
            LightSensor(DeviceName.k116, BoardName.s2),
            Co2Sensor(DeviceName.k116, BoardName.s2),
            TemperatureSensor(DeviceName.k116, BoardName.s2),
            PressureSensor(DeviceName.k116, BoardName.s2),
            HumiditySensor(DeviceName.k116, BoardName.s2),
            GasSensor(DeviceName.k116, BoardName.s2),
            AltitudeSensor(DeviceName.k116, BoardName.s2),
            RadarSensor(DeviceName.k116, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k116,
        lights = [Light(DeviceName.k116, 1, 1), Light(DeviceName.k116, 1, 2)],
        rollers = [Roller(DeviceName.k116, 1)],
        sensors = [
            LightSensor(DeviceName.k116, BoardName.s1),
            Co2Sensor(DeviceName.k116, BoardName.s1),
            TemperatureSensor(DeviceName.k116, BoardName.s1),
            PressureSensor(DeviceName.k116, BoardName.s1),
            HumiditySensor(DeviceName.k116, BoardName.s1),
            GasSensor(DeviceName.k116, BoardName.s1),
            AltitudeSensor(DeviceName.k116, BoardName.s1),
            RadarSensor(DeviceName.k116, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k117,
        lights = [Light(DeviceName.k117, 1, 1), Light(DeviceName.k117, 1, 2)],
        rollers = [Roller(DeviceName.k117, 1)],
        sensors = [
            LightSensor(DeviceName.k117, BoardName.s1),
            Co2Sensor(DeviceName.k117, BoardName.s1),
            TemperatureSensor(DeviceName.k117, BoardName.s1),
            PressureSensor(DeviceName.k117, BoardName.s1),
            HumiditySensor(DeviceName.k117, BoardName.s1),
            GasSensor(DeviceName.k117, BoardName.s1),
            AltitudeSensor(DeviceName.k117, BoardName.s1),
            RadarSensor(DeviceName.k117, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k118,
        lights = [Light(DeviceName.k117, 2, 1)],
        rollers = [Roller(DeviceName.k117, 2)],
        sensors = [
            LightSensor(DeviceName.k117, BoardName.s2),
            Co2Sensor(DeviceName.k117, BoardName.s2),
            TemperatureSensor(DeviceName.k117, BoardName.s2),
            PressureSensor(DeviceName.k117, BoardName.s2),
            HumiditySensor(DeviceName.k117, BoardName.s2),
            GasSensor(DeviceName.k117, BoardName.s2),
            AltitudeSensor(DeviceName.k117, BoardName.s2),
            RadarSensor(DeviceName.k117, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k119,
        lights = [Light(DeviceName.k119, 1, 1), Light(DeviceName.k119, 1, 2)],
        rollers = [Roller(DeviceName.k119, 1)],
        sensors = [
            LightSensor(DeviceName.k119, BoardName.s1),
            Co2Sensor(DeviceName.k119, BoardName.s1),
            TemperatureSensor(DeviceName.k119, BoardName.s1),
            PressureSensor(DeviceName.k119, BoardName.s1),
            HumiditySensor(DeviceName.k119, BoardName.s1),
            GasSensor(DeviceName.k119, BoardName.s1),
            AltitudeSensor(DeviceName.k119, BoardName.s1),
            RadarSensor(DeviceName.k119, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k120,
        lights = [Light(DeviceName.k119, 2, 1)],
        rollers = [Roller(DeviceName.k119, 2)],
        sensors = [
            LightSensor(DeviceName.k119, BoardName.s2),
            Co2Sensor(DeviceName.k119, BoardName.s2),
            TemperatureSensor(DeviceName.k119, BoardName.s2),
            PressureSensor(DeviceName.k119, BoardName.s2),
            HumiditySensor(DeviceName.k119, BoardName.s2),
            GasSensor(DeviceName.k119, BoardName.s2),
            AltitudeSensor(DeviceName.k119, BoardName.s2),
            RadarSensor(DeviceName.k119, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k121))

    rooms.append(Room(
        name = RoomName.k122))
    
    rooms.append(Room(
        name = RoomName.k123))

    rooms.append(Room(
        name = RoomName.k124,
        lights = [Light(DeviceName.k101a, 2, 1)],
        rollers = [Roller(DeviceName.k101a, 2)],
        sensors = [
            LightSensor(DeviceName.k101a, BoardName.s2),
            Co2Sensor(DeviceName.k101a, BoardName.s2),
            TemperatureSensor(DeviceName.k101a, BoardName.s2),
            PressureSensor(DeviceName.k101a, BoardName.s2),
            HumiditySensor(DeviceName.k101a, BoardName.s2),
            GasSensor(DeviceName.k101a, BoardName.s2),
            AltitudeSensor(DeviceName.k101a, BoardName.s2),
            RadarSensor(DeviceName.k101a, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k200))

    rooms.append(Room(
        name = RoomName.k201))

    rooms.append(Room(
        name = RoomName.k202))

    rooms.append(Room(
        name = RoomName.k203))

    rooms.append(Room(
        name = RoomName.k204))

    rooms.append(Room(
        name = RoomName.k205))

    rooms.append(Room(
        name = RoomName.k206))

    rooms.append(Room(
        name = RoomName.k207))

    rooms.append(Room(
        name = RoomName.k208,
        lights = [Light(DeviceName.k208, 1, 1), Light(DeviceName.k208, 1, 2)],
        rollers = [Roller(DeviceName.k208, 1)],
        sensors = [
            LightSensor(DeviceName.k208, BoardName.s1),
            Co2Sensor(DeviceName.k208, BoardName.s1),
            TemperatureSensor(DeviceName.k208, BoardName.s1),
            PressureSensor(DeviceName.k208, BoardName.s1),
            HumiditySensor(DeviceName.k208, BoardName.s1),
            GasSensor(DeviceName.k208, BoardName.s1),
            AltitudeSensor(DeviceName.k208, BoardName.s1),
            RadarSensor(DeviceName.k208, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k209, #k225? koji je hodnik koji
        lights = [RelayLight(DeviceName.k211a, 12, 1)]))

    rooms.append(Room(
        name = RoomName.k210,
        lights = [Light(DeviceName.k211a, 1, 1), Light(DeviceName.k211a, 1, 2)],
        rollers = [Roller(DeviceName.k211a, 1)],
        sensors = [
            LightSensor(DeviceName.k211a, BoardName.s1),
            Co2Sensor(DeviceName.k211a, BoardName.s1),
            TemperatureSensor(DeviceName.k211a, BoardName.s1),
            PressureSensor(DeviceName.k211a, BoardName.s1),
            HumiditySensor(DeviceName.k211a, BoardName.s1),
            GasSensor(DeviceName.k211a, BoardName.s1),
            AltitudeSensor(DeviceName.k211a, BoardName.s1),
            RadarSensor(DeviceName.k211a, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k211,
        lights = [Light(DeviceName.k211a, 2, 1)],
        rollers = [Roller(DeviceName.k211a, 2)],
        sensors = [
            LightSensor(DeviceName.k211a, BoardName.s2),
            Co2Sensor(DeviceName.k211a, BoardName.s2),
            TemperatureSensor(DeviceName.k211a, BoardName.s2),
            PressureSensor(DeviceName.k211a, BoardName.s2),
            HumiditySensor(DeviceName.k211a, BoardName.s2),
            GasSensor(DeviceName.k211a, BoardName.s2),
            AltitudeSensor(DeviceName.k211a, BoardName.s2),
            RadarSensor(DeviceName.k211a, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k212,
        lights = [Light(DeviceName.k211b, 1, 1), Light(DeviceName.k211b, 1, 2)],
        rollers = [Roller(DeviceName.k211b, 1)],
        sensors = [
            LightSensor(DeviceName.k211b, BoardName.s1),
            Co2Sensor(DeviceName.k211b, BoardName.s1),
            TemperatureSensor(DeviceName.k211b, BoardName.s1),
            PressureSensor(DeviceName.k211b, BoardName.s1),
            HumiditySensor(DeviceName.k211b, BoardName.s1),
            GasSensor(DeviceName.k211b, BoardName.s1),
            AltitudeSensor(DeviceName.k211b, BoardName.s1),
            RadarSensor(DeviceName.k211b, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k213,
        lights = [Light(DeviceName.k211c, 1, 1), Light(DeviceName.k211c, 1, 2)],
        rollers = [Roller(DeviceName.k211c, 1)],
        sensors = [
            LightSensor(DeviceName.k211c, BoardName.s1),
            Co2Sensor(DeviceName.k211c, BoardName.s1),
            TemperatureSensor(DeviceName.k211c, BoardName.s1),
            PressureSensor(DeviceName.k211c, BoardName.s1),
            HumiditySensor(DeviceName.k211c, BoardName.s1),
            GasSensor(DeviceName.k211c, BoardName.s1),
            AltitudeSensor(DeviceName.k211c, BoardName.s1),
            RadarSensor(DeviceName.k211c, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k214,
        lights = [Light(DeviceName.k211c, 2, 1)],
        rollers = [Roller(DeviceName.k211c, 2)],
        sensors = [
            LightSensor(DeviceName.k211c, BoardName.s2),
            Co2Sensor(DeviceName.k211c, BoardName.s2),
            TemperatureSensor(DeviceName.k211c, BoardName.s2),
            PressureSensor(DeviceName.k211c, BoardName.s2),
            HumiditySensor(DeviceName.k211c, BoardName.s2),
            GasSensor(DeviceName.k211c, BoardName.s2),
            AltitudeSensor(DeviceName.k211c, BoardName.s2),
            RadarSensor(DeviceName.k211c, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k215,
        lights = [Light(DeviceName.k218b, 1, 1), Light(DeviceName.k218b, 1, 2)],
        rollers = [Roller(DeviceName.k218b, 1)],
        sensors = [
            LightSensor(DeviceName.k218b, BoardName.s1),
            Co2Sensor(DeviceName.k218b, BoardName.s1),
            TemperatureSensor(DeviceName.k218b, BoardName.s1),
            PressureSensor(DeviceName.k218b, BoardName.s1),
            HumiditySensor(DeviceName.k218b, BoardName.s1),
            GasSensor(DeviceName.k218b, BoardName.s1),
            AltitudeSensor(DeviceName.k218b, BoardName.s1),
            RadarSensor(DeviceName.k218b, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k216,
        lights = [Light(DeviceName.k218d, 2, 1)],
        rollers = [Roller(DeviceName.k218d, 2)],
        sensors = [
            LightSensor(DeviceName.k218d, BoardName.s2),
            Co2Sensor(DeviceName.k218d, BoardName.s2),
            TemperatureSensor(DeviceName.k218d, BoardName.s2),
            PressureSensor(DeviceName.k218d, BoardName.s2),
            HumiditySensor(DeviceName.k218d, BoardName.s2),
            GasSensor(DeviceName.k218d, BoardName.s2),
            AltitudeSensor(DeviceName.k218d, BoardName.s2),
            RadarSensor(DeviceName.k218d, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k217,
        lights = [Light(DeviceName.tmp, 1, 1), Light(DeviceName.tmp, 1, 2)],
        rollers = [Roller(DeviceName.tmp, 1)],
        sensors = [
            LightSensor(DeviceName.tmp, BoardName.s1),
            Co2Sensor(DeviceName.tmp, BoardName.s1),
            TemperatureSensor(DeviceName.tmp, BoardName.s1),
            PressureSensor(DeviceName.tmp, BoardName.s1),
            HumiditySensor(DeviceName.tmp, BoardName.s1),
            GasSensor(DeviceName.tmp, BoardName.s1),
            AltitudeSensor(DeviceName.tmp, BoardName.s1),
                RadarSensor(DeviceName.tmp, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k218,
        lights = [Light(DeviceName.k218c, 1, 1), Light(DeviceName.k218c, 1, 2)],
        rollers = [Roller(DeviceName.k218c, 1)],
        sensors = [
            LightSensor(DeviceName.k218c, BoardName.s1),
            Co2Sensor(DeviceName.k218c, BoardName.s1),
            TemperatureSensor(DeviceName.k218c, BoardName.s1),
            PressureSensor(DeviceName.k218c, BoardName.s1),
            HumiditySensor(DeviceName.k218c, BoardName.s1),
            GasSensor(DeviceName.k218c, BoardName.s1),
            AltitudeSensor(DeviceName.k218c, BoardName.s1),
            RadarSensor(DeviceName.k218c, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k219,
        lights = [Light(DeviceName.k218c, 2, 1)],
        rollers = [Roller(DeviceName.k218c, 2)],
        sensors = [
            LightSensor(DeviceName.k218c, BoardName.s2),
            Co2Sensor(DeviceName.k218c, BoardName.s2),
            TemperatureSensor(DeviceName.k218c, BoardName.s2),
            PressureSensor(DeviceName.k218c, BoardName.s2),
            HumiditySensor(DeviceName.k218c, BoardName.s2),
            GasSensor(DeviceName.k218c, BoardName.s2),
            AltitudeSensor(DeviceName.k218c, BoardName.s2),
            RadarSensor(DeviceName.k218c, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k220,
        lights = [Light(DeviceName.k218a, 2, 1)],
        rollers = [Roller(DeviceName.k218a, 2)],
        sensors = [
            LightSensor(DeviceName.k218a, BoardName.s2),
            Co2Sensor(DeviceName.k218a, BoardName.s2),
            TemperatureSensor(DeviceName.k218a, BoardName.s2),
            PressureSensor(DeviceName.k218a, BoardName.s2),
            HumiditySensor(DeviceName.k218a, BoardName.s2),
            GasSensor(DeviceName.k218a, BoardName.s2),
            AltitudeSensor(DeviceName.k218a, BoardName.s2),
            RadarSensor(DeviceName.k218a, BoardName.s2)
            ]))

    rooms.append(Room(
        name = RoomName.k221,
        lights = [Light(DeviceName.k218a, 1, 1), Light(DeviceName.k218a, 1, 2)],
        rollers = [Roller(DeviceName.k218a, 1)],
        sensors = [
            LightSensor(DeviceName.k218a, BoardName.s1),
            Co2Sensor(DeviceName.k218a, BoardName.s1),
            TemperatureSensor(DeviceName.k218a, BoardName.s1),
            PressureSensor(DeviceName.k218a, BoardName.s1),
            HumiditySensor(DeviceName.k218a, BoardName.s1),
            GasSensor(DeviceName.k218a, BoardName.s1),
            AltitudeSensor(DeviceName.k218a, BoardName.s1),
            RadarSensor(DeviceName.k218a, BoardName.s1)
            ]))

    rooms.append(Room(
        name = RoomName.k222))

    rooms.append(Room(
        name = RoomName.k223))

    rooms.append(Room(
        name = RoomName.k225))

    rooms.append(Room(
        name = RoomName.k226))

    return rooms

def get_topics():
    rooms = get_rooms()
    topics = {}
    for room in rooms:
        t = room.generate_topics()
        for k,v in t.items():
            topics[k] = v
    return topics

def get_room_by_name(room_name):
    rooms = get_rooms()
    for room in rooms:
        if room.name.name == room_name:
            return room
    return None

def get_light_by_group_and_index(lights, group, index):
    for light in lights:
        if light.group == group and light.index == index:
            return light
    return None

def get_device_by_name(device_name):
    devices = get_devices()
    for device in devices:
        if device.device.name == device_name:
            return device
    return None


if __name__ == "__main__":
    rooms = get_rooms()
    topics = {}
    for room in rooms:
        t = room.generate_topics()
        for k,v in t.items():
            topics[k] = v
