import random
jokes = []

class DadJokes:
    def __init__(self, Prompt, Answer):
        self.__Prompt = Prompt
        self.__Answer = Answer
    
    def PrintRandomJoke(self):
        guess = input(self.__Prompt)
        print(self.__Answer)

try: 
    with open("Dadjokes.txt") as f:
        for i in range(0, 21, 2):
            Prompt = f.readline().strip()
            Answer = f.readline().strip()
            jokes.append(DadJokes(Prompt, Answer))
except FileNotFoundError:
    print("File not found.")

choose = random.choice(jokes)
DadJokes.PrintRandomJoke(choose)
