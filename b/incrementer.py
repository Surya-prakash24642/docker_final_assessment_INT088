
counter_file = '..\counter.txt'


with open(counter_file, 'r+') as file:
    count = int(file.read().strip())
    count += 1
    file.seek(0)
    file.write(str(count))
    file.truncate()
print(f"Incremented counter to {count}")

