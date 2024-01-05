from gtts import gTTS

class AudioGenerator:
    @staticmethod
    def generate_audio(text, output_file='output.mp3'):
        tts = gTTS(text=text, lang='en')
        tts.save(output_file)
        return output_file