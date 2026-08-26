from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class SensorReading:
    node_id: str
    node_type: str
    latitude: float
    longitude: float

    temperature: float
    humidity: float
    rainfall: float
    water_level: float
    soil_moisture: float

    smoke: float
    pm25: float
    pm10: float
    gas: float
    vibration: float

    timestamp: str

    def to_dict(self):
        return asdict(self)


class SensorNode:

    def __init__(self, node_id, node_type, latitude, longitude):
        self.node_id = node_id
        self.node_type = node_type
        self.latitude = latitude
        self.longitude = longitude

    def generate_reading(self, values):

        return SensorReading(
            node_id=self.node_id,
            node_type=self.node_type,
            latitude=self.latitude,
            longitude=self.longitude,

            temperature=round(values["temperature"], 2),
            humidity=round(values["humidity"], 2),
            rainfall=round(values["rainfall"], 2),
            water_level=round(values["water_level"], 2),
            soil_moisture=round(values["soil_moisture"], 2),

            smoke=round(values["smoke"], 2),
            pm25=round(values["pm25"], 2),
            pm10=round(values["pm10"], 2),
            gas=round(values["gas"], 2),
            vibration=round(values["vibration"], 2),

            timestamp=datetime.now().isoformat()
        )


def create_nodes():

    return [
        SensorNode(
            "RIVER_01",
            "river",
            13.0827,
            80.2707
        ),

        SensorNode(
            "FOREST_01",
            "forest",
            11.4102,
            76.6950
        ),

        SensorNode(
            "URBAN_01",
            "urban",
            13.0674,
            80.2376
        )
    ]