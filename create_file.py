questionName = ""


def createLCSol(name: str):
    words = name.split(" ")

    words = list(map(lambda x:x.lower(), words))

    fileName = "_".join(words)

    try:
        open(fileName + ".py", "x")
    except:
        print("file already exists")

if __name__ == "__main__":
    createLCSol(questionName)