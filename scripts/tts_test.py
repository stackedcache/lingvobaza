from gtts import gTTS

# Clearer sentence
russian_text = "Сука! Сука блять!"
tts = gTTS(text=russian_text, lang='ru')
tts.save("../audio/russian_clean_test.mp3")

print("Done.")
