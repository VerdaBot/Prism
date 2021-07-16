# Imports
from os import listdir, environ

from discord import Embed, Color, Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand

# Load the config file
from dotenv import load_dotenv
load_dotenv('.env')

# Create the bot
bot = Bot(command_prefix=environ.get("BOT_PREFIX"))
bot.remove_command('help') # Prism uses a custom help command

# Create the slash command
slash = SlashCommand(bot, sync_commands=True)

# Load all modules in the modules folder
for cog in listdir('modules'):
	if cog.endswith('.py') and not cog.startswith('__'):
		print(f'Loaded {cog}')
		bot.load_extension(f'modules.{cog[:-3]}')

# Set bot status
@bot.event
async def on_ready():
	print(f"Connected as {bot.user}")
	current_activity = Activity(name=f"{len(bot.guilds)} server{'s' if len(bot.guilds) > 1 else ''}!", type=ActivityType.watching)
	await bot.change_presence(activity=current_activity)

# Error
@bot.event
async def on_command_error(ctx, error):
	embed = Embed(title="Error!", colour=Color.from_rgb(200, 200, 200), description=f"{str(error)}")
	embed.set_thumbnail(url=environ.get("BOT_ICON_ERROR"))
	await ctx.reply(embed=embed)

# Help command
@bot.command(name='help', help="Get all the commands.")
async def help(ctx):
	embed = Embed(title="Help!", colour=Color.from_rgb(200, 200, 200))
	#embed.add_field(name="", value="Prism is a bot for managing your server!", inline=False)
	#embed.add_field(name="", value="The following commands are available:", inline=False)

	for command in bot.commands:
		embed.add_field(name=command.name, value=command.help, inline=False)
	
	embed.set_thumbnail(url=environ.get("BOT_ICON"))
	await ctx.reply(embed=embed)

# Run the bot
bot.run(environ.get("TOKEN"))