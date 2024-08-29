import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
    async def on_read(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
      if message.author == self.user:
        return

      if message.content.startswith('!meme'):
        await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('CODEHRECODEHERECODEERETOKENHERE')  <- #TOKEN INSIDE HERE

#! I have cleared the token for security purposes however the bot does work.
