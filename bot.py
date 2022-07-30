import discord
import time
import segment

TOKEN = "XXXXXXXXXXXXXXXXX"

CHANNELID =1002928960591646802 

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(CHANNELID)
    await channel.send("Someone pushed the Button!")
    print("Someone pushed the Button!")
    segment.print_calling()
    await client.close()
    

client.run(TOKEN)