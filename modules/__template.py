# Standard Imports
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

# Extra Imports

class Template(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Commands
	@commands.command(name="template", help="This is a command.")
	async def template(self, ctx):
		await ctx.send("It works!")

	# Slash Comands
	@cog_ext.cog_slash(name="template", description="This is a slash command.")
	async def slash_template(self, ctx: SlashContext):
		await ctx.send(f"This is a slash command!")

	# Events
	@commands.Cog.listener()
	async def on_message(self, message):
		await message.channel.send("It works!")

def setup(bot):
	bot.add_cog(Template(bot))