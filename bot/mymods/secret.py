import os

## 	Token can be obtained through discord developer portal
def bot_token():
	token=os.environ["TOKEN"]
##	If not using docker remove line above, 
##	uncomment line below, and add your token
	#token= "Paste bot token here"
	return token

## 	Define bot owner id for restart command (Required for owner cog)
def bot_owner():
	owner_id= os.environ["USER"]
##	If not using docker remove line above, 
##	uncomment line below, and add your user id
	#owner_id= "Paste your discord user id here"
	return int(owner_id)
	
##	Test guild is required for commands to be instantly registered upon start.  See main.py and uncomment where necessary to register global commands.
def test_guild():
	guild_id= os.environ["GUILD"]
##	If not using docker remove line above, 
##	uncomment line below, and add your guild id
	#guild_id="Paste server/guild id here"
	return int(guild_id)