# DYNAMIC INSTRUCTIONS

# from agents import Agent, Runner, RunContextWrapper, ModelSettings
# from configration import config

# async def dynamic_instructions(cxt: RunContextWrapper, starting_agent: Agent)->str:
#     print('[CONTEXT]:', cxt.context)
#     return 'You are a helpful assistant that can answer the questions and help with tasks.'

# agent = Agent(
#     name='Assistant',
#     instructions=dynamic_instructions,
#     model_settings=ModelSettings(max_tokens=50),
# )
# result = Runner.run_sync(agent, 'Hello', context=['Waqas', 12345], run_config=config)
# print(result.final_output)
    

# from agents import Agent, Runner, RunContextWrapper, ModelSettings
# from configration import config

# class UserInfo():
#     name:str
#     uid:int

#     def __init__(self, name, uid):
#         self.name= name
#         self.uid= uid

# user_data = UserInfo(
#     name='Waqas',
#     uid=12345
# )

# async def dynamic_instructions(cxt: RunContextWrapper[UserInfo], agent: Agent)->str:
#     return f'The user {cxt.context.name} is 23 years old'

# agent = Agent(
#     name='Assistant',
#     instructions=dynamic_instructions,
#     model_settings=ModelSettings(max_tokens=50),
# )
# result = Runner.run_sync(agent, 'What is the name and age of the user?', context=user_data, run_config=config)
# print(result.final_output)

# import asyncio
# from agents import Agent, Runner, RunContextWrapper, ModelSettings
# from configration import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     name:str
#     role: str

# async def dynamic_instructions(context: RunContextWrapper[UserInfo], agent: Agent)->str:
#     return f'My name is {context.context.name} and my occupation {context.context.role}'

# async def main():
#     user = UserInfo(name='Muhammad Waqas', role='Software Developer')
    
#     agent = Agent[UserInfo](
#         name='Assistant',
#         instructions=dynamic_instructions,
#         model_settings=ModelSettings(max_tokens=50),
#     )
#     result = await Runner.run(starting_agent=agent, input='Tell me about yourself', context=user, run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, RunContextWrapper, ModelSettings
# from configration import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     id: int
#     name: str
#     role: str

# users = {
#     1: UserInfo(id=1, name="Muhammad Waqas", role="Software Developer"),
#     2: UserInfo(id=2, name="Ali Khan", role="Doctor"),
#     3: UserInfo(id=3, name="Sara Ahmed", role="Teacher"),
# }

# async def dynamic_instrctions(context: RunContextWrapper[UserInfo], agent: Agent)-> str:
#     return f"""
#         "You are {context.context.name}, a {context.context.role}."
#         "Always speak as if you are introducing yourself."
#         """
    
# async def main():
#     user = users[3]
    
#     agent = Agent[UserInfo](
#         name='Assistant',
#         instructions=dynamic_instrctions,
#         model_settings=ModelSettings(max_tokens=100),
#     )
#     result = await Runner.run(starting_agent=agent, input='Introduce yourself', context=user, run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
from configration import config
from agents import Agent, Runner, RunContextWrapper
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int 

users = UserData(name='Waqas', age=23)

def dynamic_instructions(ctx: RunContextWrapper[UserData], agent: Agent):
    return f"Hi {ctx.context.name} you are {ctx.context.age} years old."
        
async def main():

    agent = Agent[UserData](
        name='Assistant',
        instructions=dynamic_instructions
    )
    result = await Runner.run(starting_agent=agent, input='What is the name and age of the user?', context=user, run_config=config)
    print(result.final_output)
    
if __name__ == '__main__':
    asyncio.run(main())




# CONTEXT MANAGEMENT

# from configration import config
# from agents import Agent, Runner, function_tool, RunContextWrapper, ModelSettings
# from dataclasses import dataclass

# @dataclass
# class UderData:
#     name:str
#     balance: float
#     id: int

# @function_tool
# def get_udhaar(ctx: RunContextWrapper[UderData]):
#     return f'{ctx.context.name} bhai aap ka baki udhaar {ctx.context.balance} rupay hai '   

# customer_data = UderData(name='Faham', balance=570, id=101)

# customer_support= Agent[UderData](
#     name='Udhaar Assistant',
#     instructions="""
#     Aap ek polite aur madadgar udhaar assistant hain.
#     Jab bhi koi user apna balance pooche, unhe naam se bula kar batayein.
#     Agar koi tool call kare to uska output theek se explain karein.
#     """,
#     tools=[get_udhaar],
#     model_settings=ModelSettings(temperature=0.1,tool_choice='auto')
# )
# result = Runner.run_sync(
#     starting_agent=customer_support,
#     input='Mera udhaar kitna hai?',
#     context=customer_data,
#     run_config=config
# )
# print(result.final_output)


# @dataclass
# class UderData:
#     name:str
#     id: int

# @function_tool
# def get_user_data(ctx: RunContextWrapper[UderData]):
#     return f'{ctx.context.name} is 23 years old. '   

# async def main():
#     customer_data = UderData(name='Waqas', id=12345)

#     customer_support= Agent[UderData](
#         name='Customer Support',
#         instructions="""
#             You are acustomer supprt agent.
#             If user ask any name and then you will response. 
#         """,
#         tools=[get_user_data],
#         model_settings=ModelSettings(temperature=0.1,tool_choice='auto')
#     )
#     result = await Runner.run(starting_agent=customer_support,input='What is the age of the user?',context=customer_data,run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())



# import asyncio
# from dataclasses import dataclass
# from agents import Agent, Runner, ModelSettings, function_tool, RunContextWrapper
# from configration import config

# # 👤 Local Context: User Data (NOT visible to LLM)
# @dataclass
# class UderData:
#     name: str
#     customer_id: int
#     balance: float  # current udhaar

# # ▶️ Run the agent with both contexts
# customer_data = UderData(
#     name="Waqas",
#     customer_id=786,
#     balance=520.0
# )
# if customer_data.balance >= 1000:
#     print('Aap ka udhaar band hai Q ke aap is waqat 1000 hazar ki udhaar utha chuke hain', customer_data.balance)
# else:
#     print('Aap filhal udhaar lai sakte hain')

# # 🧰 Tool: Access udhaar balance via local context
# @function_tool
# def get_udhaar_balance(ctx: RunContextWrapper[UderData]) -> str:
#     """Fetch the name, id and udhaar of the user. Call this function to get user's name, id and udhaar information."""
#     return f"{ctx.context.name}, aap ka udhaar baqi hai Rs. {ctx.context.balance}"

# # 🤖 Agent: Friendly LLM behavior (LLM Context)
# customer_support = Agent[UderData](
#     name="Udhaar Assistant",
#     tools=[get_udhaar_balance],
#     model_settings=ModelSettings(
#         temperature=0.4,
#         tool_choice="auto"
#     )
# )

# result = Runner.run_sync(
#     starting_agent=customer_support,
#     input="Mera udhaar kitna baqi hai?",
#     context=customer_data,
#     run_config=config
# )
# print(result.final_output)



# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper, ModelSettings
# from configration import config
# from pydantic import BaseModel

# class personalInfo(BaseModel):
#     name: str
#     id: int

# @function_tool
# def dynamic_instrction(context: RunContextWrapper[personalInfo]):
#     """Fetch the name and id of the user. Call this function to get user's name and id information."""
#     return f'user name is {context.context.name} and user id is {context.context.id} '

# async def main():
#     user = personalInfo(name='Waqas', id=12345)

#     agent = Agent[personalInfo](
#         name='Assistant',
#         tools=[dynamic_instrction],
#         model_settings=ModelSettings(max_tokens=50),
#     )

#     result = await Runner.run(agent,' What is the user name and his id? ', run_config=config, context=user)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# @dataclass
# class IntroContext:
#     name: str

# @function_tool
# async def introduction(context: RunContextWrapper[IntroContext]) -> str:
#     return f"student name is {context.context.name}"

# async def main():
#     my_intro = IntroContext(name='Waqas')

#     teacher_agent = Agent[IntroContext](
#         name="Teacher Agent",
#         instructions="You help users with thier introduction. Use tools when needed.",
#         tools=[introduction]
#     )
#     # Conversation Context (LLM کو دی جانے والی history)
#     conversation = [
#     {"role": "user", "content": "Hello, my name is Waqas"},
#     {"role": "assistant", "content": "Hi Waqas, nice to meet you!"},
#     {"role": "user", "content": "What is my name?"},
#     ]

#     # conversation = 'What is the name of the user?'
#     result = await Runner.run(starting_agent=teacher_agent, input=conversation, context=my_intro,run_config=config
#     )
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# @dataclass
# class UdhaarBalance:
#     name:str
#     udhaar: float
    
# # Local Context 
# @function_tool
# async def get_udhaar_balance(ctx: RunContextWrapper[UdhaarBalance]):
#     return f'{ctx.context.name} your udhaar balance is {ctx.context.udhaar}'

# async def main():
#     shopkeeper=UdhaarBalance(name='Waqas',udhaar=540)

#     grocery_agent = Agent[UdhaarBalance](
#         name='Grocery Agent',
#         instructions='You are a helpful grocery store assistant. Use tools when needed.',
#         tools=[get_udhaar_balance]
#     )
#     # Conversation/LLM Context
#     conversation=[
#         {'role':'user', 'content':'Hi, I am Waqas'},
#         {'role':'assistant', 'content':'Do you want to see your shopping list history?'},
#         {'role':'user', 'content':'Yes, last time I bought milk, bread and eggs'},
#         {'role':'user', 'content':'Can you remind me of my last shopping list and also tell me my lsat udhaar?'},
#     ]
#     result = await Runner.run(starting_agent=grocery_agent, context=shopkeeper, input=conversation, run_config=config)
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# # Step 1: Local Context Class (backend data)
# @dataclass
# class GroceryContext:
#     udhaar_balance: float
#     shopping_history: list

# # Step 2: Tools (LLM tools use Local Context data)
# @function_tool
# async def get_udhaar_balance(context: RunContextWrapper[GroceryContext]) -> str:
#     return f"Your current udhaar balance is {context.context.udhaar_balance} PKR."

# @function_tool
# async def get_shopping_history(context: RunContextWrapper[GroceryContext]) -> str:
#     items = ", ".join(context.context.shopping_history)
#     return f"Your last shopping list was: {items}"

# # Step 3: Main function
# async def main():
#     # Local Context (backend data, hidden from LLM)
#     grocery_context = GroceryContext(
#         udhaar_balance=1500.0, 
#         shopping_history=["milk", "bread", "eggs"]
#     )

#     # Agent definition
#     grocery_agent = Agent[GroceryContext](
#         name="Grocery Agent",
#         instructions="You are a helpful grocery store assistant. Use tools to answer about udhaar balance and shopping history.",
#         tools=[get_udhaar_balance, get_shopping_history]
#     )

#     # Run Agent (NO conversation argument here)
#     result = await Runner.run(
#         starting_agent=grocery_agent,
#         # input="Can you show me my shopping history?",
#         input='Can you remind me my last udhaar balance?',
#         context=grocery_context,
#         run_config=config
#     )

#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# @dataclass
# class GroceryContext:
#     udhaar_balance: float
#     shopping_history: list

# @function_tool
# async def get_udhaar_balance(context: RunContextWrapper[GroceryContext]) -> str:
#     return f"Your current udhaar balance is {context.context.udhaar_balance} PKR."

# @function_tool
# async def get_shopping_history(context: RunContextWrapper[GroceryContext]) -> str:
#     items = ", ".join(context.context.shopping_history)
#     return f"Your last shopping list was: {items}"


# # Conversation Manager (Dynamic Memory)
# class ConversationManager:
#     def __init__(self):
#         self.conversation = []

#     def add_user_message(self, content: str):
#         self.conversation.append({"role": "user", "content": content})

#     def add_assistant_message(self, content: str):
#         self.conversation.append({"role": "assistant", "content": content})

#     def get_conversation(self):
#         return self.conversation


# async def main():
#     # Local context
#     grocery_context = GroceryContext(
#         udhaar_balance=1500.0,
#         shopping_history=["milk", "bread", "eggs"]
#     )

#     agent = Agent[GroceryContext](
#         name="Grocery Agent",
#         instructions="You are a helpful grocery store assistant.",
#         tools=[get_udhaar_balance, get_shopping_history]
#     )

#     memory = ConversationManager()

#     # --- First turn ---
#     user_input1 = "Hi, I am Waqas"
#     memory.add_user_message(user_input1)

#     result1 = await Runner.run(starting_agent=agent, input=user_input1, context=grocery_context, run_config=config)

#     memory.add_assistant_message(result1.final_output)
#     print("Assistant:", result1.final_output)

#     # --- Second turn ---
#     user_input2 = "Can you tell me my udhaar balance?"
#     memory.add_user_message(user_input2)

#     result2 = await Runner.run(starting_agent=agent, input=user_input2, context=grocery_context, run_config=config)

#     memory.add_assistant_message(result2.final_output)
#     print("Assistant:", result2.final_output)

#     # --- Third turn ---
#     user_input3 = "And what did I buy last time?"
#     memory.add_user_message(user_input3)

#     result3 = await Runner.run(starting_agent=agent, input=user_input3, context=grocery_context, run_config=config)

#     memory.add_assistant_message(result3.final_output)
#     print("Assistant:", result3.final_output)

#     # Print full dynamic conversation
#     print("\n--- Conversation History ---")
#     for msg in memory.get_conversation():
#         print(f"{msg['role'].upper()}: {msg['content']}")


# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# @dataclass
# class GroceryContext:
#     udhaar_balance: float
#     shopping_history: list

# @dataclass
# class UserInfo:
#     id: int
#     name: str
#     context: GroceryContext

# @function_tool
# async def get_udhaar_balance(context: RunContextWrapper[GroceryContext]) -> str:
#     return f"Your current udhaar balance is {context.context.udhaar_balance} PKR."

# @function_tool
# async def get_shopping_history(context: RunContextWrapper[GroceryContext]) -> str:
#     items = ", ".join(context.context.shopping_history)
#     return f"Your last shopping list was: {items}"

# class ConversationManager:
#     def __init__(self):
#         self.histories = {}  # {user_id: [messages]}

#     def add_message(self, user_id: int, role: str, content: str):
#         if user_id not in self.histories:
#             self.histories[user_id] = []
#         self.histories[user_id].append({"role": role, "content": content})

#     def get_history(self, user_id: int):
#         return self.histories.get(user_id, [])

# class UserStore:
#     def __init__(self):
#         self.users_by_id = {}
#         self.users_by_name = {}

#     def add_user(self, user: UserInfo):
#         self.users_by_id[user.id] = user
#         self.users_by_name[user.name.lower()] = user

#     def get_by_id(self, user_id: int) -> UserInfo:
#         return self.users_by_id[user_id]

#     def get_by_name(self, name: str) -> UserInfo:
#         return self.users_by_name[name.lower()]

# async def main():
#     # Create users
#     store = UserStore()
#     store.add_user(UserInfo(1, "Waqas", GroceryContext(1500, ["milk", "bread"])))
#     store.add_user(UserInfo(2, "Ali", GroceryContext(500, ["rice", "oil"])))
#     store.add_user(UserInfo(3, "Sara", GroceryContext(2500, ["eggs", "butter"])))
#     store.add_user(UserInfo(4, "Ahmed", GroceryContext(100, ["sugar"])))
#     store.add_user(UserInfo(5, "Hina", GroceryContext(0, ["tea", "biscuits"])))

#     memory = ConversationManager()

#     # Same agent for all users
#     agent = Agent[GroceryContext](
#         name="Grocery Agent",
#         instructions="You are a helpful grocery assistant. Use tools to answer about udhaar balance and shopping history.",
#         tools=[get_udhaar_balance, get_shopping_history]
#     )

#     user_name = 'Ahmed'
#     user = store.get_by_name(user_name)

#     user_input = f"Hello, can you tell me my udhaar balance and my last shopping list?"
#     memory.add_message(user.id, "user", user_input)

#     result = await Runner.run(
#         starting_agent=agent,
#         input=user_input,
#         context=user.context,  # pass this user's context
#         run_config=config
#     )

#     memory.add_message(user.id, "assistant", result.final_output)

#     print(f"\nAssistant to {user.name}:", result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from dataclasses import dataclass
# from configration import config

# @dataclass
# class GroceryContext:
#     udhaar_balance: float
#     shopping_history: list

# @dataclass
# class UserInfo:
#     id: int
#     name: str
#     context: GroceryContext

# class UserStore:
#     def __init__(self):
#         self.users_by_name = {}

#     def add_user(self, user: UserInfo):
#         self.users_by_name[user.name.lower()] = user

#     def get_by_name(self, name: str) -> UserInfo | None:
#         return self.users_by_name.get(name.lower())

# store = UserStore()

# @function_tool
# async def get_user_info_by_name(name: str) -> str:
#     """
#     Find user by name and return their udhaar balance + shopping history.
#     """
#     user = store.get_by_name(name)
#     if not user:
#         return f"Sorry, no user found with name {name}."

#     items = ", ".join(user.context.shopping_history)
#     return (
#         f"User {user.name} (ID {user.id}) has udhaar balance: "
#         f"{user.context.udhaar_balance} PKR. Last shopping list: {items}"
#     )

# async def main():
#     # Add sample users
#     store.add_user(UserInfo(1, "Waqas", GroceryContext(1500, ["milk", "bread"])))
#     store.add_user(UserInfo(2, "Ali", GroceryContext(500, ["rice", "oil"])))
#     store.add_user(UserInfo(3, "Sara", GroceryContext(2500, ["eggs", "butter"])))
#     store.add_user(UserInfo(4, "Ahmed", GroceryContext(100, ["sugar"])))
#     store.add_user(UserInfo(5, "Hina", GroceryContext(0, ["tea", "biscuits"])))

#     # Agent
#     agent = Agent(
#         name="Grocery Agent",
#         instructions="You are a helpful assistant. Use the get_user_info_by_name tool to answer about any user's udhaar or shopping history.",
#         tools=[get_user_info_by_name]
#     )

#     # Example query
#     user_input = "What is the udhaar balance and shopping history of Ali?"

#     result = await Runner.run(
#         starting_agent=agent,
#         input=user_input,
#         run_config=config
#     )

#     print("Assistant Output:", result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())



#BOTH USES OF CONTEXT AND DYNAMIC INSTRUCTIONS

# import asyncio
# from agents import Agent, Runner, RunContextWrapper, ModelSettings, function_tool
# from configration import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     name:str
#     role: str

# @function_tool
# async def get_user_name(wrapper: RunContextWrapper[UserInfo]):
#     return f'User name is {wrapper.context.name}'
    
# async def dynamic_instructions(context: RunContextWrapper[UserInfo], agent: Agent)->str:
#     return f""""
#         "You are {context.context.name}, a {context.context.role}. "
#         f"Always speak as if you are introducing yourself and speak help. "
#     """

# async def main():
#     user = UserInfo(name='Muhammad Waqas', role='Software Developer')
    
#     agent = Agent[UserInfo](
#         name='Assistant',
#         instructions=dynamic_instructions,
#         model_settings=ModelSettings(max_tokens=50),
#         tools=[get_user_name]
#     )
#     # user_input = 'What is user name?'
#     user_input = 'Introduce yourself?'

#     result = await Runner.run(starting_agent=agent, input=user_input, context=user, run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())



# OUTPUT_TYPE IN AGENT CLASS

## dictionary output_type
# import asyncio
# from agents import Agent, Runner
# from configration import config
# from pydantic import BaseModel

# class UserInfo(BaseModel):
#     name:str
#     age: int
#     role: str

# async def main():
#     agent = Agent(
#         name="Assistant",
#         instructions="Always return user info as structured output.",
#         output_type=UserInfo,
#     )

#     user_input='My name Muhammad Waqas and I am 23 years old and my role is Software Developer'

#     result = await Runner.run(agent, input=user_input, run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())

## list output_type
# import asyncio
# from agents import Agent, Runner
# from configration import config
# from typing import List
# from pydantic import BaseModel

# class UserInfo(BaseModel):
#     name: str
#     age: int

# async def main():
#     agent = Agent[UserInfo](
#         name="Multi user agent",
#         instructions="Extract all the users' names and ages from the input. "
#             "Return them as a list of UserInfo objects.",
#         output_type=List[UserInfo]
#     )
#     input_text = """
#     We have three users:
#     1. Ali is 25 years old.
#     2. Sara is 30 years old.
#     3. Waqas is 27 years old.
#     """
#     result = await Runner.run(agent, input=input_text, run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())


# AGENT CLONE

# from agents import Agent, Runner, ModelSettings
# from configration import config

# teacher_agent = Agent(
#     name='Teacher agent',
#     instructions='You are a teacher agent',
#     model_settings=ModelSettings(max_tokens=50)
# )
# student_agent = Agent.clone(
#     name='Student agent',
#     instructions='You are a student agent',
#     model_settings=ModelSettings(max_tokens=50)
# )

# result = Runner.run_sync(teacher_agent,'What is science?', run_config=config)
# print(result.final_output)
