import random

Insult = ["artless hedge- born joithead.", "craven base-court flap-dragon.", "frothy fen-sucked haggard.", "dissembling earth-vexing clack-dish.", "fawning clay-brained clotpole.", "infectious flap-mouthed boar-pig.", "droning bat-fowling apple-john."]

user = input("Enter the name of student:")
for i in range (1):
  chosen = random.choice(Insult)
  print(user, "is a", chosen)
