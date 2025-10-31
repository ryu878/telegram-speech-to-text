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


### 🎯 Future Improvements

- Handle longer audio files in chunks

- Add support for multiple languages

- Reply with a funny message when people send voice notes


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📞 Contact Me

I develop trading bots of any complexity, dashboards, and indicators for crypto exchanges, forex, and stocks. 🚀

To contact me, please send a message:

*   **Telegram:** [https://t.me/ryu8777](https://t.me/ryu8777) ✈️
*   **Discord:** [https://discord.gg/zSw58e9Uvf](https://discord.gg/zSw58e9Uvf) 🤝

***

## 🤝 Become My Crypto Partner

Start your trading journey on Bybit! Join using my referral link below:

**Join Bybit:** [https://www.bybit.com/invite?ref=P11NJW](https://www.bybit.com/invite?ref=P11NJW)

***

## 🖥️ VPS for Your Bots and Scripts

Keep your bots running 24/7! I prefer and recommend using **DigitalOcean**.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

**Get $200 in credit over 60 days** by using my referral link:

👉 [https://m.do.co/c/3d7f6e57bc04](https://m.do.co/c/3d7f6e57bc04)

