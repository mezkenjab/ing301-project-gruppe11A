import random
from datetime import datetime


class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit


class Device:
    def __init__(self, id, supplier, model_name, device_type="Device"):
        self.id = id
        self.supplier = supplier
        self.model_name = model_name
        self.device_type = device_type
        self.room = None
        
    def is_actuator(self):
        return False

    def is_sensor(self):
        return False

    def get_device_type(self):
        return self.device_type


class Sensor(Device):
    def __init__(self, id, supplier, model_name, unit, device_type="Sensor"):
        super().__init__(id, supplier, model_name, device_type)
        self.unit = unit

    def is_sensor(self):
        return True

    def last_measurement(self):
        timestamp = datetime.now().isoformat()
        value = random.uniform(0, 100)
        return Measurement(timestamp, value, self.unit)

    def get_device_type(self):
        return self.device_type


class Actuator(Device):
    def __init__(self, id, supplier, model_name, device_type="Actuator", target_value=None):
        super().__init__(id, supplier, model_name, device_type)
        self._active = False
        self.target_value = target_value
        self.room = None

    def is_actuator(self):
        return True

    def turn_on(self, target_value=None):
        self._active = True
        if target_value is not None:
            self.target_value = target_value

    def turn_off(self):
        self._active = False

    def is_active(self):
        return self._active

    def get_device_type(self):
        return self.device_type


class Floor:
    def __init__(self, level):
        self.level = level
        self.rooms = []


class Room:
    def __init__(self, floor, room_size, room_name=None):
        self.floor = floor
        self.room_size = room_size
        self.room_name = room_name
        self.devices = []

class TemperatureSensor(Sensor):
    def __init__(self, id, supplier, model_name):
        super().__init__(id, supplier, model_name, "°C", "Temperature Sensor")
    def get_device_type(self):
        return "Temperature Sensor"


class MotionSensor(Sensor):
    def __init__(self, id, supplier, model_name):
        super().__init__(id, supplier, model_name, "motion", "Motion Sensor")

    def get_device_type(self):
        return "Motion Sensor"


class SmartBulb(Actuator):
    def __init__(self, id, supplier, model_name):
        super().__init__(id, supplier, model_name, "Light Bulp")

    def get_device_type(self):
        return "smart Bulb"


class SmartLock(Actuator):
    def __init__(self, id, supplier, model_name):
        super().__init__(id, supplier, model_name, "Smart Lock")

    def get_device_type(self):
        return "Smart Lock"


class HeatPump(Actuator):
    def __init__(self, id, supplier, model_name, target_value=None):
        super().__init__(id, supplier, model_name, "Heat Pump", target_value)

    def get_device_type(self):
        return "Heat Pump"


class PanelHeater(Actuator):
    def __init__(self, id, supplier, model_name, target_value=None):
        super().__init__(id, supplier, model_name, "Panel Heater", target_value)

    def get_device_type(self):
        return "Panel Heater"

class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def __init__(self):
        self.floors = []
        self.devices = {}

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        floor = Floor(level)
        self.floors.append(floor)
        self.floors.sort(key=lambda f: f.level)
        return floor

    def register_room(self, floor, room_size, room_name=None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        room = Room(floor, room_size, room_name)
        floor.rooms.append(room)
        return room

    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return sorted(self.floors, key=lambda f: f.level)

    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        rooms = []
        for floor in self.floors:
            rooms.extend(floor.rooms)
        return rooms

    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        total_area = 0
        for room in self.get_rooms():
            total_area += room.room_size
        return total_area

    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        if getattr(device, "room", None) is not None:
            old_room = device.room
            if device in old_room.devices:
                old_room.devices.remove(device)

        room.devices.append(device)
        device.room = room
        self.devices[device.id] = device

    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        return self.devices.get(device_id)

    def get_devices(self):
        return list(self.devices.values())

    def get_device_by_id(self, device_id):
        return self.get_device(device_id)
    
    def move_device(self, device, new_room):
        if device.room is not None and device in device.room.devices:
            device.room.devices.remove(device)
        new_room.devices.append(device)
        device.room = new_room