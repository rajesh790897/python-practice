def main():
    with open("text.txt", "w") as myfile:
        for i in range(20):
            myfile.write("Hello World\n")

myfile = open("text.txt","r")
if myfile.mode == "r":
    contents = myfile.read()
    print(contents)


    if __name__ == "__main__":
        main()