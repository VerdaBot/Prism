from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping")
	async def ping(self, ctx):
		# send the rounded latency
		await ctx.send(f"Pong! {ctx.bot.latency:.2f}ms")

def setup(bot):
	bot.add_cog(Greetings(bot))