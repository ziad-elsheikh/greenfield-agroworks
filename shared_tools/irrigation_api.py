# The Scenarios
#
# Zone 1:
#   Soil:               dry.
#   Rain:               no rains for the next 24 hours.
#   Crop tolerance:     (corn) 4 hours.
#   Correct Decision:   Irrigate immediately.
# Zone 2:
#   Soil:               dry.
#   Rain:               heavy rain is forecasted in 2 hours.
#   Crop tolerance:     (corn) 4 hours.
#   Correct Decision:   Suspend irrigation and wait for rain.
# Zone 3:
#   Soil:               wet.
#   Rain:               no rain.
#   Crop tolerance:     (corn) 4 hours.
#   Correct Decision:   Do nothing.
# Zone 4:
#   Soil:               dry.
#   Rain:               rain is forecasted in 4 hours.
#   Crop tolerance:     (strawberries) 1 hour.
#   Correct Decision:   Do nothing.

# Fake Sensors
def get_soil_moisture(zone_id: int) -> dict:

    zone_id = int(zone_id)

    # Zones 1, 2, and 4 are dry
    if zone_id in [1, 2, 4]:
        return {"zone": zone_id, "moisture_percent": 10, "critical_threshold": 30}
    return {"zone": zone_id, "moisture_percent": 45, "critical_threshold": 30}

def get_weather_forecast(zone_id: int) -> dict:

    zone_id = int(zone_id)

    if zone_id == 2:
        return {"zone": zone_id, "rain_probability": 85, "hours_until_rain": 2}
    elif zone_id == 4:
        # Zone 4: Rain is far away (4 hours)
        return {"zone": zone_id, "rain_probability": 90, "hours_until_rain": 4}
    return {"zone": zone_id, "rain_probability": 10, "hours_until_rain": 24}

def get_crop_and_soil_data(zone_id: int) -> dict:

    zone_id = int(zone_id)

    if zone_id == 4:
        # Fragile crop
        return {"zone": zone_id, "crop_type": "Strawberries", "soil_type": "Sandy", "drought_tolerance_hours": 1}
    # Tough crop
    return {"zone": zone_id, "crop_type": "Corn", "soil_type": "Clay", "drought_tolerance_hours": 4}


# Actions
def irrigate(zone_id: int, duration_minutes: int) -> dict:
    return {"status": "SUCCESS", "message": f"Valves OPENED in Zone {zone_id} for {duration_minutes} mins."}

def suspend_irrigation(zone_id: int, delay_hours: int) -> dict:
    return {"status": "SUCCESS", "message": f"Irrigation SUSPENDED in Zone {zone_id}. Re-check in {delay_hours} hours."}


def irrigate_wrapper(input_str: str) -> str:
    try:
        # بنفصل النص من عند الفاصلة
        zone_str, duration_str = input_str.split(",")
        # بننضف المسافات وبنحولهم لأرقام صحيحة
        zone_id = int(zone_str.strip())
        duration = int(duration_str.strip())
        # بننادي الدالة الأصلية بالمتغيرات الصح
        return irrigate(zone_id=zone_id, duration_minutes=duration)
    except ValueError:
        return f"Error: Invalid input format. Expected 'zone_id, duration_minutes' (e.g., '5, 60'). You provided: '{input_str}'"

def suspend_irrigation_wrapper(input_str: str) -> str:
    try:
        zone_str, delay_str = input_str.split(",")
        zone_id = int(zone_str.strip())
        delay = int(delay_str.strip())
        return suspend_irrigation(zone_id=zone_id, delay_hours=delay)
    except ValueError:

        return f"Error: Invalid input format. Expected 'zone_id, delay_hours' (e.g., '5, 2'). You provided: '{input_str}'"

        return f"Error: Invalid input format. Expected 'zone_id, delay_hours' (e.g., '5, 2'). You provided: '{input_str}'"

