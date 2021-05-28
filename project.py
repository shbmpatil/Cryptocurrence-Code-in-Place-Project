import requests
import csv


def main():
    # welcome
    print("Welcome to Shubham Patil's Cryptocurrency program!\n")
    start()


def start():
    # explanation of what this program can do
    print("This program is split into 3 different sections: ")
    # definitions of common terms used while talking about crypto
    print("A. Cryptocurrency Basics ")
    # self-explanatory: gives you price of any crypto and an overview on some popular cryptocurrencies
    print("B. Cryptocurrency Price Tracker and Coin Overview")
    # this is more of a joke than anything else
    print("C. Current Market Analysis \n")
    selection = ""
    # make sure user inputs a valid selection
    while selection != "a" and selection != "A" and selection != "b" and selection != "B" and selection != "c" and selection != "C":
        selection = input("What would you like to know? (A/B/C) ")
    print("")
    # take users the definition section
    if selection == "a" or selection == "A":
        basics()
    # take users to specific crypto info section
    if selection == "b" or selection == "B":
        crypto()
    # joke section
    if selection == "c" or selection == "C":
        trend()


def basics():
    print("I have come up with these definitions through my own research. I am not a financial advisor. \n")
    # open up  and read txt file filled with definitions I came up with
    f = open('crypto_definitions.txt', 'r', encoding="utf8")
    file_contents = f.read()
    # print txt file
    print(file_contents)
    # give user option to go back, go home, or exit program
    navigation()
    # go to beginning of function
    basics()


def crypto():
    ticker = input('What Cryptocurrency would you like to know the value (USD) and overview about? (enter ticker) ')
    # url to access live price data of any crypto through cryptocompare API
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=4e8a1766fb56558108f5cf67039771102c21d2ba866a94c5d443f1fce958e75b'
    # replace the "BTC" in the url with the ticker of any crypto
    response = requests.get(url.replace("BTC", ticker))
    # store json data
    data = response.json()
    print("")
    # print crypto price
    print(data)
    # make ticker uppercase
    ticker = ticker.upper()
    # open csv file containing info about popular cryptocurrencies
    with open('crypto_info.csv', 'r') as file:
        reader = csv.reader(file)
        # find specific row containing the info and print
        for line in reader:
            if ticker in line:
                print(line)
    print("")
    # give user option to go back, go home, or exit program
    navigation()
    # go to beginning of function
    crypto()


def trend():
    # HODL
    print("Time in the market > Timing the Market")
    # meme
    for i in range(3):
        print("")
    print("I am not a cat.")
    print("")
    # give user option to go back, go home, or exit program
    navigation()
    # go to beginning of function
    crypto()


def navigation():
    nav = ""
    #  make sure user inputs a valid selection
    while nav != "home" and nav != "Home" and nav != "back" and nav != "Back" and nav != "exit" and nav != "Exit":
        nav = input('Would you like to go back, home, or exit? (Back/Home/Exit) ')
    # direct program to start function
    if nav == "home" or nav == "Home":
        start()
    # end program
    elif nav == "exit" or nav == "Exit":
        exit()
    print("")


if __name__ == '__main__':
    main()
