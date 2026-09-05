import sys
import os
import time

# Allow imports from the project root
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

from simulator.sensor_node import create_nodes
from simulator.scenarios import normal_conditions, hazard_conditions
from edge.risk_engine import RiskEngine


def print_result(reading, result):

    print("\n" + "=" * 72)

    print(f"NODE        : {result.node_id}")
    print(f"LOCATION    : {reading.latitude}, {reading.longitude}")
    print(f"HAZARD      : {result.hazard}")

    print(f"RISK SCORE  : {result.risk_score:.1f}%")
    print(f"CONFIDENCE  : {result.confidence:.1f}%")
    print(f"SEVERITY    : {result.severity}")
    print(f"TREND       : {result.trend}")
    print(f"STATUS      : {result.status}")
    print(f"ACTION      : {result.action}")

    if result.contributing_factors:

        print("FACTORS     :")

        for factor in result.contributing_factors:
            print(f"              - {factor}")

    print("=" * 72)


def main():

    nodes = create_nodes()
    engine = RiskEngine()

    print()
    print("=" * 72)
    print("                         AEGISEdge")
    print("                 EDGE RISK ENGINE")
    print("=" * 72)

    print()
    print("Monitoring 3 environmental sensor nodes:")
    print("  RIVER_01  -> Flood monitoring")
    print("  FOREST_01 -> Fire monitoring")
    print("  URBAN_01  -> Pollution monitoring")
    print()

    for step in range(1, 11):

        print()
        print(f"---------------- ANALYSIS CYCLE {step} ----------------")

        for node in nodes:

            # First three cycles represent normal conditions.
            if step <= 3:

                values = normal_conditions(
                    node.node_type
                )

            else:

                # Select the hazard associated with each node.
                if node.node_type == "river":
                    hazard = "flood"

                elif node.node_type == "forest":
                    hazard = "fire"

                elif node.node_type == "urban":
                    hazard = "pollution"

                else:
                    continue

                # Gradually increase hazard severity.
                hazard_step = step - 3

                values = hazard_conditions(
                    node.node_type,
                    hazard,
                    hazard_step
                )

            # Generate the sensor reading.
            reading = node.generate_reading(values)

            # Send the reading to the edge risk engine.
            result = engine.analyze(reading)

            # Display the edge decision.
            print_result(reading, result)

        time.sleep(1)


if __name__ == "__main__":
    main()