import asyncio
from agents import Agent, Runner, RunContextWrapper
from configration import config
from dataclasses import dataclass
from DB import db_connection

@dataclass
class GroceryClass:
    name: str
    home_things:list

customer_list = db_connection

async def dynamic_instructions(context: RunContextWrapper[GroceryClass], agent: Agent)->str:
    return f'{context.context.name} bhai you grocery list is {context.context.home_things}.'

async def main():
    shop = GroceryClass(name='Waqas', home_things = customer_list)
    
    agent = Agent[GroceryClass](
        name='Assistant',
        instructions=dynamic_instructions,
    )
    result = await Runner.run(starting_agent=agent, input='Give me 2kg sugar, 1kg meznan, 3kg rice and 1litre oil. Calculate toltal bill ', context=shop, run_config=config)
    print(result.final_output)
    
if __name__ == '__main__':
    asyncio.run(main())