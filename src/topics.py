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

@dataclass
class RoomDescription:
    id: str
    label: str
    category: str

class RoomName(RoomDescription, Enum):
    k000 = "k000", "Ulazni prostor", "corridor"
    k001 = "k001", "Ulazni hal", "corridor"
    k002 = "k002", "WC - invalid", "wc"
    k003 = "k003", "WC - ženski", "wc"
    k004 = "k004", "WC - zaposlenici", "wc"
    k005 = "k005", "WC - muški", "wc"
    k006 = "k006", "CUSR", "maintanance"
    k007 = "k007", "Elektro - soba", "maintanance"
    k008 = "k008", "Hodnik", "corridor"
    k009 = "k009", "Biologija", "classroom"
    k010 = "k010", "Informatika", "classroom"
    k011 = "k011", "Kabinet Kem/Bio", "classroomoffice"
    k012 = "k012", "Kabinet Informatika/Mat", "classroomoffice"
    k013 = "k013", "Kabinet laboratorij", "classroomoffice"
    k014 = "k014", "Matematika", "classroom"
    k015 = "k015", "Kemija", "classroom"
    k016 = "k016", "Fizika", "classroom"
    k017 = "k017", "Strojarnica", "maintanance"
    k018 = "k018", "Kabinet fizika", "classroomoffice"
    k019 = "k019", "Multimedijska dvorana", "classroom"
    k020 = "k020", "Stubište", "corridor"
    k100 = "k100", "Stubišni hal", "corridor"
    k101 = "k101", "Knjižnica", "classroom"
    k102 = "k102", "Kabinet knjižnice", "classroomoffice"
    k103 = "k103", "WC - ženski", "wc"
    k104 = "k104", "WC - zaposlenici", "wc"
    k105 = "k105", "WC - muški", "wc"
    k106 = "k106", "WC - invalid", "wc"
    k107 = "k107", "Spremište", "maintanance"
    k108 = "k108", "Kabinet Umjetnost/Vjeronauk", "classroomoffice"
    k109 = "k109", "Hrvatski 1", "classroom"
    k110 = "k110", "Umjetnost/Vjeronauk", "classroom"
    k111 = "k111", "Hrvatski 2", "classroom"
    k112 = "k112", "Kabinet Hrvatski", "classroomoffice"
    k113 = "k113", "Društvo", "classroom"
    k114 = "k114", "Geografija", "classroom"
    k115 = "k115", "Kabinet Geo / Pov", "classroomoffice"
    k116 = "k116", "Povijest", "classroom"
    k117 = "k117", "Jezici 2", "classroom"
    k118 = "k118", "Kabinet jezici", "classroomoffice"
    k119 = "k119", "Jezici 1", "classroom"
    k120 = "k120", "Čistačice", "maintanance"
    k121 = "k121", "Prostor za odmor", "corridor"
    k122 = "k122", "Hodnik", "corridor"
    k123 = "k123", "Stubište", "corridor"
    k124 = "k124", "Kapelica", "corridor"
    k200 = "k200", "Stubišni hal", "corridor"
    k201 = "k201", "Predprostor zbornice", "corridor"
    k202 = "k202", "Čajna kuhinja", "kitchen"
    k203 = "k203", "Predprostor WC", "corridor"
    k204 = "k204", "WC - ženski", "wc"
    k205 = "k205", "WC - muški", "wc"
    k206 = "k206", "WC - invalid", "wc"
    k207 = "k207", "Spremište", "maintanance"
    k208 = "k208", "Zbornica", "office"
    k209 = "k209", "Hodnik", "corridor"
    k210 = "k210", "Jezici 3", "classroom"
    k211 = "k211", "Izborni predmet", "classroom"
    k212 = "k212", "Primanje roditelja", "office"
    k213 = "k213", "Referada", "office"
    k214 = "k214", "Admin/računovodstvo", "office"
    k215 = "k215", "Spremište/Arhiv", "office"
    k216 = "k216", "Tajnik", "office"
    k217 = "k217", "Satničar", "office"
    k218 = "k218", "Državna matura", "office"
    k219 = "k219", "Pedagog/defektolog", "office"
    k220 = "k220", "Prostor za sastanke", "office"
    k221 = "k221", "Ravnatelj", "office"
    k222 = "k222", "WC - uredi", "wc"
    k223 = "k223", "Čajna kuhinja ravnatelj", "kitchen"
    k225 = "k225", "Hodnik", "corridor"
    k226 = "k226", "Stubište", "corridor"
    d000 = "d000", "Dvorište", "outdoor"

class DeviceName(str, Enum):
    k001 = "029773192D9F"
    k007 = "029773191B9F"
    k009 = "0235610921FB"
    k010 = "023561093693"
    k014 = "021991464317"
    k015 = "0297731943AF"
    k016 = "02977319329F"
    k019 = "02977319390F"
    k101a = "029773193117"
    k101b = "02068266447B"
    k109 = "020062033BF7"
    k110 = "020682664A7F"
    k111 = "0206826626E3"
    k113 = "0206826634B3"
    k114 = "020682661AC7"
    k116 = "023561094773"
    k117 = "020682664CC7"
    k119 = "020682663197"
    k208 = "02068266368F"
    k211a = "023561093B73" # net issues
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
    light_index: Optional[int] = None

    def __post_init__(self):
        if self.light_index is None:
            self.light_index = self.index

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/lights/{self.group}/{self.index}"

    def get_sufix(self):
        return f"lights/{self.light_index}"

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
    alias: Optional[str] = None

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/R/relay{self.relay_index}"

    def get_sufix(self):
        return f"lights/{self.light_index}"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class Ventilation:
    device: DeviceName
    relay_index: int

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/R/relay{self.relay_index}"

    def get_sufix(self):
        return f"ventilation"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class AcSocket:
    device: DeviceName
    relay_index: int
    ac_socket_index: int

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/R/relay{self.relay_index}"

    def get_sufix(self):
        return f"ac_socket/{self.ac_socket_index}"

    def get_room_topic(self, room):
        return f"{room.name.name}/{Direction.UNDEFINED.value}/{self.get_sufix()}"

@dataclass
class HeatingValve:
    device: DeviceName
    relay_index: int
    raz: str
    alias: Optional[str] = None

    def get_mac_topic(self):
        return f"{self.device.value}/{Direction.UNDEFINED.value}/R/relay{self.relay_index}"

    def get_sufix(self):
        return f"heating_valve"

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
    lights: Optional[List[Light|RelayLight]] = None
    rollers: Optional[List[Roller]] = None
    sensors: Optional[List] = None
    ventilations: Optional[List[Ventilation]] = None
    ac_sockets: Optional[List[AcSocket]] = None
    heating_valves: Optional[List[HeatingValve]] = None

    def __post_init__(self):
        if self.lights is None:
            self.lights = []
        if self.rollers is None:
            self.rollers = []
        if self.sensors is None:
            self.sensors = []
        if self.ventilations is None:
            self.ventilations = []
        if self.ac_sockets is None:
            self.ac_sockets = []
        if self.heating_valves is None:
            self.heating_valves = []

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
            for ventilation in room.ventilations:
                topic_mac = ventilation.get_mac_topic()
                topic_room = ventilation.get_room_topic(room)
                topics[Direction.write(topic_room)] = Direction.write(topic_mac)
                topics[Direction.read(topic_mac)] = Direction.read(topic_room)
            for ac_socket in room.ac_sockets:
                topic_mac = ac_socket.get_mac_topic()
                topic_room = ac_socket.get_room_topic(room)
                topics[Direction.write(topic_room)] = Direction.write(topic_mac)
                topics[Direction.read(topic_mac)] = Direction.read(topic_room)
            for heating_valve in room.heating_valves:
                topic_mac = heating_valve.get_mac_topic()
                topic_room = heating_valve.get_room_topic(room)
                topics[Direction.write(topic_room)] = Direction.write(topic_mac)
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
        lights = [Light(DeviceName.k001, 1, 1), RelayLight(DeviceName.k001, 10, 2, "Garderoba")],
        rollers = [Roller(DeviceName.k001, 1)],
        heating_valves = [HeatingValve(DeviceName.k001, 3, "RAZ7", "Garderoba"), HeatingValve(DeviceName.k001, 1, "RAZ6", "Kod WC-a")],
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
        lights = [Light(DeviceName.k001, 1, 2, 1)],
        rollers = [Roller(DeviceName.k001, 2)],
        heating_valves = [HeatingValve(DeviceName.k001, 4, "RAZ5", "Jug")],
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
        name = RoomName.k007))

    rooms.append(Room(
        name = RoomName.k008,
        lights = [RelayLight(DeviceName.k007, 1, 1), RelayLight(DeviceName.k007, 2, 1, "Odmor")],
        heating_valves = [HeatingValve(DeviceName.k007, 6, "RAZ10", "Sredina"), HeatingValve(DeviceName.k007, 7, "RAZ11", "Sjever")]
        ))

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
        heating_valves = [HeatingValve(DeviceName.k010, 4, "RAZ4")],
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
        heating_valves = [HeatingValve(DeviceName.k014, 4, "RAZ3")],
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
        heating_valves = [HeatingValve(DeviceName.k015, 4, "RAZ9")],
        rollers = [Roller(DeviceName.k015, 2)],
        sensors = [
            LightSensor(DeviceName.k015, BoardName.s2),
            Co2Sensor(DeviceName.k015, BoardName.s2),
            TemperatureSensor(DeviceName.k015, BoardName.s2),
            PressureSensor(DeviceName.k015, BoardName.s2),
            HumiditySensor(DeviceName.k015, BoardName.s2),
            GasSensor(DeviceName.k015, BoardName.s2),
            AltitudeSensor(DeviceName.k015, BoardName.s2),
            RadarSensor(DeviceName.k015, BoardName.s2)],
        ventilations = [
            Ventilation(DeviceName.k015, 2)]))

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
            RadarSensor(DeviceName.k015, BoardName.s1)],
        ventilations = [
            Ventilation(DeviceName.k015, 1)]))

    rooms.append(Room(
        name = RoomName.k016,
        lights = [Light(DeviceName.k016, 1, 1), Light(DeviceName.k016, 1, 2)],
        heating_valves = [HeatingValve(DeviceName.k016, 4, "RAZ2")],
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
        heating_valves = [HeatingValve(DeviceName.k019, 4, "RAZ1")],
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
        lights = [Light(DeviceName.k101b, 1, 1)],
        heating_valves = [HeatingValve(DeviceName.k109, 4, "RAZ29")],
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
        heating_valves = [HeatingValve(DeviceName.k101b, 4, "RAZ32")],
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
        heating_valves = [HeatingValve(DeviceName.k101b, 4, "RAZ31")], #?
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
        name = RoomName.k105,
        heating_valves = [HeatingValve(DeviceName.k101a, 4, "RAZ30")], #?
        ))

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
        heating_valves = [HeatingValve(DeviceName.k111, 4, "RAZ35")],
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
        heating_valves = [HeatingValve(DeviceName.k110, 4, "RAZ36")],
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
        heating_valves = [HeatingValve(DeviceName.k109, 4, "RAZ28")],
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
        heating_valves = [HeatingValve(DeviceName.k113, 4, "RAZ27")],
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
        heating_valves = [HeatingValve(DeviceName.k114, 4, "RAZ26")],
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
        heating_valves = [HeatingValve(DeviceName.k117, 4, "RAZ37")],
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
        heating_valves = [HeatingValve(DeviceName.k119, 4, "RAZ25")],
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
        name = RoomName.k121,
        lights = [RelayLight(DeviceName.k101b, 9, 1)],
        heating_valves = [HeatingValve(DeviceName.k117, 4, "RAZ33")], #?
        ))

    rooms.append(Room(
        name = RoomName.k122,
        lights = [Light(DeviceName.k101b, 1, 2, 1)],
        heating_valves = [HeatingValve(DeviceName.k116, 4, "RAZ34")], #?
        ))
    
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
        heating_valves = [HeatingValve(DeviceName.k208, 4, "RAZ53"), HeatingValve(DeviceName.k208, 4, "RAZ51")],
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
        name = RoomName.k209,
        lights = [Light(DeviceName.k211a, 1, 2, 1)],
        heating_valves= [HeatingValve(DeviceName.k211a, 4, "RAZ50", "jug"), HeatingValve(DeviceName.k218a, 4, "RAZ49", "sredina"), HeatingValve(DeviceName.k218b, 4, "RAZ48", "sjever")] #?
        ))

    rooms.append(Room(
        name = RoomName.k210,
        lights = [Light(DeviceName.k211a, 2, 1)],
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
        lights = [Light(DeviceName.k211a, 1, 1)],
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
        lights = [Light(DeviceName.k211b, 1, 1)],
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
        lights = [Light(DeviceName.k211c, 1, 1)],
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
        lights = [Light(DeviceName.k218b, 1, 1)],
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
        lights = [Light(DeviceName.k218b, 1, 1)],
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
        name = RoomName.k218,
        lights = [Light(DeviceName.k218c, 1, 1)],
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
        lights = [Light(DeviceName.k218a, 1, 1)],
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
        name = RoomName.k225,
        lights=[RelayLight(DeviceName.k211a, 12, 1)])) # test relay-a hodnik

    rooms.append(Room(
        name = RoomName.k226))

    rooms.append(Room(
        name = RoomName.d000,
        lights = [RelayLight(DeviceName.k001, 12, 1, "Ulična rasvjeta")],
        ac_sockets = [AcSocket(DeviceName.k001, 13, 1)]))

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

def get_light_by_index(lights, index):
    for light in lights:
        if light.light_index == index:
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
