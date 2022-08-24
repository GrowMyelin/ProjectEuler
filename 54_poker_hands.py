# Problem 54 - Poker Hands

with open('poker.txt') as f:
    lines = f.read().split('\n')[:-1]

testHand = ['5H','5C','6S','7S','KD'] # Pair
testHand2 = ['2H','2D','4C','4D','4S'] #Full house
testHand3 = ['3D','6D','7D','TD','QD'] # Flush
testHand4 = ['2H','2D','4C','4D','5S'] #2 pair
testHand5 = ['2H','3H','4H','5H','6H'] #Straight flush
testHand6 = ['TS','JS','QS','KS','AS'] # Royal Flush
highCards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
hands = ['High','1pair','2pair','3kind','4kind','Straight','Flush','FullHouse','StraightFlush','RoyalFlush']
def handResult(hand):
    results = {
        'High':False,
        '1pair':False,
        '2pair':False,
        '3kind':False,
        '4kind':False,
        'Straight':False,
        'Flush':False,
        'FullHouse':False,
        'StraightFlush':False,
        'RoyalFlush':False
    }
    resultDetails = {
        'High':[],
        'Pairs':[],
        '3kind':[],
        '4kind':[],
        'Straight':[],
        'Flush':[],
        'FullHouse':[],
        'StraightFlush':[],
        'RoyalFlush':[]
    }
    suitCount = {
        'H':0,
        'D':0,
        'C':0,
        'S':0
    }

    cardCount = {
        'A':0,
        'K':0,
        'Q':0,
        'J':0,
        'T':0,
        '9':0,
        '8':0,
        '7':0,
        '6':0,
        '5':0,
        '4':0,
        '3':0,
        '2':0
    }

    highCardIdx = highCards.index(hand[0][0])
    for card in hand:
        suitCount[card[1]] += 1
        cardCount[card[0]] += 1
        highCardIdx = min(highCardIdx,highCards.index(card[0])) 

    results['High'] = True
    resultDetails['High'] = highCards[highCardIdx]
    for keys,values in suitCount.items():
        if values == 5:
            results['Flush']=True
            resultDetails['Flush'] = keys
    straightCount = 0
    for keys,values in cardCount.items():
        straightCount += 1
        if values == 0:
            straightCount = 0
        if straightCount == 5:
            results['Straight'] = True
            resultDetails['Straight'].append(keys)
        if values == 2:
            resultDetails['Pairs'].append(keys)
            results['1pair']=True
        elif values == 3:
            resultDetails['3kind'].append(keys)
            results['3kind']=True
        elif values == 4:
            resultDetails['4kind'].append(keys)
            results['4kind']=True
    
    if len(resultDetails['Pairs']) > 1:
        results['2pair']=True
    if results['1pair']==True and results['3kind']==True:
        results['FullHouse']=True
        resultDetails['FullHouse'].append(resultDetails['3kind'][0])
        resultDetails['FullHouse'].append(resultDetails['Pairs'][0])
    if results['Straight']==True and results['Flush']==True:
        results['StraightFlush']=True
        resultDetails['StraightFlush'].append(resultDetails['Straight'][0])
        resultDetails['StraightFlush'].append(resultDetails['Flush'])
        if resultDetails['StraightFlush'][0]=='T':
            results['RoyalFlush']=True
            resultDetails['RoyalFlush'].append(resultDetails['Flush'][0])

    if results['RoyalFlush']:
        return ['RoyalFlush',resultDetails['RoyalFlush']]
    elif results['StraightFlush']:
        return ['StraightFlush',resultDetails['StraightFlush']]
    elif results['FullHouse']:
        return ['FullHouse',resultDetails['FullHouse']]
    elif results['Flush']:
        return ['Flush',resultDetails['Flush']]
    elif results['Straight']:
        return ['Straight',resultDetails['Straight']]
    elif results['4kind']:
        return ['4kind',resultDetails['4kind']]
    elif results['3kind']:
        return ['3kind',resultDetails['3kind']]
    elif results['2pair']:
        return ['2pair',resultDetails['Pairs']]
    elif results['1pair']:
        return ['1pair',resultDetails['Pairs'][0]]
    else:
        return ['High',resultDetails['High']]


def compareHands(hand1,hand2):
    hand1Result = handResult(hand1)
    hand1ResultIdx = hands.index(hand1Result[0])
    hand2Result = handResult(hand2)
    hand2ResultIdx = hands.index(hand2Result[0])
    if hand1ResultIdx > hand2ResultIdx:
        return 'Hand1'
    elif hand1ResultIdx < hand2ResultIdx:
        return 'Hand2'
    elif hand1ResultIdx == hand2ResultIdx:
        hand1Val = hand1Result[1]
        hand2Val = hand2Result[1]
        hand1ValIdx = highCards.index(hand1Val)
        hand2ValIdx = highCards.index(hand2Val)
        if hand1ValIdx < hand2ValIdx:
            return 'Hand1'
        elif hand1ValIdx > hand2ValIdx:
            return 'Hand2'
        else:
            print(f"1 : {hand1Result} \n 2: {hand2Result}")
            return 'Unclear'
    else:
        return 'Unclear'


print(compareHands(testHand5,testHand6))
player1 = 0
player2 = 0
unclearCount = 0
for line in lines:
    p1 = line.split(' ')[:5]
    p2 = line.split(' ')[5:]
    res = compareHands(p1,p2)
    if res == 'Hand1':
        player1 += 1
    elif res == 'Hand2':
        player2 += 1
    elif res == 'Unclear':
        unclearCount += 1

print(player1)
print(player2)
print(unclearCount)
print(player1+player2+unclearCount)
