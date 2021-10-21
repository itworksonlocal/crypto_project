blockchain = []


def get_last_value():
    """Returns the last value of the current chain"""
    return blockchain[-1]


def add_value(tx_amount, last_tx=[1]):
    """Append new and last chain value

    Arguments:
        :tx_amount: The amount that should be added.
        :last_tx: The last chain transaction (default [1]).
    """
    blockchain.append([last_tx, tx_amount])


def get_user_input():
    """Returns the input of the user as a float."""
    return float(input("Your transaction amount: "))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_value())

print(blockchain)
