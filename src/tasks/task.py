class Task:
    def __init__(self, name: str, description: str, done: bool = False):
        self.name: str = name
        self.description: str = description
        self.done: bool = done
    def info(self):
        print(self.name, self.description, self.done, sep = " | ")


def main():
    name, descrp = input("Enter name: "), input("Enter descrp: ")
    t = Task(name, descrp)
    t.info()


if __name__ == "__main__":
    main()
