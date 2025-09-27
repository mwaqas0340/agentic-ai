import asyncio
from agents import Agent, Runner, function_tool
from agents.agent import StopAtTools
from configration import config

# @function_tool
# async def get_weather(city):
#     return f'The weather in {city} is 30C'

# @function_tool
# async def get_math(a:int, b:int):
#     return a+b

# async def main():
#     agent = Agent(
#         name='Weather Assistany',
#         instructions='You are a helpful weather Assistant',
#         tools=[get_weather,get_math],
#         tool_use_behavior=StopAtTools(stop_at_tool_names=['get_weather']) # yaha sirf get_weather tools ka final out LLM ko dobara nhi gai ga foran UI pr show hoga baki tools ka gai ga
#     )

#     result = await Runner.run(agent, 'Sum of 3 and 34', run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool
# from configration import config

# @function_tool
# async def get_weather(city):
#     return f'The weather in {city} is 30C'

# @function_tool
# async def get_math(a:int, b:int):
#     return a+b

# agent = Agent(
#     name='Weather Assistany',
#     instructions='You are a helpful weather Assistant',
#     tools=[get_weather, get_math],
#     tool_use_behavior='stop_on_first_tool' # yaha sare tools ka final out LLM ko dobara nhi gai ga foran UI pr show hoga 
# )

# async def main():     
#     result = await Runner.run(agent, 'What is the weather in Karachi?', run_config=config, max_turns=2)
#     print(result.final_output)
# if __name__ == '__main__':
#     asyncio.run(main())

