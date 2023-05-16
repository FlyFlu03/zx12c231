from eth_account import Account


def get_private_key_from_mnemonic(mnemonic):
    # Включаем неаудируемые функции HD-кошелька
    Account.enable_unaudited_hdwallet_features()

    # Получаем приватный ключ из мнемонической фразы
    account = Account.from_mnemonic(mnemonic)
    private_key = account._private_key.hex()
    address = account.address

    return private_key, address


# Список мнемонических фраз
mnemonic_phrases = [
    "phrase",
  ]

for mnemonic_phrase in mnemonic_phrases:
    private_key, address = get_private_key_from_mnemonic(mnemonic_phrase)
    output = "{}:{}".format(address, private_key)
    print('"{}" '.format(output))
