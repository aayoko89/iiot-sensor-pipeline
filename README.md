# IIoT Sensor Data Pipeline 🏭

A real-time factory sensor data pipeline that simulates 3 machines 
sending live temperature, vibration, and pressure data every second.

## Architecture
Producer (Python) → Kafka → Consumer (Python) → InfluxDB → Grafana

## What it does
- Simulates 3 factory machines sending sensor readings every second
- Streams data through Apache Kafka
- Stores every reading in InfluxDB time-series database
- Displays live charts in Grafana dashboard

## Tech Stack
- Python
- Apache Kafka
- InfluxDB 2.7
- Grafana
- Docker

## How to run
1. Clone this repo
2. Run: docker-compose up -d
3. Run: python producer.py
4. Run: python consumer.py
5. Open Grafana at http://localhost:3001