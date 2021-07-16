# Imports
from os import listdir, environ

import discord
from discord.ext import commands
from discord.ext.commands import Bot

# Load the config file
from dotenv import load_dotenv
load_dotenv('.env')

bot = Bot(command_prefix=environ.get("BOT_PREFIX"))
bot.remove_command('help') # Prism uses a custom help command

# Load all extentions in the extentions folder
for cog in listdir('extentions'):
	if cog.endswith('.py'):
		bot.load_extension(f'extentions.{cog[:-3]}')

# Set bot status
@bot.event
async def on_ready():
	print(f"Connected as {bot.user}")

	current_activity = discord.Activity(name=f"{len(bot.guilds)} server{'s' if len(bot.guilds) > 1 else ''}!", type=discord.ActivityType.watching)

	await bot.change_presence(activity=current_activity)

# Error
@bot.event
async def on_command_error(ctx, error):
	embed = discord.Embed(title="Error!", colour=discord.Color.from_rgb(255, 255, 255), description=f"{str(error)}")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863521569032896513/865481093054070824/Untitled179.png")
	await ctx.reply(embed=embed)

bot.run(environ.get("TOKEN"))