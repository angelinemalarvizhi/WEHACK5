# AegisEdge

## Edge-Intelligent Environmental Monitoring and Early Warning System

AegisEdge is a distributed environmental monitoring and early warning system
for localized detection and assessment of environmental hazards.

The system combines distributed sensor nodes, edge processing, sensor fusion,
multi-hazard risk analysis, FPGA acceleration, event-driven communication,
and centralized monitoring.

---

## 1. System Overview

The system consists of distributed environmental monitoring nodes connected
to an edge intelligence gateway.

Sensor measurements are acquired, pre-processed and combined at the edge.
The resulting data is analysed for abnormal environmental conditions and
potential hazards.

Normal sensor data can be stored locally, while significant events are
forwarded to the backend for visualization, storage and further analysis.

### Processing Flow

    Environmental Sensor Nodes
              |
              v
        Data Acquisition
              |
              v
         Pre-processing
              |
              v
          Sensor Fusion
              |
              v
       Feature Extraction
              |
              v
        Edge Intelligence
              |
              v
      Multi-Hazard Analysis
              |
              v
        Risk Assessment
              |
          +---+---+
          |       |
          v       v
     Local Storage  Event Generation
                         |
                         v
                  Communication
                         |
                         v
                      Backend
                         |
                         v
                     Dashboard

---

## 2. Environmental Sensor Nodes

The system is organized into specialized monitoring nodes based on the
environmental conditions being monitored.

### 2.1 River / Flood Node

Parameters:

- Water level
- Rainfall
- Soil moisture
- Temperature
- Humidity

Primary use:

- Flood monitoring
- Flash-flood detection
- Water-level trend analysis

### 2.2 Forest / Fire Node

Parameters:

- Temperature
- Humidity
- Smoke
- Gas concentration
- Vibration

Primary use:

- Fire detection
- Smoke detection
- Environmental condition monitoring

### 2.3 Urban / Pollution Node

Parameters:

- PM2.5
- PM10
- Gas concentration
- Temperature
- Humidity

Primary use:

- Air-quality monitoring
- Pollution event detection
- Industrial/environmental incident monitoring

The current prototype uses software-generated sensor data for development and
testing. The same data interface can be connected to physical sensors during
hardware deployment.

---

## 3. Edge Intelligence

The edge layer performs local processing before data is transmitted to a
central system.

### Processing Stages

    Sensor Data
        |
        v
    Data Acquisition
        |
        v
    Pre-processing
        |
        v
    Sensor Fusion
        |
        v
    Feature Extraction
        |
        v
    Anomaly Detection
        |
        v
    Risk Assessment
        |
        v
    Event Decision

The edge-first approach reduces unnecessary communication and allows local
monitoring and event assessment during network interruptions.

---

## 4. Multi-Hazard Analysis

The system is designed to analyse multiple environmental hazards.

### Supported Hazard Categories

- Flood and flash-flood conditions
- Forest fire indicators
- Air pollution events
- Landslide indicators
- Extreme environmental conditions
- Industrial safety events

The risk analysis module produces:

- Hazard type
- Risk score
- Confidence score
- Severity level
- Risk trend
- Event status

### Risk Classification

    NORMAL
       |
       v
    WARNING
       |
       v
    CRITICAL

Risk classification is based on environmental measurements, sensor
relationships and changes observed over time.

---

## 5. Hardware Architecture

### 5.1 PYNQ-Z2

The PYNQ-Z2 is used as the edge intelligence platform.

Responsibilities include:

- Sensor data acquisition
- Data preprocessing
- Sensor fusion
- Feature processing
- Edge inference
- Risk calculation
- Local data handling

### 5.2 Artix-7

The Artix-7 FPGA is used as a hardware acceleration platform for selected
computational workloads in the environmental analysis pipeline.

The acceleration stage will be evaluated using:

- Processing latency
- Throughput
- FPGA resource utilization

The objective is to compare the selected workload between software execution
and FPGA-based execution.

---

## 6. Communication Layer

The architecture is designed to support different communication technologies
depending on deployment requirements.

Supported communication options include:

- Wi-Fi
- LoRaWAN
- NB-IoT
- 5G

The system follows an event-driven communication model.

Instead of continuously transmitting all raw sensor measurements, the edge
layer can prioritize:

- Critical events
- Risk scores
- Sensor summaries
- Node status
- Processed environmental information

This reduces communication requirements and supports operation in
low-connectivity environments.

---

## 7. Offline Operation

The system is designed to continue local operation when network connectivity
is unavailable.

### Offline Flow

    Sensor Data
         |
         v
    Local Processing
         |
         v
    Risk Assessment
         |
         v
    Local Event Storage
         |
         v
    Connectivity Restored
         |
         v
    Data Synchronization

Immediate edge processing does not depend on continuous communication with
the backend.

---

## 8. Backend

The backend provides centralized services for the monitoring network.

Responsibilities include:

- Sensor data ingestion
- Event processing
- Data storage
- Historical data management
- Risk information management
- Node status monitoring
- Dashboard APIs
- Alert management

The backend is intended for regional monitoring and long-term analysis.

---

## 9. Command Dashboard

The dashboard provides a centralized view of the deployed monitoring nodes.

### Dashboard Functions

- Node status
- Environmental measurements
- Active hazards
- Risk levels
- Risk trends
- Geographic visualization
- Event history
- Alerts and notifications

The dashboard receives processed information from the backend and presents
the current environmental state of the monitored region.

---

## 10. Risk and Event Information

Each processed sensor update can contain information such as:

    Node ID
    Node Type
    Location
    Timestamp
    Sensor Measurements
    Hazard Type
    Risk Score
    Confidence Score
    Severity
    Trend
    Event Status

Example:

    Node        : RIVER_01
    Hazard      : FLOOD
    Risk Score  : 87
    Confidence  : 92
    Severity    : CRITICAL
    Trend       : RISING
    Status      : ACTIVE

---

## 11. Prototype Hardware

The current hardware platform consists of:

| Hardware | Role |
|---|---|
| PYNQ-Z2 | Edge intelligence and processing |
| Artix-7 FPGA | Hardware acceleration |
| Environmental sensors | Field sensing |
| Communication interface | Data and event transmission |

The current development phase uses simulated sensor inputs where physical
environmental sensors are not available.

---

## 12. Project Structure

    AegisEdge/
    |
    +-- simulator/
    |   +-- sensor_node.py
    |   +-- scenarios.py
    |   +-- run_simulation.py
    |
    +-- edge/
    |
    +-- backend/
    |
    +-- dashboard/
    |
    +-- models/
    |
    +-- data/
    |
    +-- hardware/
    |   +-- pynq/
    |   +-- artix7/
    |
    +-- tests/
    |
    +-- README.md
    +-- .gitignore
    +-- pyproject.toml

---

## 13. Development Status

| Component | Status |
|---|---|
| Project structure | Completed |
| Git repository | Completed |
| Sensor node simulation | Completed |
| Environmental scenarios | Completed |
| Edge preprocessing | In progress |
| Sensor fusion | Pending |
| Multi-hazard risk engine | Pending |
| Edge AI inference | Pending |
| PYNQ-Z2 integration | Pending |
| Artix-7 acceleration | Pending |
| Backend | Pending |
| Dashboard | Pending |
| Alert system | Pending |
| End-to-end integration | Pending |

---

## 14. Development Objective

The prototype is being developed as an edge-first environmental monitoring
system in which sensing, processing and initial risk assessment are performed
close to the source of the data.

The final prototype will demonstrate the complete path from environmental
sensor data to edge-based risk assessment, event generation, centralized
visualization and FPGA-accelerated processing.