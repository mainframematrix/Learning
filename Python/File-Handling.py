def read(file_location: str):
    """
    Reads from a file
    """
    file = open(file_location, "r")
    content = file.read()
    print(content)
    file.close()

def write(file_location: str, content: str):
    """
    Writes to a file
    """
    file= open(file_location,"w")
    file.write(content)
    print("Verification of writing the file:\n")
    file.close()
    read(file_location)
def append(file_location: str, content: str):
    """
    Appends to a file
    """
    file=open(file_location,"a")
    file.write(content)
    print("Verification of appending the file:\n")
    file.close()
    read(file_location)

if __name__ == "__main__":
    print("Reading from a file...\n")
    read(file_location="Hello.txt")
    print("\n\n")
    print("Writing to a file...\n")
    write(file_location="Hello_write.txt",content="Hi Github, I am writing to this file.\n")
    print("\n\n")
    print("Appending to a file...\n")
    append(file_location="Hello_write.txt",content="Hi Github, I am appending to this file.")
    print("\n\n")