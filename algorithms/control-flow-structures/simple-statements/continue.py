# continue

"""

"""

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

names = ["Samuel", "Andrade", "Miranda", "Tavares"]
for name in names:
    if name == "Andrade":
        print("Skipping Andrade")
        continue
    print(f"Hello, {name}!")
