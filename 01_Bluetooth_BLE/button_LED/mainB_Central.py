#CENTRAL

import aioble
import bluetooth
import asyncio
from machine import Pin

# BLE UUIDs
SERVICE_UUID = bluetooth.UUID(0x181A)
CHAR_UUID = bluetooth.UUID(0x2A6E)

# GPIO Setup
led = Pin(15, Pin.OUT)  # Use your desired GPIO pin
device_name = "ButtonPeripheral"

def decode(msg):
    return msg.decode()

async def scan_and_connect():
    print("Scanning...")
    async with aioble.scan(5000, interval_us=30000, window_us=30000, active=True) as scanner:
        async for adv in scanner:
            if adv.name() == device_name and SERVICE_UUID in adv.services():
                print(f"Found {adv.name()}")
                return adv.device
    return None

async def listen_for_button(characteristic):
    while True:
        try:
            data = await characteristic.read()
            if data:
                state = decode(data)
                print("Received:", state)
                led.value(1 if state == "ON" else 0)
        except Exception as e:
            print("Read error:", e)
            break
        await asyncio.sleep(0.1)

async def run():
    while True:
        device = await scan_and_connect()
        if not device:
            print("Retrying scan...")
            await asyncio.sleep(2)
            continue

        try:
            conn = await device.connect()
            async with conn:
                service = await conn.service(SERVICE_UUID)
                char = await service.characteristic(CHAR_UUID)
                await listen_for_button(char)
        except Exception as e:
            print("Connection failed:", e)

asyncio.run(run())

