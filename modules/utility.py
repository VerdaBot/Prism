from os import name
# Standard Imports
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

# Extra Imports
from discord import Embed, Color

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Commands
	@commands.command(name="ping", help="Get the latency of the bot.")
	async def ping(self, ctx):
		await ctx.send(f"Pong! {ctx.bot.latency:.2f}ms")

	@commands.command()
	async def server(self, ctx):
		embed = Embed(title=f"{ctx.guild.name}'s Server Info", colour=Color.from_rgb(200, 200, 200))
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.add_field(name="Total Users", value=str(ctx.guild.member_count))
		embed.add_field(name="Text Channels", value=str(len(ctx.guild.text_channels)))
		embed.add_field(name="Voice Channels", value=str(len(ctx.guild.voice_channels)))
		embed.add_field(name="Total Roles", value=str(len(ctx.guild.roles)))
		await ctx.reply(embed=embed)

	# Slash Comands
	@cog_ext.cog_slash(name="ping", description="Get the latency of the bot.")
	async def slash_ping(self, ctx: SlashContext):
		await ctx.send(f"Pong! {ctx.bot.latency:.2f}ms")

def setup(bot):
	bot.add_cog(Greetings(bot))