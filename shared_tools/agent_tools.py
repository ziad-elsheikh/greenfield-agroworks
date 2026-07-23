from langchain_core.tools import Tool
from shared_tools.irrigation_api import (
    get_soil_moisture, 
    get_weather_forecast, 
    get_crop_and_soil_data, 
    irrigate_wrapper, 
    suspend_irrigation_wrapper
)

get_soil_moisture_tool = Tool(
    name="get_soil_moisture",
    func=get_soil_moisture,
    description="Useful for finding the current soil moisture percentage and critical threshold. Input should be the zone_id (integer). Always use this FIRST to check if the soil is actually dry."
)

get_weather_forecast_tool = Tool(
    name="get_weather_forecast",
    func=get_weather_forecast,
    description="Useful for checking rain predictions. Input should be the zone_id (integer). Use this AFTER checking moisture, to see if natural rain will solve the dryness."
)

get_crop_and_soil_data_tool = Tool(
    name="get_crop_and_soil_data",
    func=get_crop_and_soil_data,
    description="Useful for finding the crop type and its drought tolerance. Input should be the zone_id (integer). Use this to understand if the crop can survive waiting for the rain."
)

irrigate_tool = Tool(
    name="irrigate",
    func=irrigate_wrapper,
    description="ACTION TOOL. Use this to open the water valves and irrigate the zone. Input should be a comma-separated string containing zone_id and duration_minutes (e.g., '5, 60')."
)

suspend_irrigation_tool = Tool(
    name="suspend_irrigation",
    func=suspend_irrigation_wrapper,
    description="ACTION TOOL. Use this to delay irrigation if rain is coming and the crop can survive. Input should be a comma-separated string containing zone_id and delay_hours (e.g., '5, 2')."
)

