import asyncio
from typing import Any
from agents import Agent, Runner, function_tool, AgentHooks, RunContextWrapper, Tool, ModelSettings
from configration import config

class HooksClass(AgentHooks):
    async def on_start(self, context: RunContextWrapper, agent: Agent):  
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent."""
        print('Starting agent')

    async def on_end(self, context: RunContextWrapper, output: Any, agent: Agent):  
        """Called when the agent produces a final output."""
        print('Ending agent')

    async def on_tool_start(self, context:RunContextWrapper, agent: Agent, tool:Tool):
        """Called concurrently with tool invocation."""
        print('Starting tool')
    
    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result:str):
        """Called after a tool is invoked."""
        print('Ending tool')

    # async def on_handoff(self, context:RunContextWrapper, agent: Agent, source: Agent):
    #     """"""
    #     print('Handoffs agent')

@function_tool
async def get_weather(city: str)->str:
    return f'The current weather in {city} is 24°C'

billling_agent=Agent(
    name='Billing Agent',
    instructions="""You are a billing agent.
        Your tasks is solve the billing related queries
    """
)
async def main():
    agent = Agent(
        name='Assistant',
        instructions='You are a helpful assistant',
        tools=[get_weather],
        hooks=HooksClass(),
        # handoffs=[billling_agent],
        model_settings=ModelSettings(max_tokens=50)
    )
    result = await Runner.run(agent, 'What is the weather in Karachi?', run_config=config)
    print(result.final_output)

if __name__ == '__main__':
    asyncio.run(main())



# import asyncio
# from agents import Agent, Runner, AgentHooks, RunContextWrapper
# from configration import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     name: str
#     start_word: str
#     end_word: str


# class HooksClass(AgentHooks):
#     async def on_start(self, context: RunContextWrapper[UserInfo], agent: Agent):  
#         print(f"[HOOK] Starting agent: {agent.name} for user: {context.context.start_word} {context.context.name} bhai")

#     async def on_end(self, context: RunContextWrapper[UserInfo], agent: Agent, output: str):  
#         print(f"[HOOK] Ending agent: {agent.name} for user: {context.context.name} bhi {context.context.end_word}")
    
# async def main():
#     user=UserInfo(name='Waqas', start_word='Assalam-o-alaikum', end_word='Allah hafiz')
#     my_hook = HooksClass()

#     agent = Agent[UserInfo](
#         name='Customer Support Agent',
#         instructions='You are a customer support agent',
#         hooks=my_hook
#     )
#     result = await Runner.run(starting_agent=agent, input='Hello',context=user, run_config=config)
#     print('Final output: ',result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())

# import asyncio
# from agents import Agent, Runner, AgentHooks, RunContextWrapper
# from configration import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     name: str

# class HooksClass(AgentHooks):
#     async def on_start(self, context: RunContextWrapper[UserInfo], agent: Agent):  
#         user = context.context.name
#         print('Hi' ,user)

# #     async def on_end(self, context: RunContextWrapper[UserInfo], agent: Agent, output: str):  
# #         print(f"[HOOK] Ending agent: {agent.name} for user: {context.context.name} bhi {context.context.end_word}")
    
# async def main():
#     user=UserInfo(name='Waqas')
#     my_hook = HooksClass()

#     agent = Agent[UserInfo](
#         name='Customer Support Agent',
#         instructions='You are a customer support agent',
#         hooks=my_hook
#     )
#     result = await Runner.run(starting_agent=agent, input='Hello',context=user, run_config=config)
#     print('Final output: ',result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, AgentHooks, RunContextWrapper
# from configration import config
# from dataclasses import dataclass

# shoping_list = {}

# @dataclass
# class UserInfo:
#     name: str

# class HooksClass(AgentHooks):
#     async def on_start(self, context: RunContextWrapper[UserInfo], agent: Agent):  
#         user = context.context.name
#         print('User :',user)
        
# async def main():

#     user = UserInfo(name='Muhammad Waqas')
#     shoping_list[user.name] ='You bought 1pcs white suite' 
    
#     agent = Agent[UserInfo](
#         name='Customer Support Agent',
#         instructions='You are a customer support agent',
#         hooks=HooksClass()
#     )
#     result = await Runner.run(starting_agent=agent, input='Hello',context=user, run_config=config)
#     print('Shoping List: ',shoping_list)
#     print('Final output: ',result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())



# import asyncio
# from agents import Agent, Runner, RunContextWrapper, ModelSettings, AgentHooks
# from configration import config

# shopping_history = {}

# class ShoppingAgentHooks(AgentHooks):
#     async def on_start(self, context: RunContextWrapper[dict], agent: Agent):

#         user = context.context.get('name')
#         shopping_history[user]=''
#         print(f"[on_start] Shopping session started for {user}")

# async def main():
#     agent = Agent(
#         name="ShoppingBot",
#         instructions="You are a shopping assistant. Track purchases.",
#         model_settings=ModelSettings(max_tokens=50),
#         hooks=ShoppingAgentHooks()   # add hooks here
#     )

#     # Context (user info)
#     user_context ={
#         "name": "Ali",
#         "name":"Waqas"}

#     # Run
#     for users in user_context:
#         result = await Runner.run(
#             starting_agent=agent,
#             input=f"{users} you bought milk and eggs",
#             context=user_context,
#             run_config=config
#     )

#     print("Final Output:", result.final_output)
#     print("DB State:", shopping_history)

# if __name__ == "__main__":
#     asyncio.run(main())


# import os
# import asyncio
# from dotenv import load_dotenv
# from pydantic import BaseModel
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, run_demo_loop

# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     time: str
#     participants: list[str]

# agent = Agent(
#     name="Calendar extractor",
#     instructions="Extract calendar events from the given text and return them in structured format.",
#     output_type=CalendarEvent,
#     model=model
# )

# async def main():
#     await run_demo_loop(agent)

# if __name__ == "__main__":
#     asyncio.run(main())

# #  Meeting with Ali and Sara on 5th September 2:30PM about Project Launch.



#SESSION

# import asyncio
# from agents import Agent, Runner, SQLiteSession
# from configration import config

# async def main():
#     agent = Agent(
#         name="Assistant",
#         instructions="Reply very concisely.")

#     session = SQLiteSession(session_id=123)
#     session2 = SQLiteSession(session_id=456)

#     result1 = await Runner.run(agent, "My name is Muhammad Waqas.",session=session, run_config=config)
#     print(f"Assistant: {result1.final_output}")
#     result2 = await Runner.run(agent, "What was my name?", session=session, run_config=config)
#     print(f"Assistant: {result2.final_output}")
    
#     result3 = await Runner.run(agent, "My name is Muhammad Ali.",session=session2, run_config=config)
#     print(f"Assistant: {result3.final_output}")
#     result4 = await Runner.run(agent, "What was my name?", session=session2, run_config=config)
#     print(f"Assistant: {result4.final_output}")

# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# from agents import Agent, Runner, SQLiteSession
# from configration import config

# async def main():
#     agent = Agent(
#         name="Assistant",
#         instructions="Reply very concisely.",
#     )

#     # session = SQLiteSession("conversation_123", "conversation_history.db")
#     session = SQLiteSession(session_id=12345)

#     print("The agent will remember previous messages automatically.\n")


#     result = await Runner.run(agent, "What city is the Golden Gate Bridge in?", session=session,run_config=config)
#     print(f"Assistant: {result.final_output}")

# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# from agents import Agent, Runner, SQLiteSession
# from configration import config

# async def main():
#     agent = Agent(
#         name="PizzaBot",
#         instructions="You are a pizza ordering assistant. Remember user orders and help them manage."
#     )
#     session=SQLiteSession('pizza_user','pizza_order.db')

#     await session.add_items([
#         {'role':'user','content':'Mujhe ek large Pepperoni Pizza chahiye.'},
#         {'role':'assistant','content':'Ok, Aap ek order me ek large Pepperoni Pizza add kr diya gaya.'}
#     ])
    
#     items = await session.get_items()
#     for msg in items:
#         print(f'{msg["role"]},{msg["content"]}')

#     # await session.clear_session()
#     # empty = await session.get_items()
#     # print("Current memory:", empty)
    
#     result = await Runner.run(agent, "Meri current order list batao.", session=session,run_config=config)
#     print(f"Assistant: {result.final_output}")

# if __name__ == '__main__':
#     asyncio.run(main())


# RESULTS

# import asyncio
# from agents import Agent, Runner, function_tool
# from configration import config

# @function_tool(is_enabled=True)
# async def add(a:int, b:int):
#     return a+b

# async def main():
#     agent = Agent(
#         name="Assistant",
#         instructions="You are a helpful assistant.",
#         tools=[add]
#     )

#     result = await Runner.run(agent, 'What is the sum of 2+5', run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())

# REPL
import os
import asyncio
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, run_demo_loop

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

agent = Agent(
    name="Assistant",
    instructions="You are ahelpful assistant.",
    model=model
)

async def main():
    await run_demo_loop(agent)

if __name__ == "__main__":
    asyncio.run(main())