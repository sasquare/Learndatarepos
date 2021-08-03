import time
bottles = 10
while bottles > 0:
    print (bottles, "bottles of beer on the wall")
    time.sleep(5)
    print(bottles, "botles of beer ")
    time.sleep(4)
    print("Take one down, pass it arround")
    bottles = bottles-1
else:
    print (bottles, "No more Beer")
    print(" where is the booze")
        