import os
import csv
from datetime import date

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "expenses.csv")
CSV_FIELDS = ["date", "amount", "category", "note"]

def ensure_data_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(CSV_FILE):  # only create if missing
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()

def add_expense(amount, category, note="", d=None):
    ensure_data_file()

    if d is None:
        d = date.today().isoformat()

    row = {
        "date": d,
        "amount": f"{float(amount):.2f}",
        "category": category,
        "note": note
    }

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writerow(row)

    print("Added:", row)

def list_expenses():
    ensure_data_file()

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':10} {'Amount':8} {'Category':12} Note")
    print("-" * 60)

    total = 0.0
    for r in rows:
        amount = float(r["amount"])
        total += amount
        print(f"{r['date']:10} {amount:8.2f} {r['category'][:12]:12} {r['note']}")

    print("-" * 60)
    print(f"Total: {total:.2f} ({len(rows)} records)")

if __name__ == "__main__":
    add_expense(15.75, "Transport", "Bus ticket")
    list_expenses()
