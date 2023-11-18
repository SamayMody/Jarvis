import openai
import pyttsx3
import speech_recognition as sr  # Library to transcribe audio to text
import time

# Setting OpenAI API key
openai.api_key = "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"

# Initializing text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()  # Creating an instance of the Recognizer class of the sr library
    with sr.AudioFile(filename) as source:  # Opening the audio file.
        audio = recognizer.record(source)  # Recording the audio
        try:
            return recognizer.recognize_google(audio)  # In-built function in sr to transcribe speech to text. The function uses the Google Cloud Speech-to-Text API.
        except sr.UnknownValueError:
            print("Google Cloud Speech-to-Text could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Cloud Speech-to-Text API; {e}")

def generate_response(prompt):  # Function to generate a response from ChatGpt-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        # Say Jarvis to activate!
        print("Say 'Jarvis' to record your question....")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == 'jarvis':
                    filename = "input.wav"
                    print("Hello, I am Jarvis, your personal AI assistant. Please state your question.")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 5
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                    # Generate response using GPT-3
                    response = generate_response(text)
                    print(f"Jarvis says: {response}")

                    # Converting text response to audio
                    speak_text(response)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Cloud Speech-to-Text API; {e}")
            except Exception as e:
                print("Error: {}".format(e))

if __name__ == "__main__":
    main()









