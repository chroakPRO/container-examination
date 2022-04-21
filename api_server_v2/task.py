import time

print("Running heavy task…")

# Emulate heavy task
for i in range(1,6):
    time.sleep(1)
    print(f"Working {20*i}%")

print("Done")
