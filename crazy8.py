# Camille, Divisia, 20119289
# Patrick, Lanoie, 20212654

# Completion of a program to simulate a game of Crazy Eights Countdown

import math
import random
import copy

# Implementation of a linked list data structure 
class LinkedList:
    # Components of the linked list 
    class _Node:
        def __init__(self, v, n):   # Node constructor  
            self.value = v
            self.next = n

    def __init__(self):             # LinkedList constructor 
        self._head = None
        self._size = 0

    def __str__(self):
        # EC : empty list 
        if self.isEmpty(): 
            return "[]"
        
        result = "["
        current = self._head

        while current != None:
            result += str(current.value) + ", "
            current = current.next
        
        return result[:-2] + "]"    # Slice to remove final ", "


    def __len__(self):
        return self._size

    # Return boolean True if LinkedList is empty 
    def isEmpty(self):
        return self._size == 0


    # Adds a node of value v to the beginning of the list
    def add(self, v):
        # EC : empty list  
        if self.isEmpty(): 
            self._head = self._Node(v, None)
        
        else:
            newNode = self._Node(v, self._head)
            self._head = newNode
        
        self._size += 1


    # Adds a node of value v to the end of the list
    def append(self,v):
        # EC : empty list 
        if self.isEmpty(): 
            self._head = self._Node(v, None)
        
        else:
            current = self._head

            while current.next != None:
                current = current.next

            current.next = self._Node(v, None)
        
        self._size += 1

        
    # Removes and returns value of the first node of the list
    def pop(self):
        # EC : empty list 
        if self.isEmpty():  
            return None

        nodeToPop = self._head
        self._head = nodeToPop.next

        self._size -= 1
        return nodeToPop.value


    # Returns the value of the first node of the list
    def peek(self):
        # EC : Empty list  
        if self.isEmpty():  
            return None

        return self._head.value
        

    # Removes the first node of the list with value v and return v
    def remove(self, v):
        # EC : Empty list 
        if self.isEmpty(): 
            return None
        
        current = self._head

        # EC : Match on first node 
        if current.value == v:  
            self._head = current.next
 
        # Other nodes 
        else:   
            prev = current
            current = current.next

            while current != None:
                if current.value == v:          # if value found link previous
                    prev.next = current.next    # and following nodes 
                    break
                # Incrementation 
                prev = current
                current = current.next
        
        # Found
        if current != None:
            self._size -= 1
            return current.value
        # Not found 
        else:
            return None 


# Implementation of circular linked list data structure extending LinkedList
class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        # EC : empty list 
        if self.isEmpty():
            return "[]"
        
        result = "["
        current = self._head

        for i in range (self._size):
            result += str(current.value) + ", "
            current = current.next
        
        return result[:-2] + "]"    # Slice to remove final ", "

    def __iter__(self):    
        # Yields all values in the circular linked list starting from head
        current = self._head
        for i in range(len(self)):
            yield current.value
            current = current.next


    # Moves head pointer to next node in list
    def next(self):
        self._head = self._head.next


    # Adds a node of value v to the end of the list
    def append(self, v):
        # EC : empty list 
        if self.isEmpty():
            self._head = self._Node(v, None)
            self._head.next = self._head        # Trivial circular

        else: 
            current = self._head

            for _ in range (self._size - 1): 
                current = current.next
            
            current.next = self._Node(v, self._head)    # last points to first

        self._size += 1


    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
        # EC : empty list or list size 1 or 2 = no change  
        if self._size <= 2:
            return

        # >= 3 elements in the list 
        current = self._head    
        prev2 = current         # prev2 = 2 nodes behind current

        current = current.next  
        prev = current          # prev = 1 node behind current
        
        for _ in range(self._size): 
            current = current.next      # Jump

            prev.next = prev2           # Link

            prev2 = prev                # Follow 
            prev = current              
         

    # Removes head node and returns its value
    def pop(self):
        # EC : empty list 
        if self.isEmpty(): 
            return None

        current = self._head
        nodeToPop = current

        # EC : Single node list 
        if(self._size == 1):
            self._head = None
        
        else: 
            # New head
            self._head = current.next

            # Go to last node 
            for _ in range(self._size - 1): 
                current = current.next

            # link last node with new head
            current.next = self._head    

        self._size -= 1
        return nodeToPop.value



# Representation of a card with a rank and a suit
class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}


    def __str__(self):
        return self._rank + self.suits[self._suit]


    def __eq__(self, other):
        #par defaut, __eq__ c'est ==
        
        # EC : Card compared with None is always false 
        if other == None :
            return False

        # Change rank of cards to their numerical value 
        rankNumSelf = self.rankInNum(self._rank)
        rankNumOther = self.rankInNum(other._rank)

        # Compare rank AND suit 
        return (rankNumSelf == rankNumOther) and (self._suit == other._suit)

    # Auxiliary function to convert the letter rank of a card into its 
    # numerical value 
    def rankInNum(self, rank): 
        newRank = rank
        # Changes to numerical value if a letter rank is given 
        if rank == "A":
            newRank = "1"
        elif rank == "J":
            newRank = "11" 
        elif rank == "Q":
            newRank = "12"
        elif rank == "K":
            newRank = "13"

        return newRank 



# Representation of a hand with a dictionnary of 4 linked lists, one for 
# each suit 
class Hand:
    def __init__(self):
        self.cards = {'s': LinkedList(), 'h': LinkedList(), 'd': LinkedList(), 'c': LinkedList()}


    def __str__(self):
        result = ''
        for suit in self.cards.values():
            result += str(suit)
        return result


    def __getitem__(self, item):
        return self.cards[item]


    def __len__(self):
        result = 0
        for suit in list(self.cards):
            result += len(self.cards[suit])

        return result


    def add(self, card):
        self.cards[card._suit].add(card)


    def get_most_common_suit(self):
        return max(list(self.cards), key = lambda x: len(self[x]))

    # Returns a card included in the hand according to
    # the criteria contained in *args and None if the card
    # isn't in the hand. The tests show how *args must be used.
    # Three args may be given : rank, suit and score 
    def play(self, *args):
        
        # All initialised to None 
        rank = None
        suit = None 
        card = None 
        score = None

        # Unpack *args 
        for i in args: 
            # score is only int 
            if isinstance(i,int): 
                score = i
            # suit is only one of four possibilities 
            elif i == 's' or i == 'h' or i == 'd' or i == 'c':
                suit = i
            # if it's not a score or a suit, it's a rank 
            else: 
                rank = i

        
        # Check hand to try to find the card 
        if suit != None:                        # A suit is given 
            listSuit = self.__getitem__(suit)   

            if rank != None:                    # Suit and rank given 
                card = listSuit.remove(Card(rank, suit))

            else:                               # Suit, no rank given 
                if len(listSuit) != 0:  # Check if hand has the suit 
                    card = listSuit.pop()

                    if card._rank == str(score):    # Card is a wildcard 

                        if len(listSuit) != 0:      # Check if others of suit
                            temp = listSuit.pop()       # Take second card
                            listSuit.add(card)          # Replace first card
                            card = temp
                        else: 
                            listSuit.add(card)          # Replace card
                            card = None
                            
        else:                                   # Rank, no suit given 
            for s, l in self.cards.items():
                # Check all suits in s,h,d,c order for card of given rank
                card = l.remove(Card(rank, s))

                if card == Card(rank, s): 
                    break 
        return card 



# Reprensentation of a 52 card deck (no jokers) extending LinkedList
class Deck(LinkedList):
    def __init__(self, custom=False):
        super().__init__()
        if not custom:
            # for all suits
            for i in range(4):
                # for all ranks
                for j in range(13):
                    s = list(Card.suits)[i]
                    r = ''
                    if j == 0:
                        r = 'A'
                    elif j > 0 and j < 10:
                        r = str(j+1)
                    elif j == 10:
                        r = 'J'
                    elif j== 11:
                        r = 'Q'
                    elif j == 12:
                        r = 'K'
                    self.add(Card(r,s))


    def draw(self):
        return self.pop() 


    # Simulate a riffle shuffle od the deck 
    def shuffle(self, cut_precision = 0.05):
        # Cutting the deck in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # other_deck must point the kth node in self
        # (starting at 0 of course)
        other_deck = self._head
        for _ in range(k - 1):              # Go to k-1 node 
            other_deck = other_deck.next
        
        prev = other_deck                   # prev = k-1 node
        other_deck = other_deck.next        # other_deck from kth node

        prev.next = None                    # Split

        # Merging the two decks together
        if random.uniform(0,1) < 0.5:
            #switch self._head and other_deck pointers
            temp = self._head
            self._head = other_deck
            other_deck = temp 

        current1 = self._head   
        current2 = other_deck

        # Continue until one of the end of one of the decks
        while ((current1 != None) and (current2 != None)): 

            prev1 = current1    # Node before current1
            prev2 = current2    # Node before current2 

            # Advance currents through their respective decks 
            current1 = current1.next
            current2 = current2.next

            # Link previous nodes to form the new merged list 
            prev1.next = prev2
            if current1 != None:    # EC : other deck is longer 
                prev2.next = current1



class Player():
    def __init__(self, name, strategy='naive'):
        self.name = name
        self.score = 8
        self.hand = Hand()
        self.strategy = strategy

    def __str__(self):
        return self.name

    # This function must modify the player's hand,
    # the discard pile, and the game's declared_suit 
    # attribute. No other variables must be changed.
    # The player's strategy can ONLY be based
    # on his own cards, the discard pile, and
    # the number of cards his opponents hold.
    def play(self, game):
        if(self.strategy == 'naive'):
            top_card = game.discard_pile.peek()

            cardToPlay = None

            # A draw card has been played by previous player 
            if ((top_card._rank == '2' or top_card == Card('Q', 's')) and
                game.draw_count != 0):  

                # EC : wildcard 2 is played by previous player -> Can only 
                # play a card of declared suit to avoid drawing
                if game.declared_suit != '':

                    # Try 2 of declared suit 
                    cardToPlay = self.hand.play('2', game.declared_suit)
                    
                    # Try Q of spades if declared suit is spades 
                    if cardToPlay == None and game.declared_suit == 's': 
                        cardToPlay = self.hand.play('Q','s') # Sinon dame de pique

                    # Otherwise, draw required cards and don't play
                    if cardToPlay == None: 
                        return game 

                # Normal draw card 
                else:   
                    # Try 2 
                    cardToPlay = self.hand.play('2') 
                    
                    # Try Q of spades 
                    if cardToPlay == None: 
                        cardToPlay = self.hand.play('Q','s') # Sinon dame de pique

                    # Otherwise, draw required cards and don't play 
                    if cardToPlay == None: 
                        return game 

            else: 
                suitToPlay = game.declared_suit if game.declared_suit != '' else top_card._suit

                # Try card of same suit 
                cardToPlay = self.hand.play(suitToPlay, self.score) 

                # Try card of same rank if previous card is not a wildcard
                if cardToPlay == None and game.declared_suit == '': 
                    cardToPlay = self.hand.play(top_card._rank)

                # Try wildcard 
                if cardToPlay == None :  
                    cardToPlay = self.hand.play(str(self.score), self.score)
                
                # Otherwise, draw 1 card and don't play 
                if cardToPlay == None: 
                    return game 
            
            game.discard_pile.add(cardToPlay)   # Play chosen card  

            # Declare suit of most common suit if a wildcard is played 
            if cardToPlay.rankInNum(cardToPlay._rank) == str(self.score):  
                game.declared_suit = self.hand.get_most_common_suit()

            # Reset declared suit if a wildcard is not played 
            if cardToPlay.rankInNum(cardToPlay._rank) != str(self.score): 
                game.declared_suit = ""
            
            return game

        else:
            # TO DO(?): Custom strategy (Bonus) NOT IMPLEMENTED 
            pass

class Game:
    def __init__(self):
        self.players = CircularLinkedList()

        for i in range(1,5):
            self.players.append(Player('Player '+ str(i)))

        self.deck = Deck()
        self.discard_pile = LinkedList()

        self.draw_count = 0
        self.declared_suit = ''


    def __str__(self):
        result = '--------------------------------------------------\n'
        result += 'Deck: ' + str(self.deck) + '\n'
        result += 'Declared Suit: ' + str(self.declared_suit) + ', '
        result += 'Draw Count: ' + str(self.draw_count) + ', '
        result += 'Top Card: ' + str(self.discard_pile.peek()) + '\n'
        
        for player in self.players:
            result += str(player) + ': '
            result += 'Score: ' + str(player.score) + ', '
            result += str(player.hand) + '\n'
        return result


    # Puts all cards from discard pile except the 
    # top card back into the deck in reverse order
    # and shuffles it 7 times
    def reset_deck(self):
        # EC: Beginning of game, shuffle only 
        if not self.discard_pile.isEmpty(): 
        
            # skip first card of discard pile 
            current = self.discard_pile._head.next 

            # Put cards in deck in reverse order  
            for _ in range(len(self.discard_pile) - 1):
                self.deck.append(current.value)
                self.discard_pile._size -= 1
                current = current.next
            
            # Keep only first card in discard pile 
            self.discard_pile._head.next = None 
        
        # Shuffle deck 7 times 
        for _ in range(7):
            self.deck.shuffle()


    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):

        player = self.players.peek()   

        for _ in range(num):    # draw num cards 

            card = self.deck.draw()
            
            player.hand.add(card)  

            # Check after each card if deck is empty, reset if it is 
            if len(self.deck) == 0:  
                self.reset_deck() 
            

    def start(self, debug=False):
        # Ordre dans lequel les joueurs gagnent la partie
        result = LinkedList()

        self.reset_deck()

        # Each player draws 8 cards
        for player in self.players:
            for _ in range(8):
                player.hand.add(self.deck.draw())

        self.discard_pile.add(self.deck.draw())

        transcript = open('result.txt','w',encoding='utf-8')
        if debug:
            transcript = open('result_debug.txt','w',encoding='utf-8')

        while(not self.players.isEmpty()):
            if debug:
                transcript.write(str(self))

            # player plays turn
            player = self.players.peek()

            old_top_card = self.discard_pile.peek()
            
            self = player.play(self)

            new_top_card = self.discard_pile.peek()

            # Player didn't play a card => must draw from pile
            if new_top_card == old_top_card:
                if self.draw_count != 0:    # Player draws more than 1 card
                    self.draw_from_deck(self.draw_count)

                    transcript.write(player.name + " draws " + 
                    str(self.draw_count) + " cards\n")

                    self.draw_count = 0     # Reset draw count 
                else: 
                    self.draw_from_deck(1)  # Player draws a single card 
                    transcript.write(player.name + " draws 1 card\n")

            # Player played a card
            else:   
                # Check if the played card is special     
                if new_top_card._rank == 'A':       # change order
                    self.players.reverse()

                elif new_top_card._rank == '2':     # add 2 to draw count
                    self.draw_count += 2

                elif new_top_card == Card('Q', 's'):# add 5 to draw count 
                    self.draw_count += 5
                
                # NB : Js are handled further down and wildcards are handled
                # in Players.play() method

                transcript.write(player.name + " plays " +
                str(new_top_card) + "\n")

            # Handling player change
            # Player has finished his game 
            if len(player.hand) == 0 and player.score == 1:

                # Game not over  
                result.append(player)               # Remove player that
                self.players.pop()                  # has finished

                transcript.write(player.name + " finishes in position " +
                str(len(result)) + "\n")

                # Game is over 
                if len(self.players) == 1:
                    player = self.players.peek()    # Remove final player 
                    result.append(player) 
                    self.players.pop()   

                    transcript.write(player.name + " finishes last\n")
                         
                
            # Player has not finished his game 
            else:
                # Player is out of cards to play
                if len(player.hand) == 0:
                    player.score -= 1       

                    self.draw_from_deck(player.score)   # draw new score cards   

                    transcript.write(player.name + 
                    " is out of cards to play! " + player.name + 
                    " draws " + str(player.score) + " cards\n")

                # Player has a single card left to play
                elif len(player.hand) == 1:
                    # Rules are rules : Knocking is essential 
                    transcript.write("*Knock, knock* - " + player.name + " has a single card left!\n")
                
                # Handle J if it was played by this player 
                if new_top_card._rank == 'J' and old_top_card != new_top_card:    
                    self.players.next()

                self.players.next()
        return result


if __name__ == '__main__':
    
    random.seed(420)
    game = Game()
    print(game.start(debug=True))

    # TESTS
    # LinkedList
    l = LinkedList()
    l.append('b')
    l.append('c')
    l.add('a')

    assert(str(l) == '[a, b, c]')
    assert(l.pop() == 'a')
    assert(len(l) == 2)
    assert(str(l.remove('c')) == 'c')
    assert(l.remove('d') == None)
    assert(str(l) == '[b]')
    assert(l.peek() == 'b')
    assert(l.pop() == 'b')
    assert(len(l) == 0)
    assert(l.isEmpty())

    # CircularLinkedList
    l = CircularLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    assert(str(l) == '[a, b, c]')
    l.next()
    assert(str(l) == '[b, c, a]')
    l.next()
    assert(str(l) == '[c, a, b]')
    l.next()
    assert(str(l) == '[a, b, c]')
    l.reverse()
    assert(str(l) == '[a, c, b]')
    assert(l.pop() == 'a')
    assert(str(l) == '[c, b]')

    # Card
    c1 = Card('A','s')
    c2 = Card('A','s')
    # Il est pertinent de traiter le rang 1
    # comme étant l'ace
    c3 = Card('1','s')
    assert(c1 == c2)
    assert(c1 == c3)
    assert(c3 == c2)

    # Hand
    h = Hand()
    h.add(Card('A','s'))
    h.add(Card('8','s'))
    h.add(Card('8','h'))
    h.add(Card('Q','d'))
    h.add(Card('3','d'))
    h.add(Card('3','c'))

    assert(str(h) == '[8♠, A♠][8♡][3♢, Q♢][3♣]')
    assert(str(h['d']) == '[3♢, Q♢]')
    assert(h.play('3','d') == Card('3','d'))
    assert(str(h) == '[8♠, A♠][8♡][Q♢][3♣]')
    assert(str(h.play('8')) == '8♠')
    assert(str(h.play('c')) == '3♣')
    assert(str(h) == '[A♠][8♡][Q♢][]')
    assert(h.play('d','Q') == Card('Q','d'))
    assert(h.play('1') == Card('A','s'))
    assert(h.play('J') == None)

    # Deck
    d = Deck(custom=True)
    d.append(Card('A','s'))
    d.append(Card('2','s'))
    d.append(Card('3','s'))
    d.append(Card('A','h'))
    d.append(Card('2','h'))
    d.append(Card('3','h'))

    random.seed(15)

    temp = copy.deepcopy(d)
    assert(str(temp) == '[A♠, 2♠, 3♠, A♡, 2♡, 3♡]')
    temp.shuffle()
    assert(str(temp) == '[A♠, A♡, 2♠, 2♡, 3♠, 3♡]')
    temp = copy.deepcopy(d)
    temp.shuffle()
    assert(str(temp) == '[A♡, A♠, 2♡, 2♠, 3♡, 3♠]')
    assert(d.draw() == Card('A','s'))
    
