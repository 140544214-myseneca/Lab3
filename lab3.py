def write_text_file():
    name = "Your Name"
    filename = "output.txt"
    with open(filename, "w") as f:
        f.write(name)

write_text_file()

def helloWorld():
    print('Hello World')

helloWorld()
