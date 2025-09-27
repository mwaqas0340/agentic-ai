# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner, function_tool
# from main import config
# import requests

# load_dotenv()

# api_key = os.getenv('WEATHER_API_KEY')

# if not api_key:
#     raise ValueError('GEMINI_API_KEY is not set in your system')

# @function_tool
# def get_weather(city):
#     'Get the current weather for a given city.'
#     weather_api_key = os.getenv('WEATHER_API_KEY')
 
#     url = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}")
#     data = url.json()
#     return f"The current weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
    
# agent=Agent(
#     name='Weather Agent',
#     instructions = 'You are a weather agent',
#     tools=[get_weather]
# )

# result = Runner.run_sync(agent, 'What is the weather in Khipro?', run_config=config)
# print(result.final_output)


from agents import Agent, Runner, function_tool
from main import config

customer_udhaar = [
    {'name': 'Ali', 'udhaar': 540},
    {'name': 'Muneeb', 'udhaar': 290},
    {'name': 'Ahmed', 'udhaar': 170},
]

@function_tool()
def get_udhaar(customer: str)-> str:
    """
      Returns the udhaar of the given customer.
    """
    for record in customer_udhaar:
        if record['name'].lower() == customer.lower():
            return(f'{record['name']} ka udhaar {record['udhaar']} rupay hai')
            
    return f"{customer} ka koi udhaar record nahi mila."

@function_tool()
def clear_udhaar(customer: str)-> str:
    """
      Sets the udhaar of the given customer to 0.
    """
    for record in customer_udhaar:
        if record['name'].lower() == customer.lower():
            if record['udhaar'] == 0:
                return f"{record['name']} ka udhaar pehle hi clear ho chuka hai."
            record['udhaar'] = 0
            return f"{record['name']} ka udhaar ab 0 kar diya gaya hai. Shukriya!"

    return f"{customer} ka koi udhaar record nahi mila."

@function_tool()
async def get_total_udhaar():
    """
        Returns the total udhaar of all customers.
    """
    total = 0
    for record in customer_udhaar:
        total+=record['udhaar']

    return f'Sab customer ka total udhaar {total} hai.'

@function_tool()
async def send_udhaar_reminder(customer: str) -> str:
    """
    Sends a reminder to the given customer about their udhaar.
    """
    for record in customer_udhaar:
        if record['name'].lower() == customer.lower():
            return f"Reminder: {record['name']} bhai, aapka {record['udhaar']} rupay udhaar baqi hai. Barah-e-karam jald adaigi karein."
    
    return f"{customer} ka koi udhaar record nahi mila."

agent=Agent(
    name='Assistant',
    instructions = 'You are a helpfull assistant. Help user find udhaar of any customer.',
    tools=[get_udhaar, clear_udhaar, get_total_udhaar,send_udhaar_reminder]
)
result = Runner.run_sync(agent, 'Ali ka udhaar kitna hai?', run_config=config, max_turns=3)
print(result.final_output)

