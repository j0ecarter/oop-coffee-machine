# OOP Coffee Machine

A command-line coffee machine built around a small class and recipe objects. It tracks water, milk, coffee and earnings while validating each order before changing the inventory.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python coffee_machine.py
```

Use `report` to inspect the machine and `off` to stop it. Run tests with `pytest`.
