import os
import ffmpeg
import whisper
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from _config import TOKEN


Name = ''
# Load Whisper model (you can choose smaller models for less CPU usage)
model = whisper.load_model("small")

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a voice message, and I'll transcribe it!\nPlease contact @vi8ilante for cooperation.")

# Handle voice messages
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем начальное сообщение
    status_message = await update.message.reply_text("Ждите. Идет распознавание голоса: [░░░░░░░░░░] 0%")
    
    file = await update.message.voice.get_file()
    file_path = "voice.ogg"
    
    # Download the voice message
    await file.download_to_drive(file_path)

    # Convert to WAV format for Whisper
    wav_path = "voice.wav"
    os.system(f"ffmpeg -i {file_path} -ar 16000 -ac 1 -c:a pcm_s16le {wav_path}")

    # Обновляем статус
    await status_message.edit_text("Ждите. Идет распознавание голоса: [████░░░░░░] 50%")

    # Transcribe the audio
    result = model.transcribe(wav_path)
    transcription = result["text"]

    # Обновляем статус
    await status_message.edit_text("Распознавание голоса: [██████████] 100%")

    # Send the transcription back
    await update.message.reply_text(f"Transcription: {transcription}")

    # Clean up files
    os.remove(file_path)
    os.remove(wav_path)

# Initialize the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()