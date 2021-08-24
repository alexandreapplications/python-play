# import sys
# sys.path.append("/foo")
import mod_show
from mod_show import showText


def main():
    mod_show.showText("Alexandre")
    showText("Alexandre")


if __name__ == "__main__":
    main()
