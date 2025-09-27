
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)
model=OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=external_client
)
config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
agents={
    'inventary': Agent(
        name='Inventary Agent',
        instructions="'Check availability of grocery items, like 'Do you have sugar?' or 'Is oil in stock?'"
    ),
    "price": Agent(
        name="Price Agent",
        instructions="Provide current prices of items, like 'What is the price of 1 kg rice?'"
    ),
    "order": Agent(
        name="Order Agent",
        instructions="Take and confirm grocery orders, like 'Order 2 kg sugar and 1 ltr oil'"
    ),
    "credit": Agent(
        name="Credit Agent",
        instructions="Handle udhaar/credit tracking, like 'How much does Ali owe?'"

    ),
    "offers": Agent(
        name="Offers Agent",
        instructions="Inform about discounts and deals, like 'Any deals on detergent?'"
    ),
    "billing": Agent(
        name="Billing Agent",
        instructions="Calculate final bill total for ordered items, like 'What is the bill for 2kg aata and 1 milk?'"
    )
}
inventary_agent=Agent(
    name='Main Inventary Agent',
    instructions=(
        "You are a smart grocery assistant. Based on the user's input, choose the right category:\n"
        "- inventory → for stock queries\n"
        "- price → for price inquiries\n"
        "- order → for taking orders\n"
        "- credit → for udhaar/credit questions\n"
        "- offers → for ongoing discounts\n"
        "- billing → for final billing queries\n"
        "Reply with only one keyword from: inventory, price, order, credit, offers, billing. No explanation."
    )
)
user_input = input('Enter your grocery query : ')
invent_agent = Runner.run_sync(inventary_agent, user_input, run_config=config).final_output.strip().lower()
selected_agent = agents.get(invent_agent, agents["inventary"])
result = Runner.run_sync(invent_agent, user_input, run_config=config).final_output
print(user_input)
print(result)








# Load API key
# load_dotenv()
# gemini_api_key = os.getenv('GEMINI_API_KEY')

# # Gemini setup
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
# )

# model = OpenAIChatCompletionsModel(
#     model='gemini-2.0-flash',
#     openai_client=external_client
# )

# run_config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # 🧠 Sub-agents: grocery-specific roles
# agents = {
#     "inventory": Agent(
#         name="Inventory Agent",
#         instructions="Check availability of grocery items, like 'Do you have sugar?' or 'Is oil in stock?'"
#     ),
#     "price": Agent(
#         name="Price Agent",
#         instructions="Provide current prices of items, like 'What is the price of 1 kg rice?'"
#     ),
#     "order": Agent(
#         name="Order Agent",
#         instructions="Take and confirm grocery orders, like 'Order 2 kg sugar and 1 ltr oil'"
#     ),
#     "credit": Agent(
#         name="Credit Agent",
#         instructions="Handle udhaar/credit tracking, like 'How much does Ali owe?'"

#     ),
#     "offers": Agent(
#         name="Offers Agent",
#         instructions="Inform about discounts and deals, like 'Any deals on detergent?'"
#     ),
#     "billing": Agent(
#         name="Billing Agent",
#         instructions="Calculate final bill total for ordered items, like 'What is the bill for 2kg aata and 1 milk?'"
#     )
# }

# # 🤖 Main router agent
# router_agent = Agent(
#     name="Main Grocery Agent",
#     instructions=(
#         "You are a smart grocery assistant. Based on the user's input, choose the right category:\n"
#         "- inventory → for stock queries\n"
#         "- price → for price inquiries\n"
#         "- order → for taking orders\n"
#         "- credit → for udhaar/credit questions\n"
#         "- offers → for ongoing discounts\n"
#         "- billing → for final billing queries\n"
#         "Reply with only one keyword from: inventory, price, order, credit, offers, billing. No explanation."
#     )
# )

# # 🚀 Step 1: Get user input
# user_input = input("🛒 Enter your grocery query: ")

# # 🚀 Step 2: Route using main agent (no if-else)
# router_agent = Runner.run_sync(router_agent, user_input, run_config=run_config).final_output.strip().lower()

# # 🚀 Step 3: Use routing key to pick sub-agent
# selected_agent = agents.get(router_agent, agents["inventory"])  # fallback agent

# # 🚀 Step 4: Run sub-agent
# response = Runner.run_sync(selected_agent, user_input, run_config=run_config).final_output

# # 🧾 Step 5: Output
# print(f"\n📌 Agent selected: {selected_agent.name}")
# print(f"🧠 Response:\n{response}")






# multi_agent_school.py

# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# from dotenv import load_dotenv
# import os

# # Load environment variable
# load_dotenv()
# gemini_api_key = os.getenv('GEMINI_API_KEY')

# # External Gemini client
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
# )

# # Model setup
# model = OpenAIChatCompletionsModel(
#     model='gemini-2.0-flash',
#     openai_client=external_client
# )

# run_config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # All Sub-Agents
# agents = {
#     "attendance": Agent(
#         name="Attendance Agent",
#         instructions="Handle student attendance queries like 'Is Ali present today?' or 'Who was absent yesterday?'"
#     ),
#     "fee": Agent(
#         name="Fee Agent",
#         instructions="Handle student fee queries like 'How much fee is due for Ahmed?' or 'Who has paid full fee?'"
#     ),
#     "result": Agent(
#         name="Result Agent",
#         instructions="Handle student exam result queries like 'Show marks of Zainab' or 'Result of class 10th.'"
#     ),
#     "timetable": Agent(
#         name="Timetable Agent",
#         instructions="Provide class timetable information like 'What is the schedule for class 9?' or 'Which subject is at 10am today?'"
#     ),
#     "admission": Agent(
#         name="Admission Agent",
#         instructions="Answer queries related to new admissions like 'How to apply for admission?' or 'What are the documents required?'"
#     ),
#     "homework": Agent(
#         name="Homework Agent",
#         instructions="Provide or manage student homework information like 'What is the homework for class 8 today?'"
#     )
# }

# # Main Router Agent (AI decision-maker)
# router_agent = Agent(
#     name="School Main Agent",
#     instructions=(
#         "You are a smart school assistant. Based on the user's question, route it to the correct department:\n"
#         "- attendance → for attendance-related queries\n"
#         "- fee → for fee inquiries\n"
#         "- result → for exam results\n"
#         "- timetable → for class schedules\n"
#         "- admission → for new student admissions\n"
#         "- homework → for daily homework queries\n"
#         "Respond with exactly one keyword from: attendance, fee, result, timetable, admission, homework. Don't explain anything else."
#     )
# )

# # Step 1: Get user input
# user_input = input("Ask your school-related question: ")

# # Step 2: Route to correct agent
# route_response = Runner.run_sync(router_agent, user_input, run_config=run_config).final_output.strip().lower()

# # Step 3: Pick agent using key (no if-else!)
# selected_agent = agents.get(route_response, agents["attendance"])

# # Step 4: Run selected agent
# response = Runner.run_sync(selected_agent, user_input, run_config=run_config).final_output

# # Step 5: Show final output
# print(f"\nSelected Agent: {selected_agent.name}")
# print(f"Response:\n{response}")


