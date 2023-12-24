def conversion(card:list):
    """
    Cleans up and converts a list of strings to a list of integers.
    """
    n1 = 0
    while n1 < len(card):
        # clean up empty strings
        if card[n1] == '':
            del(card[n1])
        
        else:
            card[n1] = int(card[n1])
            n1 += 1
            
    return card


def getCardValue(line:str, part):
    """
    Part 1 - Returns number of points scored by given card
    Part 2 - Returns number of cards won
    """
    # Convert input string into list of numbers
    winning = line[9:].strip().split(' | ')[0].split(' ')
    owned = line[9:].strip().split(' | ')[1].split(' ')
    
    winning = conversion(winning)
    owned = conversion(owned)

    # Number of points scored
    if part == 1:
        value = 0
        for win in winning:
            if win in owned:
                if value == 0:
                    value = 1
                else:
                    value *= 2

        return value
    
    # Number of cards won
    else:
        won = 0
        for win in winning:
            if win in owned:
                won += 1
        
        return won
    

def main():
    fin = open('input4.txt')
    part = 2

    card_sum = 0

    if part == 1:
        for line in fin.readlines():
            card_sum += getCardValue(line, part)

    else:
        cards = fin.readlines()

        # Add all won cards to a list of card counters
        won_cards = [1 for j in range(len(cards))]
        
        for i in range(len(cards)):
            won = getCardValue(cards[i], 2)
            for j in range(1, won + 1):
                won_cards[i + j] += won_cards[i]

        card_sum = sum(won_cards)

    print(card_sum)



if __name__ == '__main__':
    main()