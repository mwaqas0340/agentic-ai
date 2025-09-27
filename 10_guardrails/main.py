# Input Guardrail

# import asyncio
# from configration import config
# from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
# from pydantic import BaseModel
# import rich

# class PassengerOutput(BaseModel):
#     response: str
#     isWeight: bool

# security_guard_agent = Agent(
#     name='security guard',
#     instructions="""
#         Your task to check the passenger luggage.
#         If passenger's luggage more then 25KGs, gracefully stop them. 
#     """,
#     output_type=PassengerOutput
# )

# @input_guardrail
# async def aeroplane_security_guard(ctx, agent, input):

#     result = await Runner.run(security_guard_agent, input, run_config=config)
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output.response,
#         tripwire_triggered=result.final_output.isWeight
#         )

# # Main Agent
# passenger_agent=Agent(
#     name='passenger agent',
#     instructions='You are a passenger agent',
#     input_guardrails=[aeroplane_security_guard]
# )
# async def main():
#     try: 
#         result = await Runner.run(passenger_agent, 'My luggage weught is 10kg.', run_config=config)
#         print('Passenger is onboarded')
#     except InputGuardrailTripwireTriggered:
#         print('Passenger cannot check-in')

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from configration import config
# from agents import Agent , Runner, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, ModelSettings
# from pydantic import BaseModel

# class MathOutput(BaseModel):
#     response: str
#     is_math: bool 

# customer_support_agent = Agent(
#     name='math agent',
#     instructions="""
#         Check the math home work of the students.
#         If the students do the math home work. Then it will not check    
#     """,
#     output_type=MathOutput
# )

# @input_guardrail
# async def math_homework(ctx, agent, input):
#     result = await Runner.run(customer_support_agent, input, run_config=config)
#     print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output.response,
#         tripwire_triggered=result.final_output.is_math
#     )

# checker_agent = Agent(
#     name='checker agent',
#     instructions='You are a checker agent',
#     input_guardrails=[math_homework],
#     model_settings=ModelSettings(max_tokens=50)
# )
# async def main():
#     try:
#         result = await Runner.run(checker_agent, 'What is Physics?', run_config=config)
#         print('Checked your Math home work')
#     except InputGuardrailTripwireTriggered:
#         print('Cannot check your Math home work')

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from configration import config
# from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput

# language_restriction_agent =Agent(
#     name='language restriction agent',
#     instructions="""
#         Your task to check the user languages,
#         If user's speak English and Urdu then you will give the answer othrwise you did not answer.  
#     """
# )
# @input_guardrail
# async def language_checker(context, agent, input):

#     result = await Runner.run(language_restriction_agent, input, run_config=config)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=False
#     )
# async def main():
#     user_agent =Agent(
#         name='user agent',
#         instructions='You are a user agent',
#         input_guardrails=[language_checker]
#     )
#     result = await Runner.run(user_agent, 'Hola', run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from configration import config
# from agents import Agent , Runner, input_guardrail, output_math_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, ModelSettings
# from pydantic import BaseModel
# import rich
# class MathOutput(BaseModel):
#     reasoning: str
#     is_math: bool 

# class PhysicsOutput(BaseModel):
#     reasoning: str
#     is_physics: bool

# # class MainAgentOutput(BaseModel):
# #     response: str

# input_guardrail_agent = Agent(
#     name='input guardrail agent',
#     instructions='Check if the user is asking you to do their math homework',
#     output_type=MathOutput
# )
# output_guardrail_check = Agent(
#     name='output guardrail agent',
#     instructions='Check if the user is asking you to do their physics homework',
#     output_type=PhysicsOutput
# )

# @input_guardrail
# async def math_homework(ctx, agent, input):
#     result = await Runner.run(input_guardrail_agent, input, run_config=config)
#     rich.print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.is_math
#     )
# @output_math_guardrail
# async def physics_homework(ctx, agent, output):
#     result = await Runner.run(output_guardrail_check, output, run_config=config)
#     rich.print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.is_physics
#     )

# customer_support_agent = Agent(
#     name='customer support agent',
#     instructions='You help customers with their qyestions',
#     input_guardrails=[math_homework],
#     output_guardrails=[physics_homework],
#     model_settings=ModelSettings(max_tokens=50)
# )
# async def main():
#     try:
#         result = await Runner.run(customer_support_agent, 'Who is the foundre of Pakistan?', run_config=config)
#         print(result.final_output)
#     except InputGuardrailTripwireTriggered:
#         print('This is Math home work')
#     except OutputGuardrailTripwireTriggered:
#         print('This is Physics home work')

# if __name__ == '__main__':
#     asyncio.run(main())



# import asyncio
# from configration import config
# from agents import Agent , Runner, output_guardrail, GuardrailFunctionOutput,  OutputGuardrailTripwireTriggered, ModelSettings
# from pydantic import BaseModel
# import rich

# class MainAgentOutput(BaseModel):
#     response: str

# class PhysicsOutput(BaseModel):
#     reasoning: str
#     is_physics: bool

# output_guardrail_check = Agent(
#     name='output guardrail agent',
#     instructions='Check if the user is asking you to do their physics homework',
#     output_type=PhysicsOutput
# )

# @output_guardrail
# async def physics_homework(ctx, agent, output: MainAgentOutput):
#     result = await Runner.run(output_guardrail_check, output.response, run_config=config)
#     rich.print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=result.final_output.is_physics
#     )

# customer_support_agent = Agent(
#     name='customer support agent',
#     instructions='You help customers with their qyestions',
#     output_guardrails=[physics_homework],
#     model_settings=ModelSettings(max_tokens=50)
# )
# async def main():
#     try:
#         result = await Runner.run(customer_support_agent, 'Define first law of motion?', run_config=config)
#         print(result.final_output)
#     except OutputGuardrailTripwireTriggered:
#         print('This is Physics home work')

# if __name__ == '__main__':
#     asyncio.run(main())



# import asyncio
# from configration import config
# from agents import Agent , Runner, input_guardrail, output_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, ModelSettings
# from pydantic import BaseModel
# import rich

# class MathInput(BaseModel):
#     reasoning: str
#     is_math: bool 

# class MathOutput(BaseModel):
#     reasoning: str
#     is_math: bool 

# input_guardrail_agent = Agent(
#     name='input guardrail agent',
#     instructions=(
#         "Only trigger if the user is explicitly asking you to complete a school math homework or assignment. "
#         "Ignore normal math related to shopping, budgeting, or everyday life."
#     ),
#     output_type=MathInput
# )

# output_guardrail_check = Agent(
#     name='output guardrail check',
#     instructions='Check if the output includes any math.',
#     output_type=MathOutput
# )

# # SHARED_POLICY = {
# #     "input": (
# #         "Trigger ONLY if user is asking for school math homework or assignment. "
# #         "Ignore everyday calculations."
# #     ),
# #     "output": (
# #         "Trigger if the response contains explicit math calculations or algebraic solving."
# #     )
# # }

# # input_guardrail_agent = Agent(
# #     name="input guardrail",
# #     instructions=SHARED_POLICY["input"],
# #     output_type=MathInput
# # )

# # output_guardrail_check = Agent(
# #     name="output guardrail",
# #     instructions=SHARED_POLICY["output"],
# #     output_type=MathOutput
# # )

# @input_guardrail
# async def math_homework1(ctx, agent, input):
#     result = await Runner.run(input_guardrail_agent, input, run_config=config)
#     rich.print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.is_math
#     )
# @output_guardrail
# async def math_homework2(ctx, agent, output):
#     result = await Runner.run(output_guardrail_check, output, run_config=config)
#     rich.print(result.final_output)
    
#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.is_math
#     )

# customer_support_agent = Agent(
#     name='customer support agent',
#     instructions='You help customers with their questions',
#     input_guardrails=[math_homework1],
#     output_guardrails=[math_homework2],
#     model_settings=ModelSettings(max_tokens=50)
# )
# async def main():
#     try:
#         result = await Runner.run(customer_support_agent, 'Tell me the price if each pen costs $2 and I buy 4 pens.', run_config=config) #Hello, can you help me solve for x: 2x + 3 = 11?
#         print(result.final_output)
#     except InputGuardrailTripwireTriggered:
#         print('Input Guardrail Tripped')
#     except OutputGuardrailTripwireTriggered:
#         print('Output Guardrail Tripped')

# if __name__ == '__main__':
#     asyncio.run(main())



# import asyncio
# from configration import config
# from agents import Agent, Runner, input_guardrail, output_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, ModelSettings
# from pydantic import BaseModel
# import rich

# class GroceryInput(BaseModel):
#     reasoning: str
#     is_restricted: bool

# class GroceryOutput(BaseModel):
#     reasoning: str
#     contains_restricted: bool

# RESTRICTED_ITEMS = ["alcohol", "beer", "wine", "whiskey", "cigarette", "tobacco", "drug", "opium"]

# input_guardrail_agent=Agent(
#     name='input guardrail agent',
#     instructions=(
#         f"Trigger if the user is trying to buy or ask about any of these restricted items: {', '.join(RESTRICTED_ITEMS)}. "
#         "Ignore all normal grocery requests."),
#         output_type=GroceryInput
# )
# output_guardrail_check=Agent(
#     name='output guardrail check',
#     instructions=(
#         f"Check if the response contains any restricted items: {', '.join(RESTRICTED_ITEMS)}. "
#         "If yes, trigger."),
#         output_type=GroceryOutput
# )

# @input_guardrail()
# async def grocery_input_guard(ctx, agent, input):
#     result = await Runner.run(input_guardrail_agent, input, run_config=config)
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.is_restricted
#     )
# @output_guardrail()
# async def grocery_output_guard(ctx, agent, input):
#     result = await Runner.run(output_guardrail_check, input, run_config=config)
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output.reasoning,
#         tripwire_triggered=result.final_output.contains_restricted
#     )

# async def main():
#     customer_support_agent=Agent(
#         name='customer support agent',
#         instructions='You are a grocery store assistant.',
#         input_guardrails=[grocery_input_guard],
#         output_guardrails=[grocery_output_guard],
#         model_settings=ModelSettings(max_tokens=50)
#     )
#     try:
#         # CASE 1: Input Guardrail Trigger
#         #user_input = "Can I buy 2 bottles of whiskey?"

#         # CASE 2: Output Guardrail Trigger
#         user_input = "Do you sell cold drink"

#         # CASE 3: Safe Transaction
#         # user_input = "Do you have fresh apples and bananas?"

#         result = await Runner.run(customer_support_agent, user_input, run_config=config)
#         rich.print(result.final_output)
#     except InputGuardrailTripwireTriggered:
#         print('Input Guardrail Tripped')
#     except OutputGuardrailTripwireTriggered:
#         print('Output Guardrail Tripped')

# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
# from configration import config
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from pydantic import BaseModel

# class CustomerInfo(BaseModel):
#     name: str
#     balance: float

# @function_tool
# async def get_udhaar(ctx: RunContextWrapper[CustomerInfo], agent: Agent):
#     return f'{ctx.context.name} ap ka {ctx.context.balance} udhaar baki hai'

# async def main():
#     user = CustomerInfo(
#         name='Waqas Rajput',
#         balance=580
#     )
#     agent = Agent[CustomerInfo](
#         name='Assistant',
#         instructions='You are a helpful assistant',
#         tools=[get_udhaar]
#     )
#     result = await Runner.run(starting_agent=agent, input='Mera udhaar kitna hai?',context=user, run_config=config)
#     print(result.final_output)

# if __name__ == '__main__':
#     asyncio.run(main())

