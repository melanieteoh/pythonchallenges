with open("counter.txt", "w") as new_file:
  for i in range(1,11,1):
    line_to_write = str(i)+"\n"
    new_file.write(line_to_write)
    print(line_to_write)

with open("counter.txt","a") as existing_file:
    for i in range(11,21):
        line_to_write = str(i)+"\n"
        existing_file.write(line_to_write)
        print(line_to_write)
