from os import X_OK


class Results:
    gamedic = {}

    def __init__(self, fileName) -> None:
        f = open(fileName, "r")
        for line in f:
            lineData = line.split(",")
            if lineData[0].isdigit():
                self.gamedic[int(lineData[0])] = {
                    "date": lineData[3],
                    "game": [int(i) for i in lineData[4:10]]
                }
        f.close()
