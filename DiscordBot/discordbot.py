import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='//')


@client.event
async def on_ready():
    print('Bot Launched')
    channel = client.get_channel(801371604885831702)
    await channel.send('Hello, I am battle bot, your funny assistant!')
    embedVar = discord.Embed(title="Commands", description="List of commands:", color=discord.Colour.blurple())
    embedVar.add_field(name="Command Prefix", value="Command prefix: //", inline=False)
    embedVar.add_field(name="Ping", value=".ping(shows the ping of your internet.)", inline=False)
    embedVar.add_field(name="8ball", value=".8ball 'and your question'(asks the 8ball a question)", inline=False)
    embedVar.add_field(name='Pun', value='.pun(The bot will say a pun)')
    await channel.send(embed=embedVar)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['● It is certain.',
                 '● It is decidedly so.',
                 '● Without a doubt.',
                 '● Yes – definitely.',
                 '● You may rely on it.',

                 '● As I see it, yes.',
                 '● Most likely.',
                 '● Outlook good.',
                 '● Yes.',
                 '● Signs point to yes.',

                 '● Reply hazy, try again.',
                 '● Ask again later.',
                 '● Better not tell you now.',
                 '● Cannot predict now.',
                 '● Concentrate and ask again.',

                 "● Don't count on it.",
                 '● My sources say no.',
                 '● Outlook not so good.',
                 '● Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild_bans()


@client.command()
async def math(ctx, *, expression: str):
    calculation = eval(expression)
    await ctx.send('Question: {}\nAnswer: {}'.format(expression, calculation))


@client.command()
async def commands(message):
    embedVar = discord.Embed(title="Commands", description="List of commands:", color=discord.Colour.blurple())
    embedVar.add_field(name="Command Prefix", value="Command prefix: //", inline=False)
    embedVar.add_field(name="Ping", value=".ping(shows the ping of your internet.)", inline=False)
    embedVar.add_field(name="8ball", value=".8ball 'and your question'(asks the 8ball a question)", inline=False)
    embedVar.add_field(name='Pun', value='.pun(The bot will say a pun)')
    await message.channel.send(embed=embedVar)


@client.command()
async def pun(ctx):
    puns = ['I got fired from the calendar factory, just for taking a day off.',
            'What’s the best thing about Switzerland? Well, the flag is a big plus.',
            'What are windmills’ favorite genre of music? They’re big metal fans.',
            'I love whiteboards. They’re re-markable.',
            'The machine at the coin factory     just suddenly stopped working. It doesnt make any cents.',
            'I was worried about being in a long-distance relationship. But so far so good.',
            'I quit my job at the donut factory. I was fed up with the hole business.',
            "It's not the man didn't know how to juggle,he just didn't have the balls to do it!"]
    await ctx.send(f'Pun: {random.choice(puns)}')

@client.event
async def on_message(message):
    curse_words = ['badword1', 'badword2']
    if any(x in message.content.lower() for x in curse_words):
        print(f'Curse found')
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Do not use that word, or else you will get banned!")

client.run('#put your bot token here')
