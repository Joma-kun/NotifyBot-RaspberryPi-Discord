import discord
import time
import segment

#you can change here acordingto your environment
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
CHANNELID = 123456789123456789

client = discord.Client()

#send message
@client.event
async def on_ready():
    channel = client.get_channel(CHANNELID)
    await channel.send("Someone pushed the Button!")
    print("Someone pushed the Button!")

    #show in segments
    segment.print_calling()

    #stop loop
    await client.close()

#start loop
client.run(TOKEN)