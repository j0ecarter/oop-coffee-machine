from dataclasses import dataclass

COINS = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}


@dataclass(frozen=True)
class MenuItem:
    name: str
    water: int
    milk: int
    coffee: int
    cost: float


MENU = {
    "espresso": MenuItem("espresso", 50, 0, 18, 1.50),
    "latte": MenuItem("latte", 200, 150, 24, 2.50),
    "cappuccino": MenuItem("cappuccino", 250, 100, 24, 3.00),
}


class CoffeeMachine:
    def __init__(self, water: int = 300, milk: int = 200, coffee: int = 100):
        self.resources = {"water": water, "milk": milk, "coffee": coffee}
        self.money = 0.0

    def missing_resources(self, item: MenuItem) -> list[str]:
        needed = {"water": item.water, "milk": item.milk, "coffee": item.coffee}
        return [name for name, amount in needed.items() if self.resources[name] < amount]

    def take_payment(self, counts: dict[str, int]) -> float:
        total = 0.0
        for coin, value in COINS.items():
            total += counts.get(coin, 0) * value
        return round(total, 2)

    def make(self, item: MenuItem, payment: float) -> float:
        missing = self.missing_resources(item)
        if missing:
            raise ValueError(f"Not enough {', '.join(missing)}")
        if payment < item.cost:
            raise ValueError("Not enough money")

        # use ingredients now
        self.resources["water"] -= item.water
        self.resources["milk"] -= item.milk
        self.resources["coffee"] -= item.coffee
        self.money += item.cost
        return round(payment - item.cost, 2)

    def report(self) -> str:
        return (
            f"Water: {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}g\n"
            f"Money: ${self.money:.2f}"
        )


def read_coins() -> dict[str, int]:
    counts = {}
    print("Please insert coins.")
    for coin in COINS:
        counts[coin] = int(input(f"How many {coin}? "))
    return counts


def main() -> None:
    machine = CoffeeMachine()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "off":
            break
        if choice == "report":
            print(machine.report())
            continue
        if choice not in MENU:
            print("Unknown selection.")
            continue

        item = MENU[choice]
        missing = machine.missing_resources(item)
        if missing:
            print(f"Sorry, not enough {', '.join(missing)}.")
            continue

        payment = machine.take_payment(read_coins())
        try:
            change = machine.make(item, payment)
            print(f"Here is your {choice}. Change: ${change:.2f}")
        except ValueError as exc:
            print(f"Transaction cancelled: {exc}")


if __name__ == "__main__":
    main()
