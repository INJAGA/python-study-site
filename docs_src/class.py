# --8<-- [start:basic]


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def hello(self) -> None:
        print(f"こんにちは、私は{self.name}です！")


# --8<-- [end:basic]
