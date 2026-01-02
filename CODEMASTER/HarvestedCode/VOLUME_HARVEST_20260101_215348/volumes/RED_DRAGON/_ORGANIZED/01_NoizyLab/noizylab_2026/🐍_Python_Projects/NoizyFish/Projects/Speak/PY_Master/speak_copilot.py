
mport pyttsx3

text = "This is a test of the Copilot speech system. You can replace this with any response you want spoken aloud."
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

