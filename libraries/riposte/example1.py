from riposte import Riposte

calculator = Riposte(prompt="calc:~$ ")

MEMORY = []


@calculator.command("add")
def add(x: int, y: int):
    result = f"{x} + {y} = {x + y}"
    MEMORY.append(result)
    calculator.success(result)


@calculator.command("multiply")
def multiply(x: int, y: int):
    result = f"{x} * {y} = {x * y}"
    MEMORY.append(result)
    calculator.success(result)


@calculator.command("memory")
def memory():
    for entry in MEMORY:
        calculator.print(entry)


calculator.run()