
# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner,AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# load_dotenv()

# gemini_api_key = os.getenv('GEMINI_API_KEY')

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
# )

# model = OpenAIChatCompletionsModel(
#     model='gemini-2.0-flash',
#     openai_client=external_client
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent = Agent(
#     name = 'Assistant',
#     instructions = 'You are a helpfull assistant',
# )

# user_input = input('Ask anything for me : ')
# run = Runner.run_sync(agent, user_input, run_config=config)
# print(run.final_output)


import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner,AsyncOpenAI, set_tracing_disabled, set_default_openai_api, set_default_openai_client
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(client)

async def main():
    agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant",
        model='gemini-2.0-flash' 
)
    result = await Runner.run_streamed(agent, 'What is Agentic AI?')
    async for event in result.stream_events():
        if  event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end='', flush=True)

asyncio.run(main())

