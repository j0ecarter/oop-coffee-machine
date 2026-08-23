import pytest

from coffee_machine import MENU, CoffeeMachine


def test_payment_total():
    machine = CoffeeMachine()
    assert machine.take_payment({"quarters": 8, "dimes": 1}) == 2.10


def test_make_drink_uses_resources_and_returns_change():
    machine = CoffeeMachine()
    change = machine.make(MENU["latte"], 3.00)
    assert change == 0.50
    assert machine.resources == {"water": 100, "milk": 50, "coffee": 76}
    assert machine.money == 2.50


def test_low_payment_does_not_change_machine():
    machine = CoffeeMachine()
    before = machine.resources.copy()
    with pytest.raises(ValueError, match="money"):
        machine.make(MENU["espresso"], 1.00)
    assert machine.resources == before


def test_missing_resource_is_reported():
    machine = CoffeeMachine(water=20)
    assert machine.missing_resources(MENU["espresso"]) == ["water"]
