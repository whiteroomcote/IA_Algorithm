from openai import OpenAI
import openai
client = OpenAI()
openai.api_key= "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"

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
         "content": "write a haiku about ai"
         }

    ]
)
