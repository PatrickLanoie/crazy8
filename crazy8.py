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
            return "[]"
        
        # NC
        result = "["
        current = self._head

        while current != None:
            result += str(current.value) + ", "
            current = current.next
        
        return result[:-2] + "]"      # Slice pour éliminer dernière flêche, différencier de liste circulaire


    def __len__(self):
        return self._size


    def isEmpty(self):
        #TO DO
        return self._size == 0


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
            self._head = self._Node(v, None)
        
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
        if self.isEmpty(): 
            return None

        # NC
        first = self._head
        self._head = first.next

        self._size -= 1
        return first.value


    # Returns the value of the first node of the list
    def peek(self):
        #TO DO
        # EC : Liste vide  
        if self.isEmpty(): 
            return None

        # NC
        return self._head.value
        

    # Removes the first node of the list with value v and return v
    def remove(self, v):
        # TO DO

        # EC : Liste vide  
        if self.isEmpty(): 
            return None
        
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
            return None 

################# TESTS ######################################################

##############################################################################

class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        #TO DO

        # EC : liste vide
        if self._size == 0:
            return "[]"
        
        # NC
        result = "["
        current = self._head

        for i in range (self._size):
            result += str(current.value) + ", "
            current = current.next
        
        return result[:-2] + "]"

    def __iter__(self):
        #TO DO      
        # Yields all values in the circular linked list starting from head
        current = self._head
        for i in range(len(self)):
            yield current.value
            current = current.next


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
        if self.isEmpty(): 
            return None

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
        return nodeToPop.value

      
################# TESTS ######################################################


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
        
        # EC : Comparaison avec None --> always false 
        if other == None :
            return False


        # Ajuster les ranks s'ils ne sont pas sous forme numérique 
        rankNumSelf = self.checkRank(self._rank)
        rankNumOther = self.checkRank(other._rank)


        return (rankNumSelf == rankNumOther) and (self._suit == other._suit)


    def checkRank(self, rank): 
        newRank = rank
        if rank == "A":
            newRank = "1"
        elif rank == "J":
            newRank = "11" 
        elif rank == "Q":
            newRank = "12"
        elif rank == "K":
            newRank = "13"

        return newRank 


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
        # TO DO
        rank = None
        suit = None 
        card = None 
        score = None

        # Unpack les arguments et les ranges dans les variables rank ou suit 
        # selon le cas
        for i in args: 
            if isinstance(i,int): 
                score = i
            elif i == 's' or i == 'h' or i == 'd' or i == 'c':
                suit = i
            else: 
                rank = i

        
        # Cherche la carte dans la main 
        if suit != None: 
            listSuit = self.__getitem__(suit)   
            if rank != None:                    # suit et rank donné
                card = listSuit.remove(Card(rank, suit))

            else:                               # suit only
                if len(listSuit) != 0:
                    card = listSuit.pop()
                    if card._rank == str(score):     # Pas gaspiller frime 
                        if len(listSuit) != 0:  # S'il y a une autre carte de cette suite 
                            temp = listSuit.pop()   # Pige la deuxième
                            listSuit.add(card)      # Replace la première 
                            card = temp
                        else: 
                            listSuit.add(card)      # Replace la carte 
                            card = None
                            
        else:                                   # rank only
            for s, l in self.cards.items():

                card = l.remove(Card(rank, s))

                if card == Card(rank, s): 
                    break 
        return card 

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
        return self.pop()       # retourne un node 


    def shuffle(self, cut_precision = 0.05):
        # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # other_deck must point the kth node in self
        # (starting at 0 of course)
        # other_deck = #TO DO
        other_deck = self._head
        for _ in range(k - 1):              # Se rendre au node avant k
            other_deck = other_deck.next
        
        prev = other_deck                   # Node k-1
        other_deck = other_deck.next        # Node k
        prev.next = None                    # Sépare la liste

        #TO DO: seperate both lists


        # Merging the two decks together
        if random.uniform(0,1) < 0.5:
            #switch self._head and other_deck pointers
            temp = self._head
            self._head = other_deck
            other_deck = temp 

        current1 = self._head
        current2 = other_deck

        # Tant que les 2 listes n'ont pas été parcourues
        while ((current1 != None) or (current2 != None)): 

            prev1 = current1    # Node précédent liste 1
            prev2 = current2    # Node précédent liste 2

            # Inc les currents si pas à la fin de la liste
            if current1 != None:
                current1 = current1.next
            if current2 != None: 
                current2 = current2.next

            # EC : Premier node après fin liste 1    
            if current2 == None and prev2 == None:
                prev1.next = current1
            # EC : Nodes suivants après fin liste 1 
            elif current1 == None and prev1 != None:
                prev1.next = prev2
            # EC : Fin liste 2 
            elif current1 == None:
                prev2.next = current2
            # Cas de base 
            else:
                prev1.next = prev2
                prev2.next = current1



############### TESTS ###############


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
            #print(self.hand)

            #TO DO

            # PL VERSION
            cardToPlay = None

            # Forcé de piger des cartes 
            if ((top_card._rank == '2' or top_card == Card('Q', 's')) and
                game.draw_count != 0): # EC : 2 sur le discard pile, mais pas de pige  

                # EC : 2 frimé = pige automatiquement 
                if game.declared_suit != '':
                    #print(self.name + " draws " + str(game.draw_count)) 
                    return game

                cardToPlay = self.hand.play('2') # Joue un 2 si on en a un
                
                if cardToPlay == None: 
                    cardToPlay = self.hand.play('Q','s', self.score) # Sinon dame de pique

                if cardToPlay == None:  # Sinon, pige
                    #print(self.name + " draws " + str(game.draw_count)) 
                    return game 
            else: 
                suitToPlay = game.declared_suit if game.declared_suit != '' else top_card._suit
                cardToPlay = self.hand.play(suitToPlay, self.score) # Jouer carte meme suit

                if cardToPlay == None and game.declared_suit == '': # Sinon, jouer meme rang si pas frime  
                    cardToPlay = self.hand.play(top_card._rank)

                if cardToPlay == None : # Sinon, jouer une frime + change suit 
                    cardToPlay = self.hand.play(str(self.score), self.score)
                
                if cardToPlay == None: # Sinon pige
                    #print(self.name + " draws 1 card" ) 
                    return game 
            
            game.discard_pile.add(cardToPlay)   # Jouer la carte 

            if cardToPlay.checkRank(cardToPlay._rank) == str(self.score):  # Declare suit si frime 
                game.declared_suit = self.hand.get_most_common_suit()

            if cardToPlay.checkRank(cardToPlay._rank) != str(self.score):  # Reset declared suit si on ne joue pas une frime 
                game.declared_suit = ""
            
            #print(self.name + " " + str(cardToPlay)) 
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
        
        # sans itér
        #player = self.players._head
        #for _ in range(4): 
        #    result += str(player.value) + ': '
        #    result += 'Score: ' + str(player.value.score) + ', '
        #    result += str(player.value.hand) + '\n'
        #    player = player.next
        
        
        
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

        if not self.discard_pile.isEmpty():       # EC : Début de la partie. shuffle only
        
            current = self.discard_pile._head.next # Commence à la deuxième carte # NODE

            # Remet les cartes dans le deck en ordre inverse 
            for _ in range(len(self.discard_pile) - 1):
                self.deck.append(current.value)
                current = current.next
            
            # Garde seulement la première carte dans Discard pile + reset size
            self.discard_pile._head.next = None 
            self.discard_pile._size = 1
        
        # Shuffle le deck 7 fois 
        for _ in range(7):
            self.deck.shuffle()
        
        #print('reset---------------------------------------------------')


    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):
        #TO DO

        player = self.players.peek()    # Joueur qui joue 

        for _ in range(num):            # pige #num cartes 

            card = self.deck.draw()
            
            player.hand.add(card)  # ajoute une carte dans la main du joueur 

            if len(self.deck) == 0:  # Reset le deck s'il est vide 
                self.reset_deck() 
        
        return
            

    def start(self, debug=False):
        # Ordre dans lequel les joueurs gagnent la partie
        result = LinkedList()

        self.reset_deck()

        # Each player draws 8 cards
        # test sans iter
        #player = self.players._head
        #for _ in range(4): 
        #    for _ in range(8): 
        #        player.value.hand.add(self.deck.draw())
        #    print(player.value.name + str(player.value.hand))
        #    player = player.next


        for player in self.players:
            for i in range(8):
                player.hand.add(self.deck.draw())

        self.discard_pile.add(self.deck.draw())

        #print("top card = " + str(self.discard_pile))

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
                if self.draw_count != 0:    # Pige > 1 une carte
                    self.draw_from_deck(self.draw_count)
                    transcript.write(player.name + " draws " + str(self.draw_count) + " cards\n")
                    self.draw_count = 0     # Reset draw count 
                else: 
                    self.draw_from_deck(1)  # Pige une carte
                    transcript.write(player.name + " draws 1 card\n")

            

            # Player played a card
            else:   # Check si carte spéciale 
                #TO DO     
                if new_top_card._rank == 'A':  # change l'ordre de jeu 
                    self.players.reverse()

                elif new_top_card._rank == '2': # +2
                    self.draw_count += 2

                elif new_top_card == Card('Q', 's'):  # +5
                    self.draw_count += 5
                
                # J traité plus loin 

                # Frime traitée dans play 

                transcript.write(player.name + " plays " + str(new_top_card) + "\n")

                
            # Handling player change
            # Player has finished the game
            if len(player.hand) == 0 and player.score == 1:
                #TO DO

                # Partie pas terminée 
                result.append(player)
                transcript.write(player.name + " finishes in position " + str(len(result)) + "\n")
                self.players.pop()          # Élimine le jouer qui a terminé

                if len(self.players) == 1:
                    player = self.players.peek()
                    result.append(player) 
                    transcript.write(player.name + " finishes last\n")
                    self.players.pop()          # Élimine le dernier joueur 
                
            # Joueur n'a pas terminé sa partie
            else:
                # Player is out of cards to play
                if len(player.hand) == 0:           # score != 1 
                    #TO DO
                    player.score -= 1

                    self.draw_from_deck(player.score)   # Pige un nbr de carte = à son nouveau score   

                    transcript.write(player.name + " is out of cards to play! " +
                    player.name + " draws " + str(player.score) + " cards\n")

                    #print(str(player) + ' out cards. draw ' + str(player.score) + "-----------------------")

                # Player has a single card left to play
                elif len(player.hand) == 1:
                    #TO DO
                    transcript.write("*Knock, knock* - " + player.name + " has a single card left!\n")
                
                if new_top_card._rank == 'J' and old_top_card != new_top_card:    # skip next player
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
    
