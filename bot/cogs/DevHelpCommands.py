import discord,asyncio
from discord import app_commands
from discord.ext import commands

##################################################

##################################################
class DevHelpCommands(commands.Cog):
	def __init__(self, client: commands.Bot) -> None:
		self.client = client
		self.msg=self.client.msg
		self.emb=self.client.emb
		self.mytime=self.client.mytime
	
##################################################
# Makes a slash group		
##################################################
	dpy=app_commands.Group(name="discord-py",description="Commands to help with the discord.py api")
##################################################
# Subcommands in slash group
##################################################
	@dpy.command(name="docs",description="Discord.py API docs")
	async def dpy_index(self, interaction: discord.Interaction) -> None:
		url="https://discordpy.readthedocs.io/en/stable/index.html"
		title="ReadTheDocs";	desc=f"Index to the Discord.py docs: \n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################
	@dpy.command(name="search",description="Search the Discord.py API docs")
	async def search(self, interaction: discord.Interaction) -> None:
		url="https://discordpy.readthedocs.io/en/stable/search.html"
		title="ReadTheDocs";	desc=f"Search the docs below: \n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################
	@dpy.command(name="examples",description="Examples from the Discord.py API docs")
	async def examples(self, interaction: discord.Interaction) -> None:
		url="https://github.com/Rapptz/discord.py/tree/master/examples"
		title="ReadTheDocs";	desc=f"Examples can be found at: \n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################


##################################################
# Invite links that may be helpful
##################################################
	invites=app_commands.Group(name="invite-to",description="Invite links to servers that may be helpful")
##################################################
	@invites.command(name="python",description="Invite link to the python discord server")
	async def invite_python(self, interaction: discord.Interaction) -> None:
		url="https://discord.gg/python"
		title="Python Help";	desc=f"Invite link to the python discord server for help with python \n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################
	@invites.command(name="discord-py",description="Invite link to the discord.py discord server")
	async def invite_dpy(self, interaction: discord.Interaction) -> None:
		url="https://discord.gg/r3sSKJJ"
		title="Discord.py - ReadTheDocs";	desc=f"Invite link to the discord.py discord server for help with the discord.py api \n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################
	@invites.command(name="discord-developers",description="Invite link to the discord developers discord server")
	async def invite_ddevs(self, interaction: discord.Interaction) -> None:
		url="https://discord.gg/discord-developers"
		title="Discord Developers";	desc=f"Invite link to the discord developers discord server for help with discord from other developers\n\n {url}"
		embed=await self.emb.create(title,desc)
		await self.msg.send(interaction,embed,hide=True)
##################################################

##################################################
# Time Example
##################################################
	@app_commands.command(name="time",description="example for time class")
	async def time_example(self,interaction: discord.Interaction):
		# Send initial message so interaction does not time out
		embed=await self.emb.create("Checking time...","Please wait")
		await self.msg.send(interaction,embed=embed)
		# Get time object for now
		current_time_obj=await self.mytime.now()
		# Calculate later (0d,1h,1m from now)
		later_time=await self.mytime.calculate(current_time_obj,d=0,h=1,m=1)
		# Format current time for discord
		user_current=await self.mytime.local_timestamp(current_time_obj,ret_format="f")
		# Make list of different style outputs for later time
		time_list=[] ; formats=self.mytime.formats
		for f in formats:
			diff_format=await self.mytime.local_timestamp(later_time,ret_format=f)
			time_list.append(f"Format: `{f}` - {diff_format}")
		time_list="\n".join(time_list)
		# Build and swap embed
		title="Time Class Example"
		desc=f"Current time: {user_current} \n> Later Time (0d1h1m from current): \n{time_list}"
		footer="R format will update as time passes when channel reloads"
		embed=await self.emb.create(title,desc,footer=footer)
		await self.msg.swap(interaction,embed)
##################################################

##################################################

##################################################
async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(DevHelpCommands(bot))
##################################################
