"""CARD"""
card = input().upper()
trump = {"A" : "ace",
         "J" : "jack",
         "Q" : "queen",
         "K" : "king",
         "2" : 2,
         "3" : 3,
         "4" : 4,
         "5" : 5,
         "6" : 6,
         "7" : 7,
         "8" : 8,
         "9" : 9,
         "1" : 10,
         "D" : "diamonds",
         "H" : "hearts",
         "S" : "spades",
         "C" : "clubs"}
print(f"{trump[card[0]]} of {trump[card[-1]]}")
