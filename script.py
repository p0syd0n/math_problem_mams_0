import string
import random
import matplotlib.pyplot as plt

# full ASCII-ish pool
symbols = list(string.ascii_lowercase)   # 26 lowercase
symbols += list(string.ascii_uppercase)  # 26 uppercase
symbols += list(string.digits)           # 10 digits
symbols += list(string.punctuation)      # ~32 punctuation
symbols += [chr(i) for i in range(128, 256)]  # extended Latin (non-ASCII)
# ~220 unique symbols

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

while length < 200:
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
