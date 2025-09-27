
# import asyncio
# from agents import Agent, Runner
# from configration import config

# billing_agent = Agent(
#     name='Billing Agent',
#     instructions='You are a billing agent. Your tasks is to solve the billing related queries.',

# )
# refund_agent = billing_agent.clone(
#     name='Refund Agent',
#     instructions='You are a refund agent. Your tasks is to solve the refund related queries.'
# )

# async def main():
#     result = await Runner.run(refund_agent, 'Your product is broken. I want to refund.', run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())



import asyncio
from agents import Agent, Runner, function_tool
from configration import config

@function_tool
async def weather(city):
    return f'The weather in {city} is 30C'

@function_tool
async def math(a, b):
    return a+b

billing_agent = Agent(
    name='Billing Agent',
    instructions='You are a billing agent. Your tasks is to solve the billing related queries.',
    tools=[weather, math]
)

refund_agent = billing_agent.clone(
    name='Refund Agent',
    instructions='You are a refund agent. Your tasks is to solve the refund related queries.',
)

async def main():
    result = await Runner.run(refund_agent, 'What is the sum of 2+3?', run_config=config)
    print(result.last_agent.clone)
    print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())
