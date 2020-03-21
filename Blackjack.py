import random

class Card:
    type = ""
    suit = ""
    pointValue = 0
    isShowing = False

    def __init__(self, cardType, cardSuit):
        self.type = cardType
        self.suit = cardSuit
        self.pointValue = self.determineValue(cardType)
        self.isShowing = False

    def __str__(self):
        finalString = ""
        finalString += "Suit: " + self.suit + " Type: " + self.type
        return finalString

    def determineValue(self, cardType):
        if cardType == "A":
            return 11
        elif (cardType == "10" or cardType == "J" or cardType == "Q" or cardType == "K"):
            return 10
        else:
            if cardType.isdigit() and int(cardType) > 1 and int(cardType) < 10:
                return int(cardType)
            else:
                raise Exception('Value could not be determined as {} is not a valid card type'.format(cardType))

class Deck:

    numDecks = 0
    cards = []
    isShuffled = False

    def __init__(self, decks):
        self.numDecks = decks
        self.cards = self.generateDeck(decks)
        self.isShuffled = False

    def __str__(self):
        finalString = ""
        for i in range(len(self.cards)):
            finalString = finalString + "Card in deck: " + str(i) + " Suit: " + self.cards[i].suit + " Type: " + self.cards[i].type + " | "
        return finalString

    def generateDeck(self, numDecks):
        deck = []
        suits = ["C", "D", "H", "S"]
        types = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        for n in range(numDecks):
            for s in range(4):
                for c in range(13):
                    deck.append(Card(types[c], suits[s]))

        if len(deck) % 52 != 0:
            raise Exception('The deck contains an incorrect amount ({}) of cards'.format(len(cards)))

        else:
            return deck

    def shuffleDeck(self):
        cards = self.cards
        shuffled = []
        numCards = len(cards)

        for i in range(numCards):
            index = random.randrange(len(cards))
            shuffled.append(cards[index])
            cards.pop(index)

        if len(shuffled) != numCards:
            raise Exception("Something went wrong while shuffling and cards were lost.  There are {} cards in the deck".format(len(shuffled)))
        else:
            self.cards = shuffled.copy()


    def cutDeck(self, percent): # give the percent as a whole number, not as a decimal
        cards = self.cards
        numToCut = self.numDecks * 52 * percent / 100
        for i in range(int(numToCut)):
            cards.pop()

        self.cards = cards.copy()

    def dealCard(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card

deck = Deck(1)

class Hand:
    cards = []
    points = 0
    isBusted = False

    def __init__(self):
        self.cards = []
        self.points = self.calcPoints()
        self.isBusted = False

    def __str__(self):
        if len(cards) == 0:
            return "Empty Hand"

        finalString = "Cards: "
        for card in self.cards:
            finalString += str(card) + " "
        finalString += "Points: " + str(self.points) + " Is Busted: " + str(self.isBusted)
        return finalString

    def dealHand(self):
        self.cards.clear()
        self.cards.append(deck.dealCard())
        self.cards.append(deck.dealCard())

    def calcPoints(self):
        points = 0
        for card in self.cards:
            points += card.pointValue
        return points

    def checkBust(self):
        if self.points > 21:
            self.isBusted = True

    def hit(self):
        card = deck.dealCard()
        card.isShowing = True
        self.cards.append(card)
        self.points = self.calcPoints()
        self.checkBust()

class Dealer:

    hand
    isShowing = False
    showingPoints = 0

    def __init__(self):
        self.hand = Hand()
        self.hand.cards[-1].isShowing = True
        self.isShowing = False
        self.showingPoints = self.calcShowingPoints()

    def calcShowingPoints(self):
        points = 0
        for card in self.hand:
            if card.isShowing:
                points += card.pointValue
        return points

    def setup(self):
        self.hand.dealHand()
        self.hand[0].isShowing = True
        self.showingPoints = self.calcShowingPoints()

    def play(self):
        points = self.hand.calcPoints()
        if hard:


class Player:

    hands = []
    bet = 1 # Smallest bet allowed is 1.  Blackjack is 3/2
    runningCount = 0
    trueCount = 0

    def __init__(self):
        self.hands = []
        self.bet = 1
        self.runningCount = 0
        self.trueCount = 0

player = Hand()

print(player)

player.hit()

print(player)
