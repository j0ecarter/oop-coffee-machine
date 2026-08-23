# OOP Coffee Machine

I originally completed projects from Angela Yu's 100 Days of Code course across 2021–2023. After the original files were lost during a laptop change, this project was reconstructed in 2026 with substantial AI coding assistance. The Git history represents the reconstruction and first GitHub publication, not the original course timeline.

A command-line coffee machine built around a small class and recipe objects. It tracks water, milk, coffee and earnings while validating each order before changing the inventory.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python coffee_machine.py
```

Use `report` to inspect the machine and `off` to stop it. Run tests with `pytest`.
