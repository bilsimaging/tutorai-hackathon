import os
from gtts import gTTS

def text_to_speech_arabic(text, filename):
    tts = gTTS(text=text, lang='ar')
    filepath = os.path.join('static', filename)
    tts.save(filepath)
    return filepath
