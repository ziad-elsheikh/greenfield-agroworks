import sys
import os

# doing all this for adding our fake sensor reads to the system path
sys.path.append( # add this path to system path
    os.path.dirname( # back another step to get the project dir
        os.path.dirname( # back one step to get the current dir
            os.path.abspath(__file__) # __file__ means the current file path 
        )
    )
)

from shared_tools.irrigation_api import get_soil_moisture, irrigate


def run_reactive_agent(zone_id: int):
    print(f"\n=== Running Reactive Agent for Zone {zone_id} ===")
    
    # extract data from sensors
    moisture_data = get_soil_moisture(zone_id)
    current_moisture = moisture_data["moisture_percent"]
    threshold = moisture_data["critical_threshold"]

    # Rules execution
    if current_moisture < threshold:
        print(f"[LOG] Soil moisture is {current_moisture}% (below {threshold}%).")
        print(f"[ACTION] Irrigation....")

        # hard coded action
        res = irrigate(zone_id, duration_minutes=60)
        print(f"[RESULT] {res["message"]}")
    else:
        print(f"[LOG] Soil moisture is {current_moisture}% (Above {threshold}%).")
        print("[ACTION] No irrigation needed.")


if __name__ == "__main__":
    # Zone 1: dry and no rain
    run_reactive_agent(1)
    
    # Zone 2: dry but rain is coming
    run_reactive_agent(2)
    
    # Zone 3: wet
    run_reactive_agent(3)

    # Zone 4: dry
    run_reactive_agent(4)