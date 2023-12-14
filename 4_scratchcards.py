def conversion(card:list):
    n1 = 0
    while n1 < len(card):
        if card[n1] == '':
            del(card[n1])
        else:
            card[n1] = int(card[n1])
            n1 += 1
            
    return card


def getCardValue(line:str):
    value = 0
    winning = line[9:].split(' | ')[0].split(' ')
    owned = line[9:].split(' | ')[1].split(' ')
    
    winning = conversion(winning)
    owned = conversion(owned)
    
    for win in winning:
        if win in owned:
            if value == 0:
                value = 1
            else:
                value *= 2
    
    return value
       

def main():
    fin = open(r'C:\Users\HP\OneDrive - fer.hr\UPRO\AoC\input_4.txt')
    
    card_sum = 0
    for line in fin.readlines():
        card_sum += getCardValue(line)
        
    print(card_sum)


if __name__ == '__main__':
    main()