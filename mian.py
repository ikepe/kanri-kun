import discord
import yaml

import reboot

# config.yamlから情報を引き出す
with open("config.yml") as file:
  config = yaml.safe_load(file)
  TOKEN = config["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("!reboot"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            await message.channel.send("再起動します")
            reboot.reboot()
            await message.channel.send("再起動しました")
            print('終了')

client.run(TOKEN)