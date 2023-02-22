import discord,asyncio
from discord import app_commands
from discord.ext import commands

##################################################

##################################################
class BaseCommands(commands.Cog):
	def __init__(self, client: commands.Bot) -> None:
		self.client = client
		self.msg=self.client.msg
		self.emb=self.client.emb
##################################################
#PING
	@app_commands.command(name="ping",description="Shows bot ping")
	async def ping(self, interaction: discord.Interaction) -> None:
		pong=int(self.client.latency *1000)
		user=interaction.user
		title=f"/{interaction.command.name}";	desc="Checking ping..."
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
		await asyncio.sleep(1.5)
		desc=f"Pong: {pong}ms"
		embed=await self.emb.create(title,desc,footer=f"{user} has been ponged")
		await self.msg.swap(interaction,embed)

##################################################
async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(BaseCommands(bot))
##################################################
