def read(file_location: str):
    file = open(file_location, "r")
    content = file.read()
    print(content)
    file.close()

if __name__ == "__main__":
    print("Reading from a file...\n")
    read(file_location="Hello.txt")
    print("\n\n")