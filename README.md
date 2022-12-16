# Example-of-a-Discord-music-bot
Here is an example of a Discord music bot written in Python using the discord.py library and the youtube-dl library:

``` import discord

import youtube_dl

client = discord.Client()

@client.event

async def on_ready():

    print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):

    if message.author == client.user:

        return

    if message.content.startswith('!play'):

        # Split the message into the command and the argument (the URL of the video)

        command, url = message.content.split()

        # Use youtube_dl to download the video and extract the audio

        ydl_opts = {

            'format': 'bestaudio/best',

            'outtmpl': '%(id)s',

            'postprocessors': [{

                'key': 'FFmpegExtractAudio',

                'preferredcodec': 'mp3',

                'preferredquality': '192',

            }]

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:

            ydl.download([url])

        # Get the name of the downloaded file

        audio_file = ydl.prepare_filename(ydl.extract_info(url, download=False))

        # Join the voice channel

        voice_channel = message.author.voice.channel

        voice_client = await voice_channel.connect()

        # Play the audio

        voice_client.play(discord.FFmpegPCMAudio(audio_file))

        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)

        voice_client.source.volume = 0.5

        # Wait for the audio to finish playing

        while voice_client.is_playing():

            await asyncio.sleep(1)

        # Disconnect from the voice channel

        await voice_client.disconnect()

client.run('YOUR_BOT_TOKEN_HERE')
```

This bot will listen for messages that start with !play and a URL to a YouTube video. It will download the video and play the audio in the user's voice channel. To use this bot, you will need to have a Discord account and create a bot on the Discord developer portal. You will also need to install the youtube-dl library and the FFmpeg library. You can then copy the bot's token and paste it in place of YOUR_BOT_TOKEN_HERE in the code.

This is just a simple example to get you started. You can find more information about creating Discord bots and using the discord.py library in the Discord API documentation and the discord.py documentation. You can also find more information about using youtube-dl and FFmpeg to download and play audio in the youtube-dl documentation and the FFmpeg documentation.
