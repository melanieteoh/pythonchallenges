dictionary = {}

with open("monsters_simple.txt", 'r') as f:
    for line in f:
        line = line.strip('\n')
        parts = line.rsplit(",")
        dictionary[parts[0]] = parts[1]

key = input("monster name?: ").capitalize()
print (dictionary[key])