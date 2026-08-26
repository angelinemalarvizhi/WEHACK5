import time
import json

from sensor_node import create_nodes
from scenarios import normal_conditions, hazard_conditions


def print_reading(reading):

    print("\n" + "=" * 60)
    print(f"NODE       : {reading.node_id}")
    print(f"TYPE       : {reading.node_type.upper()}")
    print(f"TIME       : {reading.timestamp}")
    print("-" * 60)

    print(f"Temperature : {reading.temperature:.2f} °C")
    print(f"Humidity    : {reading.humidity:.2f} %")
    print(f"Rainfall    : {reading.rainfall:.2f} mm")
    print(f"Water Level : {reading.water_level:.2f} %")
    print(f"Soil Moist. : {reading.soil_moisture:.2f} %")
    print(f"Smoke       : {reading.smoke:.2f}")
    print(f"PM2.5       : {reading.pm25:.2f}")
    print(f"PM10        : {reading.pm10:.2f}")
    print(f"Gas         : {reading.gas:.2f}")
    print(f"Vibration   : {reading.vibration:.2f}")

    print("=" * 60)


def main():

    nodes = create_nodes()

    print("\n")
    print("=" * 60)
    print("              AEGISEdge")
    print("       ENVIRONMENTAL SENSOR NETWORK")
    print("=" * 60)

    print("\nActive Nodes:")

    for node in nodes:
        print(f"  {node.node_id} | {node.node_type}")

    print("\nSimulation started...\n")

    step = 0

    while True:

        for node in nodes:

            if step < 5:

                values = normal_conditions(node.node_type)
                mode = "NORMAL"

            else:

                if node.node_type == "river":
                    hazard = "flood"

                elif node.node_type == "forest":
                    hazard = "fire"

                else:
                    hazard = "pollution"

                values = hazard_conditions(
                    node.node_type,
                    hazard,
                    min(step - 4, 8)
                )

                mode = hazard.upper()

            reading = node.generate_reading(values)

            print(f"\n[{mode}]")

            print_reading(reading)

            print(
                json.dumps(
                    reading.to_dict(),
                    separators=(",", ":")
                )
            )

        step += 1

        time.sleep(2)


if __name__ == "__main__":
    main()