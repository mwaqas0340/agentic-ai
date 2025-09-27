
import asyncio
from configration import config
from pydantic import BaseModel
from agents import Agent, Runner, RunContextWrapper

# class UserInfo(BaseModel):
#     name: str
#     occupation: str
#     language: list[str]
#     mobile: int

# agent = Agent[UserInfo](
#     name="Calendar extractor",
#     instructions="Extract calendar events from the given text and return them in structured format.",
#     # output_type=UserInfo
# )

# async def main():
#     result = await Runner.run(agent, 'My name is Muhammad Waqas. I am a Software Developer befare I had'
#     'learned TypeScript and Python programing and my mobile number is 987654321', run_config=config)
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())



class WeatherAnswer(BaseModel):
    location: str
    temperature_c: float
    summary: str

agent = Agent[WeatherAnswer](
    name='Weather agent',
    output_type=WeatherAnswer
    )
result = Runner.run_sync(agent, "What's the weather in Karachi?",run_config=config)
print(result.final_output)
