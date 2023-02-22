import discord
from discord import app_commands
from discord.ext import commands
from mymods import secret

Interaction=discord.Interaction
##################################################
# BOT OWNER CHECK: @app_commands.check(bot_owner)
def bot_owner(interaction):
	return int(interaction.user.id)==int(secret.bot_owner())
##################################################
##################################################
class OwnerCommands(commands.Cog):
##################################################
	def __init__(self, client: commands.Bot) -> None:
		self.client = client
		self.emb=self.client.emb
		self.msg=self.client.msg
##################################################
	
##################################################
#RESTART COMMAND
##################################################
	@app_commands.command(name="restart-bot",description="Owner only. Restarts the bot")
	@app_commands.check(bot_owner) # BOT OWNER CHECK
	async def restart(self,interaction: Interaction):
		embed=await self.client.emb.create("Restarting","Closing bot connection")
		await self.client.msg.send(interaction,embed,hide=True)
		print("----BOT RESTARTED----")
		print("########## Connection Closed ############")
		await self.client.close()
##################################################


##################################################
async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OwnerCommands(bot))