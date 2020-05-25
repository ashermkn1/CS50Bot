import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # guild = discord.utils.get(client.guilds, name=GUILD)
    # print(
    #    f'{client.user} is connected to the following guild:\n'
    #   f'{guild.name}(id: {guild.id})\n'
    # )

    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message: discord.Message):
    channel = client.get_channel(702302895353233439)
    if message.author == client.user:
        return
    if message.content.contains("https://discord.gg/"):
        print(message.author)
        await message.channel.send(f'{message.author.mention}, we do not allow promotions of any kind, whether it '
                                   f'be self promotions or discord server links of any kind. Please see {channel.mention} for more details')


client.run(TOKEN)
