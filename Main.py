import openai

openai.api_key= "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"

response = completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
         "content": "write a haiku about ai",
         
         }
    ],
        max_tokens = 100
)

print(response)
