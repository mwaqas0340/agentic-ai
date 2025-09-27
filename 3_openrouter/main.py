# Use Single Model

# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner,AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# load_dotenv()

# openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# external_client = AsyncOpenAI(
#     api_key=openrouter_api_key,
#     base_url='https://openrouter.ai/api/v1'
# )

# model = OpenAIChatCompletionsModel(
#     model='deepseek/deepseek-r1-0528:free',
#     # model='google/gemma-3n-e2b-it:free',
#     openai_client=external_client
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# my_agent = Agent(
#     name = 'Assistant',
#     instructions = 'You are a helpfull assistant',
# )

# # user_input = input('Ask anything for me : ')
# run = Runner.run_sync(my_agent, 'Who is the founder of Pakistan?', run_config=config)
# print(run.final_output)


# Use Multiple Models

# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner,AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# load_dotenv()

# openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# external_client = AsyncOpenAI(
#     api_key=openrouter_api_key,
#     base_url='https://openrouter.ai/api/v1'
# )
# models = {
#     "mistral": OpenAIChatCompletionsModel(
#         model="mistralai/mistral-7b-instruct",
#         openai_client=external_client
#     ),
#     "deepseek": OpenAIChatCompletionsModel(
#         model="deepseek/deepseek-r1-0528:free",
#         openai_client=external_client
#     ),
#     "gpt": OpenAIChatCompletionsModel(
#         model="openai/gpt-3.5-turbo",
#         openai_client=external_client
#     )
# }

# my_agent = Agent(
#     name = 'Assistant',
#     instructions = 'You are a helpfull assistant',
# )

# def run_agent(user_input, model_key):
#     if model_key not in models:
#         raise ValueError("Model not found!")

#     model = models[model_key]

#     config = RunConfig(
#         model=model,
#         model_provider=external_client,
#         tracing_disabled=True
#     )
#     result = Runner.run_sync(my_agent, user_input, run_config=config)
#     print(f"\n🔁 Model: {model_key}\n📤 Response:\n{result.final_output}")

# if __name__ == "__main__":
#     user_msg = "Who is the founder of Pakistan? short answer"
    
#     # Change model key to: mistral, deepseek, or gpt
#     run_agent(user_msg, model_key="deepseek")
#     run_agent(user_msg, model_key="mistral")
#     run_agent(user_msg, model_key="gpt")



# Now Response any One Agent 

# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner,AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# load_dotenv()

# openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# external_client = AsyncOpenAI(
#     api_key=openrouter_api_key,
#     base_url='https://openrouter.ai/api/v1'
# )
# models = {
#     "mistral": OpenAIChatCompletionsModel(
#         model="mistralai/mistral-7b-instruct",
#         openai_client=external_client
#     ),
#     "deepseek": OpenAIChatCompletionsModel(
#         model="deepseek/deepseek-r1-0528:free",
#         openai_client=external_client
#     ),
#     "gpt": OpenAIChatCompletionsModel(
#         model="openai/gpt-3.5-turbo",
#         openai_client=external_client
#     )
# }
# # Step 2: RunConfig for each model
# configs = {
#     model_key: RunConfig(
#         model=models[model_key],
#         model_provider=external_client,
#         tracing_disabled=True
#     )
#     for model_key in models
# }

# # Agent definition
# my_agent = Agent(
#     name="Grocery Assistant",
#     instructions="You are a helpful grocery assistant. Always respond in Urdu."
# )

# # Model priority list
# model_priority = [ "deepseek","gpt","mistral"]

# # 🚀 Unified runner with fallback
# def run_agent_with_fallback(user_input):
#     for model_key in model_priority:
#             result = Runner.run_sync(
#                 my_agent,
#                 user_input,
#                 run_config=configs[model_key]
#             )
#             print(f"\n✅ Response from {model_key}:\n{result.final_output}")
#             return ''  
# if __name__ == "__main__":
#     user_msg = "Mujhe 2 kilo aata aur 1 packet chai chahiye."
#     run_agent_with_fallback(user_msg)



