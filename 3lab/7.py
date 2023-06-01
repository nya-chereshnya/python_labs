import random


l = int(input("type array size: "))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "1", "2", "3", "4", "5", "6", "7", "?", "!", ";"]

arr = random.choices(alphabet, k=l)
print("default arr: ", arr)
print("filtred arr: ", [a for a in arr if a != ";"])
