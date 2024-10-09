from src.ban1 import ba1
from src.bo1 import bo1
from rich.traceback import install

install(show_locals=True)


def main():
    ba1("smell")
    bo1()


if __name__ == "__main__":
    main()
