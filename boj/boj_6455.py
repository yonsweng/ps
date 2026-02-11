from sys import stdin


def solve():
    accounts = {}

    while True:
        line = stdin.readline().strip()
        if line.startswith("000"):
            break

        account_number = line[:3]
        account_name = line[3:]
        accounts[account_number] = account_name

    transactions = {}

    while True:
        line = stdin.readline().strip()
        if line.startswith("000000"):
            break

        transaction_number = line[:3]
        account_number = line[3:6]
        amount = int(line[6:])
        if transaction_number not in transactions:
            transactions[transaction_number] = []
        transactions[transaction_number].append((account_number, amount))

    for transaction_number in transactions:
        # Calculate total amount for the transaction
        total_amount = sum(amount for _, amount in transactions[transaction_number])
        if total_amount == 0:
            continue

        print(
            f"*** Transaction {transaction_number} is out of balance ***", flush=False
        )
        for account_number, amount in transactions[transaction_number]:
            account_name = accounts.get(account_number, "Unknown Account")
            print(
                f"{account_number} {account_name:<30} {amount / 100:>10.2f}",
                flush=False,
            )
        print(
            f"{999} {'Out of Balance':<30} {(-total_amount) / 100:>10.2f}", flush=False
        )
        print(flush=False)


if __name__ == "__main__":
    solve()
