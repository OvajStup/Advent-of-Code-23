class Hand:
   def __init__(self, cards: str, bid: int):
      self.cards = cards
      self.bid = bid

      self.type = self.getType(self.cards)


   def getType(self, cards):
      """
      5 - five-of-a-kind
      4.1 - four-of-a-kind
      4 - full house
      3.1 - three-of-a-kind
      3 - two pair
      2 - one pair
      1 - high card
      """
      card_dict = {}
      # Count appearance of each card in hand
      for card in cards:
         if card in card_dict:
            card_dict[card] += 1
         else:
            card_dict[card] = 1
      
      if part == 2:
         # Account for "Joker" cards instead of Jacks
         if 'J' in card_dict:
            joker = card_dict.pop('J')
            
            # Account for "JJJJJ" case
            if len(card_dict) == 0:
               return 5

            # Find most prevalent card and convert jokers to that card 
            max_card = 0
            for card in card_dict.keys():
               if max_card == 0:
                  max_card = card
               elif card_dict[card] > card_dict[max_card]:
                  max_card = card

            card_dict[max_card] += joker

      # Find hand type based on repeating cards
      card_dict_values = card_dict.values()
      
      # Three-of-a-kind / Two pair
      if len(card_dict) == 3:
         if 3 in card_dict_values:
            return 3.1
         else:
            return 3
         
      # Four-of-a-kind / Full house
      elif len(card_dict) == 2:
         if 3 in card_dict_values and 2 in card_dict_values:
            return 4
         else:
            return 4.1
      
      # Other cases
      else:
         return 6 - len(card_dict)
      

   def getCardValue(self, card: str):
      """
      Return value of given individual card.
      """
      if part == 1:

         # Find value of picture cards
         possible_cards = ['A', 'K', 'Q', 'J', 'T']
         if card in possible_cards:
            return 14 - possible_cards.index(card)
         
         # Return own value of number cards
         else:
            return int(card)
      
      elif part == 2:

         # Jacks are now Jokers
         possible_cards = ['A', 'K', 'Q', 'T']
         if card in possible_cards:
            return 14 - possible_cards.index(card)
         
         # Jokers are now the weakest card
         elif card == 'J':
            return 1
         
         # Return own value of number cards
         else:
            return int(card)


   # Special methods for rich comparisons
   def __eq__(self, Hand2):
      if self.cards == Hand2.cards and self.type == Hand2.type:
         return True
      
      else:
         return False
      

   def __gt__(self, Hand2):
      if self.type > Hand2.type:
         return True
      
      elif self.type == Hand2.type:
         for card in range(len(self.cards)):
            if self.getCardValue(self.cards[card]) > self.getCardValue(Hand2.cards[card]):
               return True
            
            elif self.getCardValue(self.cards[card]) < self.getCardValue(Hand2.cards[card]):
               return False
            
      else:
         return False
      

   def __lt__(self, Hand2):
      if self.type < Hand2.type:
         return True
      
      elif self.type == Hand2.type:
         for card in range(len(self.cards)):
            if self.getCardValue(self.cards[card]) < self.getCardValue(Hand2.cards[card]):
               return True
            
            elif self.getCardValue(self.cards[card]) > self.getCardValue(Hand2.cards[card]):
               return False
            
      else:
         return False
      

   def __le__(self, Hand2):
      if self.type <= Hand2.type:
         return True
      
      elif self.type == Hand2.type:
         for card in range(len(self.cards)):
            if self.getCardValue(self.cards[card]) <= self.getCardValue(Hand2.cards[card]):
               return True
            
            elif self.getCardValue(self.cards[card]) > self.getCardValue(Hand2.cards[card]):
               return False
            
      else:
         return False
      

   def __ge__(self, Hand2):
      if self.type >= Hand2.type:
         return True
      
      elif self.type == Hand2.type:
         for card in range(len(self.cards)):
            if self.getCardValue(self.cards[card]) >= self.getCardValue(Hand2.cards[card]):
               return True
            
            elif self.getCardValue(self.cards[card]) < self.getCardValue(Hand2.cards[card]):
               return False
            
      else:
         return False
      


def processLines(lines):
   """
   Generates list of Hand objects based on input file.
   """
   hands = []
   for line in lines:
      hand = line.strip().split(' ')
      hands.append(Hand(hand[0], int(hand[1])))
   
   return hands  


def rankHand(hands):
   """
   Ranks all hands based on their strength.
   """
   sorted_hands = sorted(hands)

   # Multiply bid by hand's rank to get its winnings
   winnings = 0
   for i in range(len(sorted_hands)):
      winnings += (i + 1) * sorted_hands[i].bid

   return winnings


def main():
   global part
   part = 2
   fin = open('input7.txt')
   lines = fin.readlines()

   hands = processLines(lines)
   winnings = rankHand(hands)

   print(winnings)



if __name__ == '__main__':
   main()      