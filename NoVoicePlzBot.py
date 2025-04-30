import os
import whisper
import hashlib
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from _config import TOKEN



NAME = 'NoVoicePlzBot'
VER = '300425'
print(f' {NAME} ver {VER}')

# Load Whisper model
model = whisper.load_model("small")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a voice message, and I'll transcribe it!\nPlease contact @vi8ilante for cooperation.")


def generate_file_hash():
    """Generate a short unique hash for filenames"""
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:8]


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    file_hash = generate_file_hash()
    status_message = await update.message.reply_text("Please wait. Voice recognition in progress: [░░░░░░░░░░] 0%")
    
    try:
        # Get voice message file
        file = await update.message.voice.get_file()
        ogg_path = f"{user_id}_voice_{file_hash}.ogg"
        wav_path = f"{user_id}_voice_{file_hash}.wav"
        
        # Download the voice message
        await file.download_to_drive(ogg_path)

        # Update status
        await status_message.edit_text("Please wait. Voice recognition in progress: [████░░░░░░] 50%")

        # Convert to WAV format for Whisper
        os.system(f"ffmpeg -i {ogg_path} -ar 16000 -ac 1 -c:a pcm_s16le {wav_path}")

        # Transcribe the audio
        result = model.transcribe(wav_path)
        transcription = result["text"]

        # Update status
        await status_message.edit_text("Voice recognition progress: [██████████] 100%")

        # Send the transcription back
        await update.message.reply_text(f"Transcription: {transcription}")

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
    finally:
        # Clean up files if they exist
        for file_path in [ogg_path, wav_path]:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except:
                    pass


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    print(f' BOT {NAME} ver {VER} id rinning...')
    app.run_polling()


if __name__ == "__main__":
    main()