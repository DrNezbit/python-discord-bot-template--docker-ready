# Python3 discord bot template (docker ready) (python3.11-slim, discord.py v2)

## This is designed as a template for creating a lightweight discord bot with or without docker
If unfamiliar with how to create a discord bot or get a token see: https://www.writebots.com/discord-bot-token/

## Setup with docker:
As easy as installing docker (if not installed already), cloning this repository and editing "secret.env" to add your own bot token, user ID, and guild/server ID for the commands to be registered to. You can also set image, stack, and container names in the "Dockerfile" and "docker-compose.yaml".  Once token and IDs are added simply run "docker compose up" (add "-d" to run in background) in the command line from the cloned directory.  Changes can be made to the bot code in the /bot directory while bot is running and upon using the /restart-bot command (usable by the user matching the user id set in .env file) or restarting the container, the changes will be loaded for speedy development.

## Setup without docker:
If you do not wish to use docker you must install discord.py in your python pip packages (if not already) and edit /bot/mymods/secret.py to include the token, owner ID, and guild/server ID before running main.py.  If not using docker, restart command closes bot script if not restarted by other means (like a bash script or service).

## Notes:
Included are a few basic commands like restart and ping along with a few to help with development for beginners.  I also included my own module with a few helper functions I use to simplify common tasks like building and sending embeds and swapping messages.  I also added a time helper for displaying users time in their own timezones.  Errors are sent to the console to view in container logs and also sent as reply to to the command which caused the error.
