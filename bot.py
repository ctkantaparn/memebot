# Import necessary libraries
import discord  # Discord API wrapper
import requests  # For making HTTP requests
import json  # To parse JSON responses

# Function to fetch memes from a specified subreddit
def get_meme(subreddit='memes', count=1):
    # If only one meme is requested
    if count == 1:
        response = requests.get(f'https://meme-api.com/gimme/{subreddit}/')  # Get meme
        json_data = json.loads(response.text)  # Parse the JSON response
        return [json_data['url']]  # Return a list with one meme URL
    else:
        # If multiple memes are requested (up to 10)
        response = requests.get(f'https://meme-api.com/gimme/{subreddit}/{count}')
        json_data = json.loads(response.text)
        return [meme['url'] for meme in json_data['memes']]  # Extract URLs from the list

# Define a custom client class inheriting from discord.Client
class MyClient(discord.Client):
    
    # This function is called when the bot is ready and logged in
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # This function is called whenever a message is sent in a channel the bot can see
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return
        
        # Help command
        if message.content.startswith('$help'):
            await message.channel.send('__Command List__ \n$meme [subreddit] [number] - Sends memes')
        
        # Meme command
        if message.content.startswith('$meme'):
            parts = message.content.split()  # Split the command into parts
            sub = 'memes'  # Default subreddit
            cnt = 1        # Default meme count

            # Get subreddit if specified
            if len(parts) >= 2:
                sub = parts[1]
            # Get meme count if specified
            if len(parts) >= 3:
                try:
                    cnt = int(parts[2])  # Convert count to integer
                    cnt = max(1, min(cnt, 10))  # Limit count between 1 and 10
                except ValueError:
                    await message.channel.send("⚠️ Count must be a number.")
                    return

            # Try to fetch memes and send them
            try:
                memes = get_meme(subreddit=sub, count=cnt)
                for meme_url in memes:
                    await message.channel.send(meme_url)
            # Handle errors if API fails
            except Exception as e:
                await message.channel.send(f"❌ Error fetching meme: {e}")

# Set up intents to allow reading message content (required for on_message)
intents = discord.Intents.default()
intents.message_content = True

# Create client instance and run the bot
client = MyClient(intents=intents)
client.run('Token')  # Replace 'Token' with your bot's actual token
