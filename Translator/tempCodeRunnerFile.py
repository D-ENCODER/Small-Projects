speak = gTTS(text=text, lang=to_lang, slow=False)

# # Using save() method to save the translated
# # speech in capture_voice.mp3
# speak.save("captured_voice.mp3")

# # Using OS module to run the translated voice.
# playsound('captured_voice.mp3')
# os.remove('captured_voice.mp3')