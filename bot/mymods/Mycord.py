import discord
import time,datetime


##################################################
class Get:
##################################################
	def __init__(self): self.self=self
##################################################
	async def object(self,obj_id): 
		obj=discord.Object(id=obj_id) ; return obj
##################################################
##################################################

##################################################
class Message:
##################################################
	def __init__(self): self.self=self
##################################################
	async def send(self,interaction,embed,view=None,hide=False):
		if view is None:
			await interaction.response.send_message(embed=embed,ephemeral=hide)
		else:
			await interaction.response.send_message(embed=embed,view=view,ephemeral=hide)
##################################################		
	async def swap(self,interaction,embed,view=None):
		if view is None:
			await interaction.edit_original_response(embed=embed)
		else:
			await interaction.edit_original_response(embed=embed,view=view)
##################################################
	async def add_reactions(self,interaction,emojis):
		response=await interaction.original_response()
		for emoji in emojis:
			await response.add_reaction(emoji)
##################################################
##################################################


##################################################
class Embed:
##################################################
	def __init__(self): self.self=self
##################################################
	async def create(self,title,desc,color=None,thumb=None,image=None,footer=None):
		if color is None: color=discord.Color.random()
		embed=discord.Embed(title=title,description=desc,color=color)
		if footer!=None: embed.set_footer(text=footer)
		if thumb !=None: embed.set_thumbnail(url=thumb)
		if image !=None: embed.set_image(url=image)
		return embed
##################################################
##################################################


################################################
# TIME FUNCTIONS
################################################
class Time:
################################################
	def __init__(self): self.formats=["t","T","d","D","f","F","R"]
################################################
# Get current time as datetime
	async def now(self,timestamp=False):
		now= datetime.datetime.utcnow()
		if timestamp==True: 
			now=now.replace(tzinfo=datetime.timezone.utc)
		return now
################################################
# Convert datetime object to user local time
	async def local_timestamp(self,date_time,ret_format="f"):
		try: date_time=await self.from_int(date_time)
		except: pass
		"""
Style	Example Output	Description

t		 	22:57					 Short Time
T			22:57:58		 	  Long Time
d			17/05/2016		 Short Date
D			17 May 2016	   Long Date
f 	17 May 2016 22:57    Short Date Time	(default)
F	Tuesday, 17 May 2016 22:57	Long Date Time
R			5 years ago	  	Relative Time
		"""
		if ret_format not in self.formats: return "bad format"
		local=discord.utils.format_dt(date_time,style=ret_format)
		return local
################################################
# Converts datetime object to epoch time int
	async def to_int(self,date_time):
		unix_ts=time.mktime(date_time.timetuple())
		return int(unix_ts)
################################################
# Converts epoch time int to datetime object
	async def from_int(self,int_time):
		date_time=time.ctime(int(int_time)) #Sun Jun 20 23:21:05 1993
		if "  " in date_time: date_time=date_time.replace("  "," 0")
		ret_date=datetime.datetime.strptime(date_time,"%a %b %d %H:%M:%S %Y")
		ret_date=ret_date.replace(tzinfo=datetime.timezone.utc)
		return ret_date
################################################
# Calculate time object adjustments
	async def calculate(self,start_time_obj,m=0,h=0,d=0):
		end_time=start_time_obj + datetime.timedelta(minutes=m,hours=h,days=d)
		return end_time
################################################
