def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(1,5):
    print(i)