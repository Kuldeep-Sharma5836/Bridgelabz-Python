import time
start=input("Enter the start time: ")
startTime = time.time()
end=input("Enter the end time: ")
endTime = time.time()
difference = endTime - startTime
print(f"Elapsed time: {difference} seconds")