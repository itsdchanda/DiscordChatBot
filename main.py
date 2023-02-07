import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() in ['how are you?', 'how are you doing/going?', 'whats up?']:
        await message.channel.send("I'm doing great, thank you! How about you?")

    elif message.content.lower() in ['good morning', 'good evening', 'good afternoon', 'good night']:
        await message.channel.send(f"Good {message.content.lower().split()[1]}! How can I help you today?")

    elif message.content.lower() == 'tell me something':
        await message.channel.send("Something! :wink_wink:")

    elif message.content.lower() in ['ok', 'yes', "i'll do that now"]:
        await message.channel.send("Great! Let me know if there's anything else I can help with.")

    elif message.content.lower() in ['hello', 'thank you', 'goodbye']:
        await message.channel.send(f"{message.content.capitalize()}! Have a great day.")

    elif message.content.lower() in ['how can you help me?', 'what can you do?']:
        await message.channel.send("I can provide information on a variety of topics, answer questions, and assist with tasks. How may I help you today?")

    elif message.content.lower().startswith('hi, my name is'):
        name = message.content[14:]
        await message.channel.send(f"Nice to meet you, {name}! How can I help you today?")

    elif message.content.lower() == 'happy birthday!':
        await message.channel.send("Thank you! How can I assist you on your special day?")

    elif message.content.lower() in ['i have a question', 'can you help me?']:
        await message.channel.send("Of course! What's your question?")
      
    elif message.content.lower() == 'test':
        await message.channel.send("TEST Passed!")



client.run('YOUR_TOKEN_ID')
