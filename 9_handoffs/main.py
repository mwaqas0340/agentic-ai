# from agents import Agent, Runner
# from configration import config

# urdu_agent = Agent(
#     name="Urdu agent",
#     instructions="You only speak Urdu."
# )
# sindhi_agent = Agent(
#     name="Sindhi agent",
#     instructions="You only speak Sindhi"
# )
# english_agent = Agent(
#     name="English agent",
#     instructions="You only speak English"
# )

# triage_agent = Agent(
#     name="Triage agent",
#     instructions="Handoff to the appropriate agent based on the language of the request.",
#     handoffs=[urdu_agent, sindhi_agent, english_agent],
# )
# result = Runner.run_sync(triage_agent, 'How are you? in urdu and sindhi', run_config=config)
# print(result.final_output)



# from agents import Agent, Runner, RunContextWrapper, handoff
# from configration import config
# import asyncio

# urdu_agent = Agent(
#     name="Urdu agent",
#     instructions="You only speak Urdu."
# )

# english_agent = Agent(
#     name="English agent",
#     instructions="You only speak English",
# )

# def on_handoff(agent: Agent, ctx: RunContextWrapper):
#     agent_name = agent.name
#     print(f"Handing off to {agent_name}...")
  
# async def main():
#     triage_agent = Agent(
#         name="Triage agent",
#         instructions="Handoff to the appropriate agent based on the language of the request.",
#         handoffs=[
#                 handoff(urdu_agent, on_handoff=lambda ctx: on_handoff(urdu_agent, ctx)),
#                 handoff(english_agent, on_handoff=lambda ctx: on_handoff(english_agent, ctx))
#         ]
#     )

#     result = await Runner.run(triage_agent, "Tum kese ho 'in english'", run_config=config)
#     print(result.final_output)

# asyncio.run(main())


# Advance Handoff

# from agents import Agent, Runner, handoff
# from configration import config

# account_agent = Agent(
#     name="Account Agent",
#     instructions="You handle account related info"
# )
# payment_agent = Agent(
#     name="Payment Agent",
#     instructions="You handle payment realted quereis"
# )

# # Custom Handoff
# custom_account_handoff = handoff(
#     agent=account_agent,
#     tool_name_override='account_service',
#     tool_description_override='Handles balance inquiries and account details.'
# )

# custom_payment_handoff = handoff(
#     agent=payment_agent,
#     tool_name_override='payment_service',
#     tool_description_override='Handles bill payments, money transfers, and transactions.'
# )

# triage_agent = Agent(
#         name="Triage Agent",
#     instructions="""
#         Analyze user's intent.
#         If they are talking about balance, accounts → use Account Agent.
#         If requesting payment or transfer → use Payment Agent.
#     """,
#     handoffs=[custom_account_handoff, custom_payment_handoff]
# )

# result = Runner.run_sync(triage_agent, 'I want to take my account detail', run_config=config)
# print(result.final_output)


# from agents import Agent, Runner, handoff
# from configration import config

# billin_agent = Agent(
#     name='billing agent',
#     instructions='You only response in billing-related quereis'
# )
# refund_agent = Agent(
#     name='refund agent',
#     instructions='You only response in refund-related queries'
# )

# #custom Handoff
# broken_delivery_refund=handoff(
#     agent=refund_agent,
#     tool_name_override='broken_delivery_refund',
#     tool_description_override='Handle refund due to broken item'
# )
# late_delivery_refund=handoff(
#     agent=refund_agent,
#     tool_name_override='late_delivery_refund',
#     tool_description_override='Handle refund due to late delivery'
# )

# triage_agent = Agent(
#     name='Triage agent',
#     instructions="""
#         Analyze user's intent.
#         If they are talking about billing → use billing agent.
#         If requesting payment or transfer → use refund agent.
#     """,
#     handoffs=[billin_agent, broken_delivery_refund, late_delivery_refund]
# )
# result = Runner.run_sync(triage_agent, 'I want to refund because your product is broken.', run_config=config)
# print(result.final_output)



# from agents import Agent, Runner, handoff, RunContextWrapper, function_tool
# from configration import config
# from pydantic import BaseModel

# class NewsRequest(BaseModel):
#     topic: str
#     reason: str

# @function_tool
# def get_weather(city: str) -> str:
#     """A simple function to get the weather for a user."""
#     return f"The weather for {city} is sunny."

# def on_news_transfer(ctx: RunContextWrapper, input_data: NewsRequest) -> None:
#     print(f"\nTransferring to for news updates. input_data:", input_data, "\n")

# news_agent: Agent = Agent(
#     name="NewsAgent",
#     instructions="You get latest news about tech community and share it with me.",
#     tools=[get_weather],
# )

# weather_agent: Agent = Agent(
#     name="WeatherAgent",
#     instructions="You are weather expert - share weather updates as I travel a lot. For all Tech and News let the NewsAgent handle that part by delegation.",
#     tools=[get_weather],
#     handoffs=[handoff(
#         agent=news_agent, 
#         on_handoff=on_news_transfer, 
#         input_type=NewsRequest)
#     ]
# )

# res = Runner.run_sync(weather_agent, "Check if there's any news about OpenAI after GPT-5 launch?", run_config=config)
# print("\nAGENT NAME", res.last_agent.name)
# print("\n[RESPONSE:]", res.final_output)



# from agents import Agent, Runner, handoff, function_tool, HandoffInputData
# from configration import config

# def summarized_news_transfer(data: HandoffInputData) -> HandoffInputData:
#     print("\n\n[HANDOFF] Summarizing news transfer...\n\n")
#     summarized_conversation = "Get latest tech news."
    
#     print("\n\n[ITEM 1]", data.input_history)
    
#     return HandoffInputData(
#         input_history=summarized_conversation,
#         pre_handoff_items=(),
#         new_items=(),
#     )

# @function_tool
# def get_weather(city: str) -> str:
#     """A simple function to get the weather for a user."""
#     return f"The weather for {city} is sunny."

# news_agent: Agent = Agent(
#     name="NewsAgent",
#     instructions="You get latest news about tech community and share it with me.",
#     tools=[get_weather],
# )

# weather_agent: Agent = Agent(
#     name="WeatherAgent",
#     instructions="You are weather expert - share weather updates as I travel a lot. For all Tech and News let the NewsAgent handle that part by delegation.",
#     tools=[get_weather],
#     handoffs=[handoff(agent=news_agent, input_filter=summarized_news_transfer)]
# )

# res = Runner.run_sync(weather_agent, "Check if there's any news about Google Gemini?", run_config=config)
# print("\nAGENT NAME", res.last_agent.name)
# print("\n[RESPONSE:]", res.final_output)




from agents import Agent, Runner, handoff, RunContextWrapper
from configration import config
from pydantic import BaseModel

class Users(BaseModel):
    name: str

billin_agent = Agent(
    name='billing agent',
    instructions='You only response in billing-related quereis'
)
refund_agent = Agent(
    name='refund agent',
    instructions='You only response in refund-related queries'
)
def handoff_fun(ctx: RunContextWrapper[Users]):
    return f'{ctx.context.name}successfully handoff'

late_delivery_refund=handoff(
    agent=refund_agent
)

triage_agent = Agent[Users](
    name='Triage agent',
    instructions="""
        Analyze user's intent.
        If they are talking about billing → use billing agent.
        If requesting payment or transfer → use refund agent.
    """,
    handoffs=[billin_agent,refund_agent]
)
result = Runner.run_sync(triage_agent, 'I want to refund because your product is broken.', run_config=config)
print(result.final_output)