from kafka import KafkaProducer
import json
import time
import random
import threading
from datetime import datetime

# Kafka Producer Initialization
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Thread control event
stop_event = threading.Event()

# Global thread variable
device_thread = None

def run(device):
    while not stop_event.is_set():
        try:
            # Generate device data
            device_record = sensor_tick(device)

            # Send data to Kafka
            producer.send('devices', device_record)
            print(f"Sent: {device_record}")
        except Exception as e:
            print(f"Error sending device data: {e}")

        # Wait for the next tick or exit if stopped
        stop_event.wait(10)

def sensor_tick(device):
    return {
        'device_id': device.id,
        'farm_id': device.farm_id,
        'tower_id': device.tower_id,
        'slot_id': device.slot_id,
        'device_type': device.device_type,
        'status': device.status,
        'timestamp': datetime.now().isoformat(),
        'value': round(random.uniform(0.01, 10), 4),
        'unit': device.unit
    }

def start(device):
    global device_thread  # Declare global scope for the thread variable
    if device_thread and device_thread.is_alive():
        print("Device thread is already running.")
        return

    device_thread = threading.Thread(target=run, args=(device,), daemon=True)
    device_thread.start()

def stop():
    global device_thread  # Ensure you're referencing the global variable
    stop_event.set()
    if device_thread and device_thread.is_alive():
        device_thread.join()
        print("Device thread stopped.")
