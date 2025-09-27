# import asyncio
# from typing import Any
# from agents import Agent, Runner, RunHooks, RunContextWrapper, Tool, ModelSettings, function_tool
# from configration import config

# class HooksClass(RunHooks):
#     async def on_agent_start(self, context: RunContextWrapper, agent: Agent):  
#         """Called before the agent is invoked. Called each time the running agent is changed to this
#         agent."""
#         print('Starting agent')

#     async def on_agent_end(self, context:RunContextWrapper, agent: Agent, output:str):
#         """Called when the agent produces a final output."""
#         print('Ending agent')
    
#     async def on_tool_start(self, context:RunContextWrapper, agent:Agent, tool: Tool):
#         """"""
#         print('Starting tool')
    
#     async def on_tool_end(self, context:RunContextWrapper, agent:Agent, tool:Tool, result:Any):
#         """"""
#         print('Ending tool')

# @function_tool
# async def math_tool(num1, num2):
#     return num1+num2 or num1-num2

# async def main():
#     agent = Agent(
#         name='Assistant',
#         instructions='You are a helpful assistant',
#         model_settings=ModelSettings(max_tokens=50),
#         tools=[math_tool]
#     )
#     result = await Runner.run(starting_agent=agent, input='Subtract of 10-4?', run_config=config,hooks=HooksClass())
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())


import asyncio
from agents import Agent, Runner, ModelSettings, function_tool
from configration import config


@function_tool
async def customer_udhaar(city):
    return f'The weather in {city} is 30C'
    # customers_name=[{'id':101, 'name':'Waqas', 'balance': 540},{'id':102, 'name':'Fahham', 'balance': 270}]
    # return f'Your current Udhaar balance is {customers_name}.'

async def main():
    agent = Agent(
        name='ShopKeeper Agent',
        instructions='You are a helpful shopkeeper agent',
        tools=[customer_udhaar]
    )
    result = await Runner.run(agent, 'What is the weather in Karachi?', run_config=config)
    print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())