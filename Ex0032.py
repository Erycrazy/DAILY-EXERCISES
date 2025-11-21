import time

for i in range(10, 0, -1):
    print(f"Os fogos vão estourar em: {i}")
    time.sleep(0.5)
    if i == 1:
        pass
print("BUMMMM!!!")