import random
import math

numDecks = 6
blackjackReturn = 3/2


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
        elif cardType == "Cut":
            return 0
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

    def insertCutCard(self, percent): # give percent from beginning of deck
        cards = self.cards
        location = self.numDecks * 52 * percent / 100 if percent > 1 else math.floor(self.numDecks * 52 * percent)
        self.cards.insert(location, Card("Cut", "Cut"))

    def cutDeck(self, percent): # give the percent from end
        cards = self.cards
        numToCut = self.numDecks * 52 * percent / 100 if percent > 1 else math.floor(self.numDecks * 52 * percent)
        for i in range(int(numToCut)):
            cards.pop()

        self.cards = cards.copy()

    def dealCard(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card

class Hand:
    cards = []
    points = 0
    isBusted = False
    isSurrendered = False
    numAces = 0

    def __init__(self):
        self.cards = []
        self.points = self.calcPoints()
        self.isBusted = False
        self.isSurrendered = False
        self.numAces = 0

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
        self.calcAces()

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
        self.calcAces()

    def clearHand(self):
        self.cards.clear()
        self.points = 0
        self.isBusted = False
        self.numAces = 0

    def calcAces(self):
        for card in self.cards:
            if card.type == "A":
                self.numAces += 1

class Dealer:

    hand = None
    isShowing = False
    showingPoints = 0

    def __init__(self):
        self.hand = Hand()

    def calcShowingPoints(self):
        points = 0
        for card in self.hand.cards:
            if card.isShowing:
                points += card.pointValue
        return points

    def setup(self):
        self.hand.dealHand()
        self.hand.cards[0].isShowing = True
        self.showingPoints = self.calcShowingPoints()

    def play(self):
        points = self.hand.calcPoints()
        while points < 17:
            self.hand.hit()
            points = self.hand.calcPoints()

        return points

class Player:

    hands = []
    bets = [] # Smallest bet allowed is 1.  Blackjack is 3/2

    def __init__(self):
        self.hands = [Hand(),]
        self.bets = [1,]

    def setup(self, betAmount):
        for i in range(len(self.hands)):
            hands[i].dealHand()
            bets[i] = betAmount

    def double(self, index):
        self.hands[index].hit()
        self.bets[index] *= 2

        return self.hands[index].calcPoints()

    def split(self, index):
        self.hands.append(Hand())
        card = self.hands[index].cards.pop()
        self.hands[index].hit()

        self.hands[-1].cards.append(card)
        self.hands[-1].hit()

        self.bets.append(self.bets[index])

    def surrender(self, index):
        self.hands[index].isSurrendered = True

    def play(self):
        if

deck = Deck(numDecks)
dealer = Dealer()
player = Player()

class Game:
    runningCount = 0
    trueCount = 0
    winnings = 0
    deck = None
    dealer = None
    Player = None

    def __init__(self, decks):
        self.runningCount = 0
        self.trueCount = 0
        self.winnings = 0
        self.deck = Deck(decks)
        self.dealer = Dealer()
        self.Player()

    def playRound(self):
        if self.trueCount < 1:
            self.player.setup(1)
        elif self.trueCount >= 1 and self.trueCount < 2:
            self.player.setup(2)
        elif self.trueCount >= 2 and self.trueCount < 3:
            self.player.setup(3)
        elif self.trueCount >= 3 and self.trueCount < 4:
            self.player.setup(5)
        elif self.trueCount >= 4 and self.trueCount < 5:
            self.player.setup(10)
        else:
            self.player.setup(12)

        dealer.setup()

        player.play()

        dealer.play()

        for hand, bet in zip(self.player.hands, self.player.bets):
            if hand.isSurrendered:
                self.winnings -= bet/2
            elif hand.isBusted:
                self.winnings -= bet
            elif not self.dealer.hand.isBusted:
                if hand.points < self.dealer.hand.points:
                    self.winnings -= bet
                elif hand.points > self.dealer.hand.points:
                    self.winnings += bet
            else:
                self.winnings += bet

        self.calcCount()

        for i in range(len(self.player.hands)):
            self.player.hands[i].clearHand()
            self.player.bet[i] = 0

        self.dealer.hand.clearHand()

    def calcCount(self):
        for hand in self.player.hands:
            for card in hand.cards:
                if card.type == "A" or card.type == "K" or card.type == "Q" or card.type == "J" or card.type == "10":
                    self.runningCount -= 1
                elif card.type == "6" or card.type == "5" or card.type == "4" or card.type == "3" or card.type == "2":
                    self.runningCount += 1

        decks = round(self.deck.numDecks + (len(self.deck.cards) - self.deck.numDecks * 52)/52)
        self.trueCount = self.runningCount/decks
