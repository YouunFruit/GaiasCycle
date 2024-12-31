# Kafka Integration

<!-- 
Include:
1. How Kafka is used in the app.
2. Setting up Kafka.
3. Example use cases (e.g., messaging or logging).
-->
## Kafka in the Application

### 1. How Kafka is Used in the App
Kafka is implemented as a false data producer. This allows us to display the web app as if it is already in use.:
- Streaming device telemetry data from producers to consumers.
- Feeding real-time data into the database for storage and analytics.
- Supporting asynchronous workflows like logging or background processing.

---

### 2. Setting Up Kafka
The kafka begins producing as soon as you create a device. It will instantiate a thread, producing data for it. The consumer will run automatically.

#### Prerequisites
These are the packages installed through the requirements.txt
- **kafka-python**
- **spark-sql-kafka**
- **kafka-python-ng**
- **mysql-connector-python**

