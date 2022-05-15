# Camille, Divisia, 20119289
# Patrick, Lanoie, 20212654

import math
import random
import copy



class LinkedList:
    class _Node:
        def __init__(self, v, n):   # Constructeur Node
            self.value = v
            self.next = n

    def __init__(self):             # Constructeur LinkedList
        self._head = None
        self._size = 0

    def __str__(self):
        #TO DO

        # EC : liste vide
        if self._size == 0:
            return ""
        
        # NC
        result = ""
        current = self._head

        while current != None:
            result += str(current.value) + '->'
            current = current.next
        
        return result[:-2]      # Slice pour éliminer dernière flêche, différencier de liste circulaire


    def __len__(self):
        return self._size


    def isEmpty(self):
        #TO DO
        return self._size == 0


    def emptyListCheck(self):
        if self.isEmpty():
            raise RuntimeError("Oh no! The list is empty :(")


    # Adds a node of value v to the beginning of the list
    def add(self, v):
        # TO DO

        # EC : Liste vide 
        if self._size == 0:
            self._head = self._Node(v, None)
        
        # NC
        else:
            newNode = self._Node(v, self._head)
            self._head = newNode
        
        self._size += 1


    # Adds a node of value v to the end of the list
    def append(self,v):
        #TO DO
        
        # EC : Liste vide 
        if self._size == 0:
            self.add(v)
        
        # NC
        else:
            current = self._head

            while current.next != None:
                current = current.next

            current.next = self._Node(v, None)
        
        self._size += 1

        
    # Removes and returns the first node of the list
    def pop(self):
        #TO DO
        # EC : Liste vide
        self.emptyListCheck()

        # NC
        first = self._head
        self._head = first.next

        self._size -= 1
        return first


    # Returns the value of the first node of the list
    def peek(self):
        #TO DO
        # EC : Liste vide     À voir si on veut cette erreur ou retourner 0, -1 ... 
        self.emptyListCheck()

        # NC
        return self._head.value
        

    # Removes the first node of the list with value v and return v
    def remove(self, v):
        # TO DO

        # EC : Liste vide     À voir si on veut cette erreur ou retourner 0, -1 ... 
        self.emptyListCheck()
        
        # NC
        current = self._head

        # EC : Match premier node 
        if current.value == v:  
            self._head = current.next

        # Nodes suivants 
        else:   
            prev = current
            current = current.next

            while current != None:
                if current.value == v:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
        
        # Trouvé
        if current != None:
            self._size -= 1
            return current.value
        # Pas trouvé 
        else:
            return -1  

################# TESTS ######################################################

listeV = LinkedList()
liste1 = LinkedList()
listeP = LinkedList()

# Op sur liste vide
#print(listeV)
#listeV.pop()
#listeV.peek()
#listeV.remove(1)
#listeV.append(2)
#listeV.add(1)
#print(listeV)

# Op sur liste 1 élément
#liste1.append(1)
#print(liste1.peek())
#liste1.pop()
#print(liste1)

#for i in range(10):
    #listeP.append(i)

#print(listeP)
#listeP.add(42)
#print(listeP.peek())
#listeP.pop()
#listeP.remove(0)
#listeP.remove(9)
#listeP.remove(7)
#print(listeP.remove(99))
#listeP.add(42)
#print(listeP)

##############################################################################

class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        #TO DO

        # EC : liste vide
        if self._size == 0:
            return ""
        
        # NC
        result = ""
        current = self._head

        for i in range (self._size):
            result += str(current.value) + '->'
            current = current.next
        
        return result

    def __iter__(self):
        #TO DO              ????
        pass


    # Moves head pointer to next node in list
    def next(self):
        #TO DO
        self._head = self._head.next


    # Adds a node of value v to the end of the list
    def append(self, v):
        #TO DO

        # EC : Liste vide 
        if self._size == 0:
            self._head = self._Node(v, None)
            self._head.next = self._head        # Circulaire

        # NC
        else: 
            current = self._head

            for i in range (self._size - 1): 
                current = current.next
            
            current.next = self._Node(v, self._head)

        self._size += 1


    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
        #TO DO

        # EC : Liste vide, 1 noeud ou 2 noeuds = aucun changement 
        if self._size <= 2:
            pass

        # NC 
        current = self._head    # 1er node
        prev2 = current

        current = current.next  # 2e node
        prev = current
        
        for i in range(self._size): 
            current = current.next      # Jump

            prev.next = prev2           # Link

            prev2 = prev                # Inc
            prev = current              
         

    # Removes head node and returns its value
    def pop(self):
        #TO DO
        # EC : Liste vide
        self.emptyListCheck()

        current = self._head
        nodeToPop = current
        # EC : 1 seul Node
        if(self._size == 1):
            self._head = None
        
        # NC
        else: 
            self._head = current.next

            for i in range(self._size - 1): 
                current = current.next

            current.next = nodeToPop.next   # link
            self._head = nodeToPop.next     # new head

        self._size -= 1
        return nodeToPop

      
################# TESTS ######################################################

listeV = CircularLinkedList()
liste1 = CircularLinkedList()
listeP = CircularLinkedList()

# Op sur liste vide
print(listeV)
#listeV.pop()
#listeV.peek()
#listeV.remove(1)
listeV.append(2)
#listeV.add(1)
print(listeV)

# Op sur liste 1 élément
liste1.append(1)
#print(liste1.peek())
#liste1.pop()
print(liste1)

for i in range(5):
    listeP.append(i)

print(listeP)
#listeP.add(42)
#print(listeP.peek())
#listeP.pop()
#listeP.remove(7)
#print(listeP.remove(99))
#listeP.add(42)
listeP.next()
listeP.next()
print(listeP)
#listeP.pop()
#print(listeP)
#listeP.next()
#print(listeP)
listeP.reverse()
print(listeP)

##############################################################################



class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}

    def __str__(self):
        return self._rank + self.suits[self._suit]

    def __eq__(self, other):
        #par defaut, __eq__ c'est ==
        #TO DO
        return self._rank == other._rank #car les ranks sont les memes malgre la couelru


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
    def play(self, *args):
        #TO DO
        pass

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

    def shuffle(self, cut_precision = 0.05):
        # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # other_deck must point the kth node in self
        # (starting at 0 of course)
        # other_deck = #TO DO

        #TO DO: seperate both lists

        # Merging the two decks together
        if random.uniform(0,1) < 0.5:
            pass
            #switch self._head and other_deck pointers
        
        #TO DO


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

            #TO DO

            return game

        else:
            # TO DO(?): Custom strategy (Bonus)
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
        #TO DO
        pass

    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):
        #TO DO
        pass
            

    def start(self, debug=False):
        # Ordre dans lequel les joeurs gagnent la partie
        result = LinkedList()

        self.reset_deck()

        # Each player draws 8 cards
        for player in self.players:
            for i in range(8):
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
               #TO DO
               pass
            # Player played a card
            else:
                #TO DO
                pass
            # Handling player change
            # Player has finished the game
            if len(player.hand) == 0 and player.score == 1:
                #TO DO
                pass
            else:
                # Player is out of cards to play
                if len(player.hand) == 0:
                    #TO DO
                    pass
                # Player has a single card left to play
                elif len(player.hand) == 1:
                    #TO DO
                    pass
                self.players.next()
        return result


if __name__ == '__main__':
    '''
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
    '''
