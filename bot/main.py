import discord,os
from discord.ext import commands
from mymods import Mycord,secret

##################################################
intents = discord.Intents.default()
##################################################
class MyClient(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix="-",intents=intents)
		self.MyCord=Mycord
		self.msg=self.MyCord.Message()
		self.emb=self.MyCord.Embed()
		self.mytime=self.MyCord.Time()
		self.get_obj=self.MyCord.Get().object
##################################################
	async def setup_hook(self):
		# This adds "cogs"" folder to bot
		if "cogs" in os.listdir("./"):
			for ext in cog_list(): await self.load_extension(ext)
		# This copies the global commands over to your guild.
		MY_GUILD = await self.get_obj(secret.test_guild()) #GUILD ID
		self.tree.copy_global_to(guild=MY_GUILD)
		await self.tree.sync(guild=MY_GUILD)
## Uncomment below to add commands globally
		#await self.tree.sync()  #Commands can take up to an hour to show
##################################################

##################################################
client = MyClient() ; tree = client.tree
##################################################

##################################################
#	ON READY
@client.event
async def on_ready():
	print(f'Logged in as {client.user} On {len(client.guilds)} servers')
	print('------')
##################################################

##################################################
#	ERRORS
@tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError) -> None:
	print(error)
	title="Error Encountered"
	desc=error
	embed=await client.emb.create(title,desc)
	await client.msg.send(interaction,embed,hide=True)
##################################################

##################################################
#	GET COGS TO ADD	
def cog_list():
	mycogs=[]
	for f in os.listdir("./cogs"):
		if f.endswith(".py"): mycogs.append(f"cogs.{f[:-3]}")
	return mycogs
##################################################

##################################################
client.run(secret.bot_token())
##################################################
