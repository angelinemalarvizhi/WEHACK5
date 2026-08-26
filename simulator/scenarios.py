import random


def normal_conditions(node_type):

    if node_type == "river":
        return {
            "temperature": random.uniform(28, 33),
            "humidity": random.uniform(70, 90),
            "rainfall": random.uniform(0, 10),
            "water_level": random.uniform(30, 55),
            "soil_moisture": random.uniform(45, 70),
            "smoke": 0,
            "pm25": random.uniform(15, 40),
            "pm10": random.uniform(25, 60),
            "gas": random.uniform(0, 10),
            "vibration": random.uniform(5, 15)
        }

    if node_type == "forest":
        return {
            "temperature": random.uniform(27, 34),
            "humidity": random.uniform(55, 85),
            "rainfall": random.uniform(0, 8),
            "water_level": 0,
            "soil_moisture": random.uniform(35, 65),
            "smoke": random.uniform(0, 5),
            "pm25": random.uniform(10, 30),
            "pm10": random.uniform(20, 50),
            "gas": random.uniform(0, 8),
            "vibration": random.uniform(2, 12)
        }

    return {
        "temperature": random.uniform(28, 35),
        "humidity": random.uniform(50, 80),
        "rainfall": random.uniform(0, 5),
        "water_level": 0,
        "soil_moisture": random.uniform(20, 50),
        "smoke": random.uniform(0, 3),
        "pm25": random.uniform(20, 60),
        "pm10": random.uniform(30, 90),
        "gas": random.uniform(5, 20),
        "vibration": random.uniform(2, 10)
    }


def hazard_conditions(node_type, hazard, step):

    values = normal_conditions(node_type)

    if hazard == "flood" and node_type == "river":

        values["rainfall"] = 40 + step * 5
        values["water_level"] = 55 + step * 7
        values["soil_moisture"] = 70 + step * 4
        values["humidity"] = 85 + step

    elif hazard == "fire" and node_type == "forest":

        values["temperature"] = 32 + step * 2
        values["humidity"] = max(20, 60 - step * 5)
        values["smoke"] = 10 + step * 12
        values["gas"] = 10 + step * 7

    elif hazard == "pollution" and node_type == "urban":

        values["pm25"] = 50 + step * 20
        values["pm10"] = 80 + step * 25
        values["gas"] = 20 + step * 8
        values["temperature"] += step * 0.5

    return values