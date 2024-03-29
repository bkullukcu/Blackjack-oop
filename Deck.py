# -*- coding: utf-8 -*-
"""Python OOP Blackjack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ItTRbIEhCEKaNpj2jJKEW2FdaqHyMoBa
"""

import random

class Deck:

  deck = []
  colors = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
  values = ['Ace','2','3','4','5','6','7','8','9','10','Queen','King','Jack']

  def __init__(self):
    self.value = self.values
    self.color = self.colors

    for i in self.values:
      for j in self.colors:
        self.deck.append(str(i +" of "+j))
    random.shuffle(self.deck)

  def remove_card(self):
    self.deck.pop(0)

  def show(self):
    print(self.deck)

  def get_deck(self):
    return self.deck

  def get_card(self):
    return self.deck[0]
  
  def starting_hand(self):
    return list(self.deck[0:2])