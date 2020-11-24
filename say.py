import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')  # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
engine.say('The quick brown fox jumped over the lazy dog.')

'''
for voice in voices:
  print("ID: %s" % voice.id)
  print("Name: %s" % voice.name)
  print("Age: %s" % voice.age)
  print("Gender: %s" % voice.gender)
  print("Languages Known: %s" % voice.languages)

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
'''

engine.runAndWait()