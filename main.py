import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # To see members
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} is now active.')

@client.command(name='register')
async def register(ctx, name: str):
    # The code for the registration system starts from here.
    database = {}  # Database
    if ctx.author.id not in database:
        database[ctx.author.id] = {
            'name': name,
            'permission': 0
        }
        await ctx.send(f'The user {name} has been registered.')
    else:
        await ctx.send('You are already a registered member.')

@client.command(name='list')
async def list(ctx):
    database = {}
    # The list of registered members is displayed.
    list_message = 'Registered Members:\n'
    for id, data in database.items():
        list_message += f'{data["name"]} ({id})\n'
    await ctx.send(list_message)

@client.command(name='permission')
async def permission(ctx):
    database = {}
    # The list of members with permissions is displayed.
    database[ctx.author.id]['permission'] = 1
    list_message = 'Members with Permissions:\n'
    for id, data in database.items():
        list_message += f'{data["name"]} ({id})\n'
    await ctx.send(list_message)

@client.command(name='delete')
async def delete(ctx):
    # The deletion command.
    database = {}
    database.pop(ctx.author.id)
    await ctx.send(f'The registered member {ctx.author.mention} has been removed from the list.')

client.run('YOUR_BOT_TOKEN')  # Your bot token
