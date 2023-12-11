
import discord
from discord.ext import commands
import logging
# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='>',intents=intents)


# @bot.event
# async def on_ready():
#     print("ログインしました！")
#     await bot.change_presence(activity=discord.Game(name="1"))

# @bot.command()
# async def ping(ctx):
#     raw_ping = bot.latency
#     ping = round(raw_ping * 1000)
#     await ctx.reply(f"Pong!\nBotのPing値は{ping}msです。")

# intents = discord.Intents.all()
# bot = commands.Bot(command_prefix="!", intents=intents)

# @bot.event
# async def on_ready():
#     print("ボットが起動した！")

# @bot.command()
# async def serverinfo(ctx):
#   guild = ctx.message.guild
#   roles =[role for role in guild.roles]
#   text_channels = [text_channels for text_channels in guild.text_channels]
#   embed = discord.Embed(title=f"{guild.name}info",color=0x3683ff)
#   embed.add_field(name="管理者",value=f"{ctx.guild.owner}",inline=False)
#   embed.add_field(name="ID",value=f"{ctx.guild.id}",inline=False)
#   embed.add_field(name="チャンネル数",value=f"{len(text_channels)}",inline=False)
#   embed.add_field(name="ロール数",value=f"{len(roles)}",inline=False)
#   embed.add_field(name="サーバーブースター",value=f"{guild.premium_subscription_count}",inline=False)
#   embed.add_field(name="メンバー数",value=f"{guild.member_count}",inline=False)
#   embed.add_field(name="サーバー設立日",value=f"{guild.created_at}",inline=False)
#   embed.set_footer(text=f"実行者 : {ctx.author} ")
#   await ctx.send(embed=embed)

# @bot.command()
# async def userinfo(ctx):
#   embed = discord.Embed(title=f"user {ctx.author.name}",description="userinfo",color=0x3683ff)
#   embed.add_field(name="名前",value=f"{ctx.author.mention}",inline=False)
#   embed.add_field(name="ID",value=f"{ctx.author.id}",inline=False)
#   embed.add_field(name="ACTIVITY",value=f"{ctx.author.activity}",inline=False)
#   embed.add_field(name="TOP_ROLE",value=f"{ctx.author.top_role}",inline=False)
#   embed.add_field(name="discriminator",value=f"#{ctx.author.discriminator}",inline=False)
#   embed.add_field(name="サーバー参加",value=f"{ctx.author.joined_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
#   embed.add_field(name="アカウント作成",value=f"{ctx.author.created_at.strftime('%d.%m.%Y, %H:%M Uhr')}",inline=False)
#   embed.set_thumbnail(url=f"{ctx.author.avatar.url}")
#   embed.set_footer(text=f"実行者 : {ctx.author} ")
#   await ctx.send(embed=embed)

# @bot.command(pass_content=True)
# @commands.has_permissions(administrator=True)
# async def nick(ctx, member: discord.Member, nick):
#   await member.edit(nick=nick)
#   embed = discord.Embed(title="ニックネームを変更しました",description=f"変更された人物: {member.mention}",color=0xffffff)
#   await ctx.send(embed=embed)
# bot.run('token')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run('MTE4MjMwOTUyMjcxMTI2MTI4Ng.GOPCns._PQm1ZgxeRcG47UyAzoO2agLxyfg9yURV8Xwzk',log_handler=handler)