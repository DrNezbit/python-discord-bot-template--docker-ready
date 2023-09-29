import os

##################################################
## 	Token can be obtained through discord developer portal

## If not using docker paste token below
token="Paste_Here"

##################################################
## 	Define bot owner id for restart command (Required for owner cog)

## If not using docker paste your user ID below
owner_id="Paste_Here"

##################################################
##	Test guild is required for commands to be instantly registered upon start.  See main.py and uncomment where necessary to register global commands.

## If not using docker paste guild (server) ID below
guild_id="Paste_Here"

##################################################
##################################################
def bot_token():
	TOKEN=os.getenv("TOKEN",default="")
	if TOKEN=="": TOKEN=token
	return TOKEN
##################################################
def bot_owner():
	OWNER=os.getenv("OWNER",default="")
	if OWNER=="": OWNER=owner_id 
	return int(OWNER)
##################################################
def test_guild():
	GUILD=os.getenv("GUILD",default="") 
	if GUILD=="": GUILD=guild_id
	return int(GUILD)
##################################################
	