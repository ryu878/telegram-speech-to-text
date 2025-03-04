# NoVoicePlzBot — Telegram Voice Message Transcriber

A playful Telegram bot that converts voice messages into text using OpenAI's Whisper model. Perfect for people who prefer reading over listening! 🛑🎙️

## 🚀 Features

- Transcribes Telegram voice messages to text

- Handles audio conversion with FFmpeg

- Supports Whisper's small model (or other sizes)

- Fully self-hosted

## 🛠️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/NoVoicePlzBot.git
cd NoVoicePlzBot
```

### Set up your environment:

```
sudo apt update
sudo apt install ffmpeg python3 python3-pip
python3 -m venv venv
source venv/bin/activate
```

or use conda:

```
conda create --name NoVoicePlzBot -c conda-forge python=3.11
conda activate NoVoicePlzBot
```

### Install Python dependencies:

```
pip install python-telegram-bot openai-whisper ffmpeg-python
```

### Create a Telegram bot:

- Message BotFather

- Use /newbot and follow the steps

- Save your bot token

### Configure the bot:

- Create a _config.py file in the project directory:

TOKEN = "your-telegram-bot-token"

### 🏁 Run the Bot

Start the bot with:

```
python bot.py
```

The bot will start polling for updates. Send a voice message to see it in action!

### ⚡ Optimizations

- Use smaller Whisper models for lightweight servers:

model = whisper.load_model("tiny")

### Run with GPU acceleration (if available):

```
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### 🧹 File Cleanup

Temporary audio files are automatically deleted after transcription.

### 📜 License

MIT License — Free to use, share, and modify!

### 🤝 Contributions

PRs and suggestions are welcome! Let’s make voice messages less annoying, one transcription at a time. 😉

### 🎯 Future Improvements

- Handle longer audio files in chunks

- Add support for multiple languages

- Reply with a funny message when people send voice notes

## Contacts

https://t.me/vi8ilante

## VPS for bots and scripts
I prefer using DigitalOcean.
  
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
  
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
