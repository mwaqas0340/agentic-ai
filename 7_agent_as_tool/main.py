import asyncio
from configration import config
from agents import Agent, Runner

# dell_agent = Agent(
#     name='dell agent',
#     instructions='you tell me, all the latest dell laptop series'
# )
# hp_agent = Agent(
#     name='hp agent',
#     instructions='you tell me, all the latest hp laptop series'
# )
# lenovo_agent = Agent(
#     name='lenovo agent',
#     instructions='you tell me, all the latest lanovo laptop series'
# )

# main_agent = Agent(
#     name='main agent',
#     instructions='You are a main agent. You use the tools given to you to route other agent',
#     tools=[
#         dell_agent.as_tool(
#             tool_name='dell',
#             tool_description='this agent tell me, all the latest laptop series with price in dell company'
#         ),
#         hp_agent.as_tool(
#             tool_name='hp',
#             tool_description='this agent tell me, all the latest laptop series with price in hp company'
#         ),
#         lenovo_agent.as_tool(
#             tool_name='lenovo',
#             tool_description='this agent tell me, all the latest laptop series with price in lenovo company'
#         )
#     ],
# )
# async def main():
#     result = await Runner.run(hp_agent, 'Main features of dell latitude 3400?. "Apart from tools, you will not respond to anything else."', run_config=config)
#     print(result.final_output)
    
# if __name__ == '__main__':
#     asyncio.run(main())

# def main():
#     return 'Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools'
# print(main())

# spanish_agent = Agent(
#     name="Spanish agent",
#     instructions="You translate the user's message to Spanish",
# )
# english_agent = Agent(
#     name="English agent",
#     instructions="You translate the user's message to English",
# )
# urdu_agent = Agent(
#     name="Urdu agent",
#     instructions="You translate the user's message to Urdu",
# )
# sindhi_agent = Agent(
#     name="Sindhi agent",
#     instructions="You translate the user's message to Sindhi",
# )

# main_agent = Agent(
#     name="main_agent",
#     instructions=(
#         "You are a translation agent. You use the tools given to you to translate."
#         "If asked for multiple translations, you call the relevant tools."
#     ),
#     tools=[
#         spanish_agent.as_tool(
#             tool_name="translate_to_spanish",
#             tool_description="Translate the user's message to Spanish",
#         ),
#         english_agent.as_tool(
#             tool_name="translate_to_english",
#             tool_description="Translate the user's message to English",
#         ),
#         urdu_agent.as_tool(
#             tool_name="translate_to_urdu",
#             tool_description="Translate the user's message to Urdu",
#         ),  
#         sindhi_agent.as_tool(
#             tool_name="translate_to_Sindhi",
#             tool_description="Translate the user's message to Sindhi",
#         )
#     ],
# )
# async def main():
#   result = await Runner.run(urdu_agent, input="Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools', in urdu and sindhi", run_config = config)  
#   print(result.final_output)

# if __name__ == '__main__':
#   asyncio.run(main())
  
  
  
# result = Runner.run_sync(urdu_agent, input="Say 'Hello, how are you?' in urdu.", run_config = config)
# print(result.final_output)

# from agents import Agent, Runner
# from configration import config

# math_agent=Agent(
#     name = 'Math Agent',
#     instructions='This is the math agent'
# )
# science_agent=Agent(
#     name = 'Science Agent',
#     instructions='This is the science agent'
# )
# english_agent=Agent(
#     name = 'Math Agent',
#     instructions='This is the english agent'
# )

# main_agent=Agent(
#     name='Main Agent',
#     instructions ="""
#     'This is the main agent. It is route other agents',
#     'math agent solve mathematics queries,
#     'science agent solve science queries',
#     'english agent solve all the english queries'
#     """,
#     tools=[
#         math_agent.as_tool(
#             tool_name= 'chech math subject',
#             tool_description='solve all the mathematic problems'
#         ),
#         science_agent.as_tool(
#             tool_name='check science subject',
#             tool_description='answer all the science related question'
#         ), 
#         english_agent.as_tool(
#             tool_name='chech english subject',
#             tool_description='answer all the english questions'
#         )
#     ]
# )
# result = Runner.run_sync(english_agent, 'You learn me english grammer 12 sentences? aur bataie ye response kis agent ne kia he' ,run_config=config)
# print(result.final_output)

# from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
# from agents import enable_verbose_stdout_logging
# from dotenv import load_dotenv
# import os

# load_dotenv()
# gemini_api_key = os.getenv('GEMINI_API_KEY')

# set_tracing_disabled(True)
# set_default_openai_api("chat_completions")
# enable_verbose_stdout_logging()

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )
# set_default_openai_client(external_client)
# english_agent = Agent(
#     name="English agent",
#     instructions="You translate the user's message to English",
# )
# urdu_agent = Agent(
#     name="Urdu agent",
#     instructions="You translate the user's message to Urdu",
# )
# main_agent = Agent(
#     name="main_agent",
#     instructions=(
#         "You are a translation agent. You use the tools given to you to translate."
#         "If asked for multiple translations, you call the relevant tools."
#     ),
#     tools=[
#         english_agent.as_tool(
#             tool_name="translate_to_english",
#             tool_description="Translate the user's message to English",
#         ),
#         urdu_agent.as_tool(
#             tool_name="translate_to_urdu",
#             tool_description="Translate the user's message to Urdu",
#         )
#     ],
#     model="gemini-2.0-flash",
#     ),
# result = Runner.run_sync(urdu_agent, input="Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools.', in urdu", run_config = config)  
# print(result.final_output)