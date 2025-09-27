
from agents import Agent, Runner, function_tool, set_trace_processors, RunContextWrapper
from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor
from configration import config

# exporter=ConsoleSpanExporter()
# processor=BatchTraceProcessor(exporter)
# set_trace_processors([processor])

# @function_tool(
#         name_override='WeatherInfo', # custom tool name
#         description_override='Get the latest weather updates for any city') # custom description 

# def get_weather(city):
#     """This function returns the weather for a given city."""
#     return f'The current weather in {city} is 30°C'

# agent=Agent(
#     name='Weather Agent',
#     instructions = 'You are a weather agent',
#     tools=[get_weather]
# )
# print('Custom tool name: ',get_weather.name)
# print('Custom tool description: ',get_weather.description)
# print('is_enable: ',get_weather.is_enabled)

# result = Runner.run_sync(agent, 'What is the weather in Karachi?', run_config=config)
# print(result.final_output)


# failure_error_function

# def weather_failure_handler(error: Exception, tool_call: None)-> str:
#     return f'⚠️ Weather service is currently unavailable. Error {error}'

# @function_tool(failure_error_function=weather_failure_handler) # Custom error handler added

# def get_weather(city):
#     """This function returns the weather for a given city."""

#     if city.lower() == 'karachi':
#         raise Exception("API Timeout while fetching karachi weather")
    
#     return f'The current weather in {city} is 30C'

# agent=Agent(
#     name='Weather Agent',
#     instructions = 'You are a weather agent',
#     tools=[get_weather]
# )

# # Run 1: Karachi (error case)
# result = Runner.run_sync(agent, 'What is the weather in karachi?', run_config=config)
# print(result.final_output)

# # # Run 2: Lahore (success case)
# # result = Runner.run_sync(agent, 'What is the weather in Lahore?', run_config=config)
# # print(result.final_output)


# strict_mode 

# @function_tool(strict_mode=True) #Strict mode enabled
# @function_tool(strict_mode=False) #Strict mode disabled
# def get_weather(city):
#     """This function returns the weather for a given city."""
#     return f'The current weather in {city} is 30C'

# agent=Agent(
#     name='Weather Agent',
#     instructions = 'You are a weather agent',
#     tools=[get_weather]
# )

# try:
#     # result = Runner.run_sync(agent, 'What is the weather in Lahore with humidity?', run_config=config)
#     result = Runner.run_sync(agent, 'What is the weather in Lahore?', run_config=config)
#     print(result.final_output)
# except Exception as e:
#     print('strict mode.' ,e)


#is_enabled

# @function_tool(is_enabled= True) # Tool enable
# # @function_tool(is_enabled= False) # Tool disabled

# def get_weather(city):
#     """This function returns the weather for a given city."""
#     return f'The current weather in {city} is 30C'

# agent=Agent(
#     name='Weather Agent',
#     instructions = 'You are a weather agent',
#     tools=[get_weather]
# )

# result = Runner.run_sync(agent, 'What is the weather in Karachi?', run_config=config)
# print(result.final_output)

