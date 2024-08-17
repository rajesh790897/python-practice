def main():
    with open("textfile.txt", "w") as myfile:
        for i in range(20):
            myfile.write("Hello, It's Rajesh...\n")


myfile = open("textfile.txt","r")
if myfile.mode == "r":
    contents= myfile.read()
    print(contents)



if __name__ == "__main__":
    main()