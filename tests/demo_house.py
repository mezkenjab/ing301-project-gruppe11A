from smarthouse.domain import (
    SmartHouse,
    TemperatureSensor,
    MotionSensor,
    SmartBulb,
    SmartLock,
    HeatPump,
    PanelHeater,
)

DEMO_HOUSE = SmartHouse()

# Floors
f0 = DEMO_HOUSE.register_floor(0)
f1 = DEMO_HOUSE.register_floor(1)
f2 = DEMO_HOUSE.register_floor(2)

# Rooms (12 total, sum = 156.55)
r1 = DEMO_HOUSE.register_room(f0, 18.0, "Basement Storage")
r2 = DEMO_HOUSE.register_room(f0, 12.5, "Laundry")
r3 = DEMO_HOUSE.register_room(f0, 13.0, "Workshop")

r4 = DEMO_HOUSE.register_room(f1, 25.0, "Living Room")
r5 = DEMO_HOUSE.register_room(f1, 14.0, "Kitchen")
r6 = DEMO_HOUSE.register_room(f1, 10.5, "Bathroom")
r7 = DEMO_HOUSE.register_room(f1, 9.5, "Hallway")
r8 = DEMO_HOUSE.register_room(f1, 8.0, "Office")

r9 = DEMO_HOUSE.register_room(f2, 16.0, "Master Bedroom")
r10 = DEMO_HOUSE.register_room(f2, 9.0, "Dressing Room")
r11 = DEMO_HOUSE.register_room(f2, 11.0, "Bedroom 2")
r12 = DEMO_HOUSE.register_room(f2, 10.05, "Bathroom 2")

# Devices (14 total)

d1 = TemperatureSensor(
    "4d8b1d62-7921-4917-9b70-bbd31f6e2e8e",
    "Xiaomi",
    "Mi Temperature Sensor"
)
DEMO_HOUSE.register_device(r4, d1)

d2 = MotionSensor(
    "cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5",
    "NebulaGuard Innovations",
    "MoveZ Detect 69"
)
DEMO_HOUSE.register_device(r9, d2)

d3 = SmartBulb(
    "6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28",
    "Elysian Tech",
    "Lumina Glow 4000"
)
DEMO_HOUSE.register_device(r7, d3)

d4 = SmartLock("11111111-1111-1111-1111-111111111111", "Yale", "Doorman")
DEMO_HOUSE.register_device(r4, d4)

d5 = HeatPump("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Mitsubishi", "MSZ-AP", 22)
DEMO_HOUSE.register_device(r4, d5)

d6 = PanelHeater("33333333-3333-3333-3333-333333333333", "Adax", "Neo", 21)
DEMO_HOUSE.register_device(r11, d6)

d7 = SmartBulb("44444444-4444-4444-4444-444444444444", "Philips", "Hue Color")
DEMO_HOUSE.register_device(r4, d7)

d8 = SmartBulb("55555555-5555-5555-5555-555555555555", "Philips", "Hue Color")
DEMO_HOUSE.register_device(r5, d8)

d9 = SmartBulb("66666666-6666-6666-6666-666666666666", "Philips", "Hue White")
DEMO_HOUSE.register_device(r9, d9)

d10 = MotionSensor("77777777-7777-7777-7777-777777777777", "Aqara", "Motion Sensor P1")
DEMO_HOUSE.register_device(r6, d10)

d11 = TemperatureSensor("88888888-8888-8888-8888-888888888888", "Netatmo", "Indoor Module")
DEMO_HOUSE.register_device(r9, d11)

d12 = SmartLock("99999999-9999-9999-9999-999999999999", "Nuki", "Smart Lock 4.0")
DEMO_HOUSE.register_device(r1, d12)

d13 = SmartBulb("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "IKEA", "TRADFRI Bulb E27")
DEMO_HOUSE.register_device(r8, d13)

d14 = TemperatureSensor("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", "Tibber", "Temp Sensor")
DEMO_HOUSE.register_device(r12, d14)