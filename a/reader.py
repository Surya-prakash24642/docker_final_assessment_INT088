counter_file = '.\counter.txt'


with open(counter_file, 'r') as file:
    count = file.read().strip()
print(f"Current counter value: {count}")
