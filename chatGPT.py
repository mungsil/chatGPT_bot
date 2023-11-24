import telegram
import asyncio
from openai import OpenAI

client = OpenAI(
    api_key=""
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
   messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

body=completion.choices[0].message.content

token = "6928016911:AAEfmD-uwp2jYpTxdN35vlI18BvqfpJ_x3M"
bot = telegram.Bot(token = token)
public_chat_name = '@kopensw'
asyncio.run(bot.sendMessage(chat_id=public_chat_name,text=body))