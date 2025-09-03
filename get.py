from collections import defaultdict

data = {}

with open("data.txt", "r") as file:
  contents = file.read().split("\n")

for line in contents:
  if (line == ""):
    continue
  datapoint = line.split(": ")
  data[datapoint[0]] = datapoint[1]


inverted_dict = defaultdict(list)

for key, value in data.items():
    inverted_dict[value].append(key)

while True:
  get = input()
  
  if get[0] == ".":
    print("    "+str(inverted_dict[get[1:]]))
  elif get[0] == "[":
    get = eval(get)
    for i in get:
      print(f"    {i}: "+str(inverted_dict[str(i)]))
  else:
    print("    "+data[get])