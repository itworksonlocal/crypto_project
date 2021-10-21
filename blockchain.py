blockchain = [[1]]


def get_last_value():
    return blockchain[-1]


def add_value(tx_amount):
    blockchain.append([get_last_value(), tx_amount])


add_value(2)

print(blockchain)
