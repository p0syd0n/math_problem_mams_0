import string
import random
import matplotlib.pyplot as plt

symbols = list(string.ascii_lowercase)
symbols += list(string.ascii_uppercase)
symbols += list(string.digits)
symbols += list(string.punctuation)
symbols += [chr(i) for i in range(128, 256)]
symbols += [chr(i) for i in range(0x0370, 0x03FF+1)]  # Greek
symbols += [chr(i) for i in range(0x0400, 0x04FF+1)]  # Cyrillic
symbols += [chr(i) for i in range(0x2190, 0x21FF+1)]  # Arrows
symbols += [chr(i) for i in range(0x2200, 0x22FF+1)]  # Math
symbols += [chr(i) for i in range(0x2600, 0x26FF+1)]  # Misc symbols
symbols += [chr(i) for i in range(0x2700, 0x27BF+1)]  # Dingbats

# remove duplicates, preserve order
symbols = list(dict.fromkeys(symbols))

print(f"Total unique symbols: {len(symbols)}")

length = 3

def shuffle(changeable):
    mid = (len(changeable)+1) // 2
    left_half = changeable[:mid]
    right_half = changeable[mid:]
    
    counter_inserting = 1
    for element in right_half:
        left_half.insert(counter_inserting, element)
        counter_inserting += 2
    return left_half


data = {}

while length < 1438:
    print(f"Length {length}:")
    symbols_to_choose_from = symbols.copy()
    original = []
    for i in range(length):
        element_chosen = random.choice(symbols_to_choose_from)
        original.append(element_chosen)
        symbols_to_choose_from.remove(element_chosen)

    changeable = original[:]

    attempts_to_return_to_original = 1
    changeable = shuffle(changeable)

    while (changeable != original):
        changeable = shuffle(changeable)
        attempts_to_return_to_original += 1

    print(attempts_to_return_to_original)
    data[length] = attempts_to_return_to_original  

    length += 1
  

powers_of_two = []
for i in range(100):
    powers_of_two.append(2**i)

# Write results to file
with open("data.txt", "w") as file:
    for i in sorted(data.keys()):
        file.write(f"{i}: {data[i]}\n")

# Now read them back
lengths = []
attempts = []
with open("data.txt", "r") as file:
    for line in file:
        if ":" in line:
            l, a = line.strip().split(":")
            lengths.append(int(l))
            attempts.append(int(a))

# Plot
plt.figure(figsize=(10,6))
plt.plot(lengths, attempts, marker="o")
plt.title("Attempts to Return to Original vs Length")
plt.xlabel("List Length")
plt.ylabel("Attempts to Return to Original")
plt.grid(True)
plt.savefig("graph.png")
plt.show()
