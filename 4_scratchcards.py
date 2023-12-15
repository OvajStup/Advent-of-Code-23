def conversion(card:list):
    n1 = 0
    while n1 < len(card):
        if card[n1] == '':
            del(card[n1])
        else:
            card[n1] = int(card[n1])
            n1 += 1
            
    return card


def getCardValue(line:str, part):
    value = 0
    winning = line[9:].split(' | ')[0].split(' ')
    owned = line[9:].split(' | ')[1].split(' ')
    
    winning = conversion(winning)
    owned = conversion(owned)

    if part == 1:
        for win in winning:
            if win in owned:
                if value == 0:
                    value = 1
                else:
                    value *= 2

        return value
    
    else:
        won = 0
        for win in winning:
            if win in owned:
                won += 1
        
        return 0
    
global memo
memo = {}

def cardCounting(cards, index):
    won_now = getCardValue(cards[index])
    if won_now == 0:
        return 0
    
    else:
        won = 0
        for i in range(1, won_now + 1):
            if index + i in memo:
                return memo[index + i]
            else:
                won += cardCounting(cards, index + i) + 1
                if index + 1 not in memo:
                    memo[index + i] = won
            
        return won


def main():
    fin = open(r'C:\Users\HP\OneDrive - fer.hr\UPRO\AoC\input_4.txt')
    part = 2

    if part == 1:
        card_sum = 0
        for line in fin.readlines():
            card_sum += getCardValue(line, part)

    else:
        cards = fin.readlines()
        card_sum = 0
        for i in range(len(cards)):
            won = getCardValue(cards[i])
            card_sum += cardCounting(cards, i)

        card_sum += len(cards)

    print(card_sum)



if __name__ == '__main__':
    main()