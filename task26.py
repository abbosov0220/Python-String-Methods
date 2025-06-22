username = input("GitHub username: ")
cleaned = username.replace("-", "")
print(cleaned.isalnum())
