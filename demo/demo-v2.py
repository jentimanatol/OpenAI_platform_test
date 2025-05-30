import openai

openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
  model="gpt-4",  # or "gpt-3.5-turbo"
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
)

print(response['choices'][0]['message']['content'])
