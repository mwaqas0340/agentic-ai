
import asyncio
from agents import Agent, Runner
from configration import config
from openai.types.responses import ResponseTextDeltaEvent

async def main():
    agent=Agent(
        name='Assistant',
        instructions='You are a helpful assistant'
    )

    result = Runner.run_streamed(agent, 'What is AI?', run_config=config)
    async for event in result.stream_events():
        if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end='', flush=True)

if __name__ == '__main__':
    asyncio.run(main())
