import discord
from discord.ext import commands

intent = discord.Intents.all()
intent.members = True

client = commands.Bot(command_prefix = "-", intents=intent)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("discord.gg/tsurugi"))
    print("Bot is Online!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_role("own")
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@client.command()
async def cmds(ctx):
    embed = discord.Embed(title="Commands :", color=0xff000d)

    embed.add_field(name="-ping", value="Pings the bot", inline=False)
    embed.add_field(name="-clear", value="Purges messages", inline=False)
    embed.add_field(name="-invite", value="Sends a permanent link for the server!", inline=False)
    embed.add_field(name="-stock", value="Checks the stock!", inline=False)
    embed.add_field(name="-cmds", value="Shows this embed message!", inline=False)
    embed.add_field(name="-kick", value="Kicks a member", inline=False)
    embed.add_field(name="-mute", value="Mutes a member", inline=False)
    embed.add_field(name="-ban", value="Bans a member", inline=False)
    embed.add_field(name="-members", value="Shows the membercount of the server!", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
    invite = await ctx.channel.create_invite(max_age=0, max_uses=0)
    await ctx.send(f'Here is a link for the server : {invite.url}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = 'No reason provided'
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for {reason}')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = 'No reason provided'
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason}')

@client.command()
async def stock(ctx):
    channel = discord.utils.get(ctx.guild.channels, name='stock')
    await ctx.send(f'Check the #{channel.name} channel!')

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        await ctx.send("The 'Muted' role does not exist, please create one and try again.")
        return
    await member.add_roles(role)
    await ctx.send(f'Muted {member.mention}')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='wlc')
    if channel:
        await channel.send(f'Welcome to the server, {member.name}!')

@client.command()
async def members(ctx):
    members = ctx.guild.members
    await ctx.send(f'There are {len(members)} members in this server.')

client.run("MTI0MjE5MTg2ODYxNjUxMTUyOA.GiWgGt.HaIXwG8NaFGpGcG1vl_LPfdvE42Xi2PRfV6-FU")
