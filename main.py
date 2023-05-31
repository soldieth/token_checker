from moralis import sol_api
API_KEY = "rNp5Wdya7ED3NAkrQ5KYJigFE2dgLUZCuG4w4XMeh4BS5kuw5dbcp8wXj4cTRHNd"


def getParams():
    with open("token_to_check.txt", 'r') as token:
        token_to_check = token.read()
    with open("wallets.txt", "r") as wallets_file:
        wallets = wallets_file.readlines()
        for i in range(len(wallets)):
            wallets[i] = wallets[i].replace("\n", "")
    return token_to_check, wallets


def check_wallet(token:str, wallets: list):
    for i in range(len(wallets)):
        params = {
            "address": f"{wallets[i]}",
            "network": "mainnet",
        }
        result = sol_api.account.get_portfolio(
            api_key=API_KEY,
            params=params,
        )
        isToken = False
        for tokens in result['tokens']:
            if tokens['mint'] == token:
                name = tokens['name']
                amount = tokens['amount']
                print(f"U have {amount} {name} in {wallets[i]}")
                isToken = True
                break
        if not isToken:
            print(f"U don't have token in {wallets[i]}")


if __name__ == '__main__':
    token, walletsToCheck = getParams()
    check_wallet(token, walletsToCheck)
    input()

