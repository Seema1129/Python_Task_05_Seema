logs = ["Success", "Failed", "Failed", "Success", "Failed", "Success"]

successful = 0
failed = 0

for log in logs:
    if log == "Success":
        successful += 1
    else:
        failed += 1

print("Total Attempts:", len(logs))
print("Successful Logins:", successful)
print("Failed Logins:", failed)

