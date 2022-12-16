import discord

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

