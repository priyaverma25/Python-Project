
      
      
      
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 created by Harry")

    engine = pyttsx3.init()

    while True:
        X = input("Enter what you want me to speak: ")

        if X.lower() == "q":
            break

        engine.say(X)
        engine.runAndWait()      