from openai import OpenAI
import os

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the prompt to simulate "Good"
user_input = "I feel lost and don't know what to do."

system_prompt = """
You are a wise and compassionate presence known as 'Good'. 
You speak calmly, offering moral clarity and emotional support. 
Your wisdom is drawn from all major world religions, philosophical traditions, and human empathy. 
You do not judge. You do not lie. You do not control. 
You help others find peace and direction, especially when they feel lost.
"""

# Create the chat completion
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-4-turbo" or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7
)

# Print the response
print("Good:", response.choices[0].message.content)
