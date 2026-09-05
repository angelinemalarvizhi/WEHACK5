import sys
import os
import time

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

from simulator.sensor_node import create_nodes
from simulator.scenarios import normal_conditions, hazard_conditions
from edge.risk_engine import RiskEngine


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    nodes = create_nodes()
    engine = RiskEngine()

    cycle = 0

    print("=" * 72)
    print("                         AEGISEdge")
    print("              ENVIRONMENTAL INTELLIGENCE")
    print("=" * 72)

    print("\nEdge monitoring started.")
    print("Press Ctrl+C to stop.\n")

    try:

        while True:

            cycle += 1

            # Repeat the scenario every 10 cycles.
            scenario_step = ((cycle - 1) % 10) + 1

            print("\n" + "=" * 72)
            print(f"MONITORING CYCLE : {cycle}")
            print("=" * 72)

            for node in nodes:

                if scenario_step <= 3:

                    values = normal_conditions(
                        node.node_type
                    )

                else:

                    if node.node_type == "river":
                        hazard = "flood"

                    elif node.node_type == "forest":
                        hazard = "fire"

                    elif node.node_type == "urban":
                        hazard = "pollution"

                    else:
                        continue

                    hazard_step = scenario_step - 3

                    values = hazard_conditions(
                        node.node_type,
                        hazard,
                        hazard_step
                    )

                reading = node.generate_reading(values)

                result = engine.analyze(reading)

                print(
                    f"\n{result.node_id:<12} "
                    f"{result.hazard:<15} "
                    f"Risk: {result.risk_score:>6.1f}%  "
                    f"{result.severity:<8} "
                    f"{result.trend:<8}"
                )

                if result.status == "ACTIVE":

                    print(
                        f"  ALERT → {result.action}"
                    )

                elif result.status == "MONITOR":

                    print(
                        f"  WARNING → {result.action}"
                    )

                else:

                    print(
                        "  STATUS → Normal monitoring"
                    )

            time.sleep(2)

    except KeyboardInterrupt:

        print("\n\nMonitoring stopped.")

        print("=" * 72)


if __name__ == "__main__":
    main()