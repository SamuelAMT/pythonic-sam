# break

"""
The break statement exits the closest loop immediately.
It stops further iterations even if the loop condition is still true.
Often used inside for or while when a condition is satisfied.
"""

for i in range(20):
    if i == 10:
        break
    print(i)

count = 0
while True:
    print(count)
    if count == 2:
        break
    count += 1

names = ["Samuel", "Andrade", "Miranda", "Tavares"]
for name in names:
    if name == "Andrade":
        print("Hello, Andrade!")
        break
