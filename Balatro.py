#lets make balatro
import random
import time
from collections import Counter
deck=[]
DiscardPile=[]
ReqScore=[300,800,2000]
Cjokers=["Joker","Greedy Joker","Lusty Joker","Wrathful Joker","Gluttonous Joker"]
shopjokers=[]
shopjokerprice=[]
#so no stupid parameters
class Globals:
    RemainingDeck=["2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
    deck=["2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
    NumOrder=[]
    SuitOrder=[]
    hand=[]
    JokerInv=[]
    chips=0
    mult=0
    hands=4
    discards=99#debug
    handsize=8
    money=4
    score=0
    ante=1
    Round=1
    ReqScoreValue=0
def menu():
    #home screen thingy
    print("Welcome to balatro made in python!\nHope you enjoy!")
    while True:
        deckchoice=input("What deck do you want to play on?\nRED DECK\n").upper()
        if deckchoice=="RED DECK":
            Globals.discards+=1
            game()
            break
        else:
            print("Pick a valid deck choice please!\n")
def draw():
    while True:
        card=random.choice(Globals.deck)
        if card not in Globals.hand and card not in DiscardPile:
            Globals.hand.append(card)
            return card
            break
def SuitSort(HandNums):
    Globals.SuitOrder=[]
    FixedSuitSort=["2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
    SortIndex=-1
    for i in range(len(FixedSuitSort)):
        SortIndex+=1
        for i in range(len(Globals.deck)):
            if FixedSuitSort[SortIndex] in Globals.deck[i]:
                Globals.SuitOrder.append(Globals.deck[i])
    #now for the part to allow for custom cards
    ordermap={hand: index for index, hand in enumerate(Globals.SuitOrder)}
    Globals.hand.sort(key=lambda x:ordermap[x])
    #print(HandNums)
    #print(Globals.hand)
    cardnum=0
    for i in range(len(Globals.hand)):
        cardnum+=1
        print((str(cardnum))+".",Globals.hand[i])
def NumSort(HandNums):
    Globals.NumOrder=[]
    FixedNumSort=["2♥","2♦","2♣","2♠","3♥","3♦","3♣","3♠","4♥","4♦","4♣","4♠","5♥","5♦","5♣","5♠","6♥","6♦","6♣","6♠","7♥","7♦","7♣","7♠","8♥","8♦","8♣","8♠","9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠","A♥","A♦","A♣","A♠"]
    SortIndex=-1
    for i in range(len(FixedNumSort)):
        SortIndex+=1
        for i in range(len(Globals.deck)):
            if FixedNumSort[SortIndex] in Globals.deck[i]:
                Globals.NumOrder.append(Globals.deck[i])
    ordermap={hand: index for index, hand in enumerate(Globals.NumOrder)}
    Globals.hand.sort(key=lambda x:ordermap[x])
    #print(HandNums)
    #print(hand)
    cardnum=0
    for i in range(len(Globals.hand)):
        cardnum+=1
        print((str(cardnum))+".",Globals.hand[i])
def game():
    for i in range(Globals.handsize):
        playerdraw=draw()
    HandNums=[]
    HandSuits=[]
    HandValues=[]
    #split cards into suits and nums to make it easy to compare for sorting
    for i in range(len(Globals.hand)):
        if len(Globals.hand[i])==2:
            HandSuits.append(Globals.hand[i][1])
        else:
            HandSuits.append(Globals.hand[i][2])
        if len(Globals.hand[i])==2:
            HandNums.append(Globals.hand[i][0])
        else:
            HandNums.append("10")
    #print(HandNums,HandSuits)
    #print(sorted(HandNums))
    #gives each card in hand an internal value
    for i in range(len(Globals.hand)):
        if HandNums[i]=="J":
            HandValues.append("11")
        elif HandNums[i]=="Q":
            HandValues.append("12")
        elif HandNums[i]=="K":
            HandValues.append("13")
        elif HandNums[i]=="A":
            HandValues.append("14")
        else:
            HandValues.append(HandNums[i])
        HandValues.sort(key=int)
    NumSort(HandNums)
    #print(HandValues)
    HandValues=list(map(int,HandValues))
    #now we actually select the cards lol
    Globals.ReqScoreValue=ReqScore[Globals.ante-1]
    if Globals.Round % 3==2:
        Globals.ReqScoreValue*=1.5
    elif Globals.Round % 3==0:
        Globals.ReqScoreValue*=2
    print("You need "+str(Globals.ReqScoreValue)+" score to beat this round.")
    while True:
        for i in range(len(Globals.hand)):
            #print("WORK")
            #print(Globals.hand[i])
            if Globals.hand[i] in Globals.RemainingDeck:
                Globals.RemainingDeck.remove(Globals.hand[i])
                #print("TRUE")
        #print(Globals.RemainingDeck)
        #print("DEBUG len remaining cards",len(Globals.RemainingDeck))
        choice=input("Which cards are you selecting?").lower()
        if choice=="suits":
            SuitSort(HandNums)
        elif choice=="nums":
            NumSort(HandNums)
        else:
            #print(choice)
            UsingCards=choice.split(",")
            CardsUsing=[]
            CheckCards=set()
            dupes=[]
            for i in UsingCards:
                if i in CheckCards:
                    dupes.append(i)
                else:
                    CheckCards.add(i)
                #print(dupes,"dupes")
            #print("Debug check",CheckCards)
            #print("Debug using",UsingCards)
            print(UsingCards) #dont delete          
            #print(len(UsingCards),"debug len usercard")
            indexchange=0
            for i in range(len(UsingCards)):
                #print(UsingCards[indexchange])
                if 0<=indexchange<len(UsingCards) and UsingCards[i].isdigit()==True and int(UsingCards[i])<=len(Globals.hand) and int(UsingCards[i])!=0 and len(dupes)==0 and len(UsingCards)<6:
                    UsingCards[indexchange]=int(UsingCards[indexchange])
                    #our nums are +1 to what pc thinks, so take one to stop this
                    UsingCards[indexchange]-=1
                    indexchange+=1
                    CardsUsing.append(Globals.hand[int(UsingCards[i])])
                    #print(CardsUsing)
                    playable=True
                else:
                    print("No")
                    playable=False
                    break
            if playable==True:
               print(CardsUsing)
               while True:
                   use=input("Play or Discard?").upper()
                   if use=="DISCARD" or use=="D" and Globals.discards>0:
                       print("Discarding the hand")
                       Discard(CardsUsing,HandNums)
                       break
                   elif use=="PLAY" or use=="P" and Globals.hands>0:
                       print("Playing the hand")
                       Play(CardsUsing,HandNums)
                       break
                   else:
                       print("Not an action")
def death():
    epic=input("Just restart as death is a W.I.P!")
    while True:
        if epic=="!(7423890fkjl":
            print("ok")
#playing the hand function
def Play(CardsUsing,HandNums):
    CardNums=[]
    CardSuits=[]
    CardValues=[]
    #split cards into suits and nums to make it easy to compare
    for i in range(len(CardsUsing)):
        if len(CardsUsing[i])==2:
            CardSuits.append(CardsUsing[i][1])
        else:
            CardSuits.append(CardsUsing[i][2])
        if len(CardsUsing[i])==2:
            CardNums.append(CardsUsing[i][0])
        else:
            CardNums.append("10")
    #print(CardNums,CardSuits)
    #print(sorted(CardNums))
    #gives each card played an internal value
    for i in range(len(CardsUsing)):
        if CardNums[i]=="J":
            CardValues.append("11")
        elif CardNums[i]=="Q":
            CardValues.append("12")
        elif CardNums[i]=="K":
            CardValues.append("13")
        elif CardNums[i]=="A":
            CardValues.append("14")
        else:
            CardValues.append(CardNums[i])       
    #print(CardValues)
    CardValues=list(map(int,CardValues))
    #now detect which hand we are playing
    Globals.hands-=1
    print(Globals.hands,"hands left.")
    Straight=False
    Flush=False
    FullHouse=False
    HCard=True
    #print(hand)
    #check what hand it is
    sortedR=[]
    for i in range(len(CardValues)):
        sortedR.append(sorted(CardValues)[i])
    rankcounts=Counter(CardNums).values()
    #print(rankcounts)
    #print("DEBUG LEN RANKCOUNTS",len(rankcounts))
    #print("DEBUG LEN CARDUSE",len(CardsUsing))
    if len(CardsUsing)==5:
        #print("LEN IS 5???")
        if CardSuits[0]==CardSuits[1]==CardSuits[2]==CardSuits[3]==CardSuits[4]:
            Flush=True
            HCard=False
        if sortedR[0]==sortedR[1]-1 and sortedR[1]==sortedR[2]-1 and sortedR[2]==sortedR[3]-1 and sortedR[3]==sortedR[4]-1 or sortedR==[2,3,4,5,14]:
            Straight=True
            HCard=False
        if Straight==True and Flush==True:
            print("Straight Flush")
            handtype="SFlush"
        elif Straight==True and Flush==False:
            print("Straight")
            handtype="Straight"
        elif Straight==False and Flush==True:
            print("Flush")
            handtype="Flush"
        if sorted(rankcounts)==[2,3]:
            print("Full House")
            handtype="FHouse"
            HCard=False
        if sorted(rankcounts)==[1,2,2]:
            print("Two pair")
            handtype="2Pair"
            print("DEbug",CardValues)
            HCard=False
        if sorted(rankcounts)==[1,4]:
            print("Four of a kind")
            handtype="4Kind"
            HCard=False
        if sorted(rankcounts)==[1,1,3]:
            print("Three of a kind")
            handtype="3Kind"
            HCard=False
        if sorted(rankcounts)==[1,1,1,2]:
            print("Pair")
            handtype="Pair"
            HCard=False
        if HCard==True: 
            print("High Card")
            handtype="HCard"
    elif len(CardsUsing)==4:
        #print("LEN IS 4???")
        if sorted(rankcounts)==[2,2]:
            print("Two Pair")
            handtype="2Pair"
        elif sorted(rankcounts)==[4]:
            print("Four of a Kind")
            handtype="4Kind"
        elif sorted(rankcounts)==[1,3]:
            print("Three of a Kind")
            handtype="3Kind"
        elif sorted(rankcounts)==[1,1,2]:
            print("Pair")
            handtype="Pair"
        else:
            print("High Card")
            handtype="HCard"                
    elif len(CardsUsing)==3:
        #print("LEN IS 3???")
        if sorted(rankcounts)==[3]:
            print("Three of a Kind")
            handtype="3Kind"
        elif sorted(rankcounts)==[1,2]:
            print("Pair")
            handtype="Pair"
        else:
            print("High Card")
            handtype="HCard"
    elif len(CardsUsing)==2:
        #print("LEN IS 2???")
        if sorted(rankcounts)==[2]:
            print("Pair")
            handtype="Pair"
        else:
            print("High Card")
            handtype="HCard"
    else:
        #print("LEN IS 1???")
        print("High Card")
        handtype="HCard"
    highest=[0]
    #print("DEBUG HANDTYPE",handtype)
    #print("DEBUG HIGHEST",highest)
    #make sure only hands in handtype are scored in ScoredHand()
    if handtype!="HCard" and handtype!="Flush" and handtype!="Straight" and handtype!="SFlush":
        ScoredHand(CardValues)
        ScoredHandUse(CardSuits,CardNums)
    elif handtype=="HCard":
        #make high card work so only one card is scored
        for i in range(len(CardNums)):
            #print("High Card Scoring")
            if CardValues[i]>highest[0]:
                highest.remove(highest[0])
                highest.append(CardValues[i])
        CardValues=[]
        CardValues.append(highest[0])
        #print(highest)
        #print("Debug",CardValues)         
    Scoring(CardValues,handtype,CardNums,CardSuits)
    #print("Work after score?")
    for i in range(len(CardsUsing)):
        DiscardPile.append(CardsUsing[i])
    for i in range(len(CardsUsing)):
        Globals.hand.remove(DiscardPile[len(DiscardPile)-i-1])
        if DiscardPile[len(DiscardPile)-i-1] in Globals.RemainingDeck:
            Globals.RemainingDeck.remove(DiscardPile[len(DiscardPile)-i-1])
    if len(Globals.RemainingDeck)==0 and len(Globals.hand)==0:
        print("You lose")
        death()
        #will make death soon
    if len(Globals.RemainingDeck)<=0:
        print("No card in deck")
    elif 0<len(Globals.RemainingDeck)<5:
      for i in range(len(Globals.RemainingDeck)):
          draw()
    else:
        #print("DEBUG CARDUSING LEN",len(CardsUsing))
        for i in range(len(CardsUsing)):
            draw()
    NumSort(HandNums)
#use the function below so we know what cards are/are not scoring
def ScoredHand(CardValues):
    #print("Scored hand()")
    ScoredCards=[]
    CardDupes=[]
    for i in CardValues:
        if i in ScoredCards:
            CardDupes.append(i)
        else:
            ScoredCards.append(i)
    #print("DEBUG CARDDUPES",CardDupes)
    #print("DEBUG SCOREDCARDS",ScoredCards)
    for i in range(len(ScoredCards)):
        if ScoredCards[i] not in CardDupes:
            CardValues.remove(ScoredCards[i])
    #print("DEbug",CardValues)
#use the below function o extract nums and suist being used in raw external form
def ScoredHandUse(CardSuits,CardNums):
    ScoredCards=[]
    CardDupes=[]
    for i in range(len(CardNums)):
        #print(CardNums[i])
        if len(CardNums[i])==1:
            if CardNums[i] in ScoredCards:
                CardDupes.append(CardNums[i])
            else:
                ScoredCards.append(CardNums[i])
        else:
            if CardNums[i] in ScoredCards:
                CardDupes.append(CardNums[i])
            else:
                ScoredCards.append(CardNums[i])
    #print("DEBUG CARDDUPES USING",CardDupes)
    #print("DEBUG SCOREDCARDS USING",ScoredCards)
    #print("DEbug",CardValues)
    #print(CardNums)
    for i in range(len(CardNums)):
        #print(i)
        if CardNums[i-1] not in CardDupes:
            CardNums.remove(CardNums[i-1])
            CardSuits.remove(CardSuits[i-1])
            #print("HELLO")
        #else:
            #print("WHAT")
    #print(CardNums,CardSuits)
#discard function
def Discard(CardsUsing,HandNums):
    Globals.discards-=1
    print(Globals.discards,"Discard(s) Left")
    for i in range(len(CardsUsing)):
        DiscardPile.append(CardsUsing[i])
    for i in range(len(CardsUsing)):
        #print(i)
        #print(DiscardPile[0])
        #print(DiscardPile[len(DiscardPile)-i-1])
        Globals.hand.remove(DiscardPile[len(DiscardPile)-i-1])#removing played cards from hand
        #print(DiscardPile)
        #print(Globals.hand)
        #print(len(DiscardPile)+len(Globals.hand))
        if DiscardPile[len(DiscardPile)-i-1] in Globals.RemainingDeck:
            Globals.RemainingDeck.remove(DiscardPile[len(DiscardPile)-i-1])
    #print(Globals.RemainingDeck)
    #print("DEBUG len remaining cards",len(Globals.RemainingDeck))
    if len(Globals.RemainingDeck)==0 and len(Globals.hand)==0:
        print("You lose")
        death()
        #will make death soon
    if len(Globals.RemainingDeck)<=0:
        print("No card in deck")
    elif 0<len(Globals.RemainingDeck)<5:
      for i in range(len(Globals.RemainingDeck)):
          draw()
    else:
        #print("DEBUG CARDUSING LEN",len(CardsUsing))
        for i in range(len(CardsUsing)):
            draw()
        #print("DEBUG normal draw")
   # print(Globals.hand)
   # print(DiscardPile)
    NumSort(HandNums)
#end of hand joker scoring like jimbo
def EndOfHandScore():
    for i in range(len(Globals.JokerInv)):
        if Globals.JokerInv[i]=="Joker":
            Globals.mult+=4
            print("+4 mult (Joker)")
            time.sleep(0.5)
            print(Globals.chips,"X",Globals.mult)
            time.sleep(0.5)
def JokerHandScore(CardNums,CardSuits,cardnum):
    for i in range(len(Globals.JokerInv)):
        if "Lusty Joker" in Globals.JokerInv[i] and CardSuits[cardnum-1]=="♥":
            Globals.mult+=3
            print("+3 mult (Lusty Joker)")
            time.sleep(0.5)
            print(Globals.chips,"X",Globals.mult)
            time.sleep(0.5)
        elif "Gluttonous Joker" in Globals.JokerInv[i] and CardSuits[cardnum-1]=="♣":
            Globals.mult+=3
            print("+3 mult (Gluttonous Joker)")
            time.sleep(0.5)
            print(Globals.chips,"X",Globals.mult)
            time.sleep(0.5)
        elif "Wrathful Joker" in Globals.JokerInv[i] and CardSuits[cardnum-1]=="♠":
            Globals.mult+=3
            print("+3 mult (Wrathful Joker)")
            time.sleep(0.5)
            print(Globals.chips,"X",Globals.mult)
            time.sleep(0.5)
        elif "Greedy Joker" in Globals.JokerInv[i] and CardSuits[cardnum-1]=="♦":
            Globals.mult+=3
            print("+3 mult (Greedy Joker)")
            time.sleep(0.5)
            print(Globals.chips,"X",Globals.mult)
            time.sleep(0.5)
            
#main poker hand scoring
def Scoring(CardValues,handtype,CardNums,CardSuits):
    if handtype=="SFlush":
        Globals.chips=100
        Globals.mult=8
    elif handtype=="Straight":
        Globals.chips=30
        Globals.mult=4
    elif handtype=="Flush":
        Globals.chips=35
        Globals.mult=4
    elif handtype=="FHouse":
        Globals.chips=40
        Globals.mult=4
    elif handtype=="4Kind":
        Globals.chips=70
        Globals.mult=6
    elif handtype=="3Kind":
        Globals.chips=30
        Globals.mult=3
    elif handtype=="2Pair":
        Globals.chips=20
        Globals.mult=2
    elif handtype=="Pair":
        Globals.chips=10
        Globals.mult=2
    elif handtype=="HCard":
        Globals.chips=5
        Globals.mult=1
    print(Globals.chips,"X",Globals.mult)
    time.sleep(0.5)
    #print("DEBUG CARDVALUES",CardValues)
    cardnum=0
    for i in range(len(CardValues)):
        if CardValues[i]<11:
            print("Chips +",CardValues[i]," ("+str(CardNums[i])+str(CardSuits[i])+")")
            time.sleep(0.5)
            Globals.chips+=CardValues[i]
        elif 10<CardValues[i]<14:
            print("Chips + 10 ("+str(CardNums[i])+str(CardSuits[i])+")")
            time.sleep(0.5)
            Globals.chips+=10
        else:
            print("Chips + 11 ("+str(CardNums[i])+str(CardSuits[i])+")")
            time.sleep(0.5)
            Globals.chips+=11
        print(Globals.chips,"X",Globals.mult)
        time.sleep(0.5)
        cardnum+=1
        JokerHandScore(CardNums,CardSuits,cardnum)
    EndOfHandScore()
    Globals.score+=Globals.mult*Globals.chips
    if Globals.score<Globals.ReqScoreValue:
        print("Your score now is "+str(Globals.score)+" out of "+str(Globals.ReqScoreValue))
    else:
        print("You beat the round. You scored " +str(Globals.score)+" and needed "+str(Globals.ReqScoreValue)+str("."))
        if Globals.Round % 3==0:
            Globals.ante+=1
        Globals.Round+=1
        #interest(very easy)
        if Globals.money<26:
            Globals.money+=Globals.hands+(Globals.money//5)
        else:
            Globals.money+=Globals.hands+5
        print("Round "+str(Globals.Round))
        print("Ante "+str(Globals.ante))
        Globals.score=0
        Globals.hands=4
        Globals.discards=99
        shop()
#shop...
def shop():
    print("$"+str(Globals.money))
    DiscardPile=[]
    Globals.hand=[]
    Globals.RemainingDeck=[]
    for i in range(len(Globals.deck)):
        Globals.RemainingDeck.append(Globals.deck[i])
    #print(Globals.hand)
    print("Jokers in shop are:")
    for i in range(2):
        shopitemJ=(random.choice(Cjokers))
        #print(shopitemJ)
        shopjokers.append(shopitemJ)
        Cjokers.remove(shopitemJ)
    #print(Cjokers)
    for i in range(2):
        if shopjokers[i]=="Joker":
            shopjokerprice.append(2)
        else:
            shopjokerprice.append(4)
    #print(shopjokerprice)
    print("Wait i must make shop first")
    while True:
        for i in range(len(shopjokers)):
            print(str(i+1)+". "+shopjokers[i]+" $"+str(shopjokerprice[i]))
        choice=input("What do you want to do?\nBUY JOKER\nBUY PACK(WIP)\nBUY VOUCHER(WIP)\nREROLL\nLEAVE\n").lower()
        if choice=="leave":
            for i in range(len(shopjokers)):
                Cjokers.append(shopjokers[0])
                shopjokers.remove(shopjokers[0])
                shopjokerprice.remove(shopjokerprice[0])
                print(Cjokers)
            game()
            break
        elif choice=="buy joker":
            if len(shopjokers)>0:
                while True:
                    shopchoice=input("Which Joker are you buying?")
                    if shopchoice.isdigit()==False:
                        print("This is not an option")
                    elif len(shopjokers)==2 and (shopchoice=="1" or shopchoice=="2"):
                        if Globals.money>=shopjokerprice[int(shopchoice)-1]:
                            Globals.JokerInv.append(shopjokers[int(shopchoice)-1])
                            shopjokers.remove(shopjokers[int(shopchoice)-1])
                            shopjokerprice.remove(shopjokerprice[int(shopchoice)-1])
                            break
                    elif len(shopjokers)==1 and shopchoice=="1":
                        if Globals.money>=shopjokerprice[int(shopchoice)-1]:
                            Globals.JokerInv.append(shopjokers[int(shopchoice)-1])
                            shopjokers.remove(shopjokers[int(shopchoice)-1])
                            shopjokerprice.remove(shopjokerprice[int(shopchoice)-1])
                            break
            else:
                print("There are no jokers left to buy!")
        elif choice=="reroll":
            print("Rerolling the shop...")
            time.sleep(0.5)
            for i in range(len(shopjokers)):
                Cjokers.append(shopjokers[0])
                shopjokers.remove(shopjokers[0])
                shopjokerprice.remove(shopjokerprice[0])
            for i in range(2):
                shopitemJ=(random.choice(Cjokers))
                shopjokers.append(shopitemJ)
                Cjokers.remove(shopitemJ)
            for i in range(2):
                if shopjokers[i]=="Joker":
                    shopjokerprice.append(2)
                else:
                    shopjokerprice.append(4)
game()
#Globals.money=100
#shop()
#to do:
#oh no now I need to code the jokers excl. jimbo, made him now + suit jimbos
#make card display when score increase is shown (CURRENTLY WIP - card modifications, ignore until these exist)
#boss blinds + skip tags
#idk other stuff ig
