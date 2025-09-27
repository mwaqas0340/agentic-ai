from agents import Agent, Runner, handoff, set_trace_processors
from agents.tracing.processors import ConsoleSpanExporter, BatchTraceProcessor
from configration import config

exporter=ConsoleSpanExporter()
processor=BatchTraceProcessor(exporter)

set_trace_processors([processor])

billin_agent = Agent(
    name='billing agent',
    instructions='You only response in billing-related quereis'
)
refund_agent = Agent(
    name='refund agent',
    instructions='You only response in refund-related queries'
)

#custom Handoff
broken_delivery_refund=handoff(
    agent=refund_agent,
    tool_name_override='broken_delivery_refund',
    tool_description_override='Handle refund due to broken item'
)
late_delivery_refund=handoff(
    agent=refund_agent,
    tool_name_override='late_delivery_refund',
    tool_description_override='Handle refund due to late delivery'
)

triage_agent = Agent(
    name='Triage agent',
    instructions="""
        Analyze user's intent.
        If they are talking about billing → use billing agent.
        If requesting payment or transfer → use refund agent.
    """,
    handoffs=[billin_agent, broken_delivery_refund, late_delivery_refund]
)
result = Runner.run_sync(triage_agent, 'I want to refund because your product is broken', run_config=config)
print(result.final_output)
