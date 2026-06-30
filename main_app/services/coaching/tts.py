from io import BytesIO
from gtts import gTTS


class TextToSpeech:
    def speak(self, text, lang="en", tld="co.in"):
        cleaned = (text or "").strip()

        if not cleaned:
            return
        
        buffer = BytesIO()  # create file in RAM

        gTTS(text=cleaned, lang=lang, tld=tld).write_to_fp(buffer)

        buffer.seek(0)      # after writing points the cursor at the start
 
        return buffer.read()