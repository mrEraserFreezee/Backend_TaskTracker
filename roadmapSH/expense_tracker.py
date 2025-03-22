import argparse
import json
import os
from datetime import datetime

DATA_FILE = 'data.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)
def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    date = datetime.now().strftime('%Y-%m-%d')
    new_expense = {
        'id': expense_id,
        'date': date,
        'description': description,
        'amount': amount
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Pengeluaran berhasil ditambahkan (ID: {expense_id})")

def list_expenses():
    expenses = load_expenses()
    print("ID  Tanggal    Deskripsi   Jumlah")
    for expense in expenses:
        print(f"{expense['id']}   {expense['date']}  {expense['description']}        ${expense['amount']}")

def show_summary(month=None):
    expenses = load_expenses()
    total = sum(expense['amount'] for expense in expenses)
    if month:
        expenses = [expense for expense in expenses if datetime.strptime(expense['date'], '%Y-%m-%d').month == month]
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total pengeluaran untuk bulan {datetime(2024, month, 1).strftime('%B')}: ${total}")
    else:
        print(f"Total pengeluaran: ${total}")

def delete_expense(expense_id):
    expenses = load_expenses()
    updated_expenses = [expense for expense in expenses if expense['id'] != expense_id]
    if len(updated_expenses) == len(expenses):
        print("Error: ID pengeluaran tidak ditemukan.")
        return
    save_expenses(updated_expenses)
    print("Pengeluaran berhasil dihapus")


def main():
    parser = argparse.ArgumentParser(description='Aplikasi Pelacak Pengeluaran')
    subparsers = parser.add_subparsers()

    # Menambah pengeluaran
    add_parser = subparsers.add_parser('add', help='Tambah pengeluaran baru')
    add_parser.add_argument('--description', required=True, help='Deskripsi pengeluaran')
    add_parser.add_argument('--amount', type=float, required=True, help='Jumlah pengeluaran')
    add_parser.set_defaults(func=lambda args: add_expense(args.description, args.amount))

    # Menampilkan pengeluaran
    list_parser = subparsers.add_parser('list', help='Tampilkan semua pengeluaran')
    list_parser.set_defaults(func=lambda args: list_expenses())

    # Ringkasan pengeluaran
    summary_parser = subparsers.add_parser('summary', help='Tampilkan ringkasan pengeluaran')
    summary_parser.add_argument('--month', type=int, help='Bulan tertentu (1-12)')
    summary_parser.set_defaults(func=lambda args: show_summary(args.month))

    # Menghapus pengeluaran
    delete_parser = subparsers.add_parser('delete', help='Hapus pengeluaran')
    delete_parser.add_argument('--id', type=int, required=True, help='ID pengeluaran yang ingin dihapus')
    delete_parser.set_defaults(func=lambda args: delete_expense(args.id))

    # Menjalankan perintah
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
