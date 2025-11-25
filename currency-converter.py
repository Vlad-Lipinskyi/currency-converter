# 1. Створити гаманець
# 2. Запитати валюту гаманця
# 3. Запитати початковий баланс
# 4. Вибрати гаманець з якого перевести
# 5. Вибрати гаманець в який перевести
# 6. Запитати суму для конвертації
# 7. Виконати конвертацію
# 8. Відняти кошти з першого гаманця
# 9. Додати кошти до другого гаманця


wallets = []

rates = {
    ("USD", "EUR"): 0.9,
    ("EUR", "USD"): 1.1,
    ("USD", "UAH"): 40,
    ("UAH", "USD"): 0.025,
    ("EUR", "UAH"): 44,
    ("UAH", "EUR"): 0.0227
}

def getExchangeRate(fromCurrency, toCurrency):
    return rates.get((fromCurrency, toCurrency))


def createWallet():
    name = input("Введіть назву гаманця: ")
    currency = input("Введіть валюту (USD, EUR, UAH): ")

    if currency not in ["USD", "EUR", "UAH"]:
        print("Невідома валюта!")
        return

    balance = int(input("Введіть початковий баланс: "))
    
    wallet = [name, currency, balance]
    wallets.append(wallet)
    
    print("Гаманець створено!")

def chooseWallet(prompt):
    print(prompt)
    for i in range(len(wallets)):
        print(str(i + 1) + ". " + wallets[i][0] + " (" + wallets[i][1] + ") – " + str(wallets[i][2]))

    index = int(input("Оберіть номер: ")) - 1
    return index

def convert():
    if len(wallets) < 2:
        print("Потрібно хоча б два гаманці!")
        return

    print()
    fromIndex = chooseWallet("З якого гаманця переводити:")
    toIndex = chooseWallet("В який гаманець переводити:")

    fromWallet = wallets[fromIndex]
    toWallet = wallets[toIndex]

    amount = int(input("Введіть суму: "))

    if fromWallet[2] < amount:
        print("Недостатньо коштів!")
        return

    rate = getExchangeRate(fromWallet[1], toWallet[1])

    if rate is None:
        print("Курс між цими валютами не існує!")
        return

    convertedAmount = amount * rate

    fromWallet[2] -= amount
    toWallet[2] += convertedAmount

    print("Конвертація виконана!")


def showWallets():
    print("Ваші гаманці:")
    for wallet in wallets:
        print(wallet[0] + " (" + wallet[1] + ") " + str(wallet[2]))
    print()


def menu():
    while True:
        print("Меню:")
        print("1 – Створити гаманець")
        print("2 – Конвертувати валюту")
        print("3 – Показати всі гаманці")
        print("0 – Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            createWallet()
        elif choice == "2":
            convert()
        elif choice == "3":
            showWallets()
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір!")

menu()