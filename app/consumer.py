from kafka import KafkaConsumer
import requests
import json
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="secret",
    database="gaiascycle",
    port=3309
)
cursor = conn.cursor()

# Kafka consumer initialization
consumer = KafkaConsumer(
    'devices',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# API endpoint for writing data to the database
API_URL = "http://localhost:8000/api/devices/"  # Replace with your actual API endpoint

for message in consumer:
    device_data = message.value  # Data from Kafka
    try:
        # Send device data to the API
        response = requests.post(API_URL, json=device_data)
        response.raise_for_status()  # Raise an error for HTTP failures
        print(f"Data successfully sent to API: {device_data}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data to API: {e}")


# Connect to MySQL


for message in consumer:
    transaction = message.value
    account_id = transaction['account_id']
    timestamp = transaction['timestamp']
    crypto_type = transaction['crypto_type']
    amount = transaction['amount']
    price = transaction['price']

    # Insert transaction into MySQL
    cursor.execute(
        "INSERT INTO transactions (account_id, timestamp, crypto_type, amount, price) VALUES (%s, %s, %s, %s, %s)",
        (account_id, timestamp, crypto_type, amount, price)
    )
    conn.commit()
    print(f"Written to MySQL: {transaction}")