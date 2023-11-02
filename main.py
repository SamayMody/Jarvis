import openai
import pyttsx3
import speech_recognition as sr # Library to transcribe audio to text

# Setting OpenAI API key
openai.api_key = "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"

# Initializing text-to-speech engine
enigne = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source: # Opening the audio file.
        audio = recognizer.record(source) # Recording the audio
        try:
            return recognizer.recognize_google(audio) # In-built function in sr to transcribe speech to text. The function uses the Google Cloud Speech-to-Text API.
        except:
            print("Error in audio_to_text transcribe")

def generate_response(prompt):
    response = openai.Completion.create(
        enigne="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"]["0"]["text"]

def speak_text(text):
    enigne.say(text)
    enigne.runAndWait()

def main():
    while True:
        # Say Jarvis to activate!
        print("Say 'Jarvis' to record your question....")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower == 'jarvis':
                    filename = "input.wav"
                    print("Hello I am Jarvis your personel ai assistant")







