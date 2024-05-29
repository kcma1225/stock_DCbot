# bot.py

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define a custom bot class to manage the bot and its commands
class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")

# Define the intents required for the bot
intents = discord.Intents.all()

# Initialize the bot
bot = MyBot(command_prefix="!", intents=intents)

# Define the slash command using the existing tree
@bot.tree.command(name="hello", description="Hello, world!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, world!")

# Main function to run the bot
def main():
    try:
        # Get the token from environment variables
        token = os.getenv('DISCORD_BOT_TOKEN')
        if not token:
            raise ValueError("No token found. Please set the DISCORD_BOT_TOKEN environment variable.")
        
        bot.run(token)
    except discord.LoginFailure:
        print("Invalid token provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()