import collections
from random import choice
# Name tupled are basically an easy to create lightweight object types. Is a simple way to create a Class  
# with the use  Dictionary tuple struct. This type of collection support the access Key and the iteration.
# The firs argument is the type, second is the tuple that basically is the fields as attributtes. Si is possible
# access to the fields using getattr or with indexes.
# This object doesn't have methods but just have attributes so can be used like a database record
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        """Make possible use Len over an instance of this class like
        instance = FrenchDeck()
        len(instance)
        """
        return len(self.cards)

    def __getitem__(self, position):
        """Make possible access to values using indexes directly over the instance of the object class
        like: instance = FrenchDeck()
        instance[2]
        """
        return self.cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()

    number_of_cards = len(deck)
    print(number_of_cards)

    # Get the first item of Deck
    first_card_of_deck = deck[0]
    print(first_card_of_deck)

    # Get the last item of deck
    last_card_of_deck = deck[-1]
    print(last_card_of_deck)

    # picking a random item from deck
    # Python already have a function to get a random item from a sequence:
    # random.choice
    random_choice = choice(deck.cards)
    print(random_choice)

    print("\n\n\n")
    print(deck[14])
    # Wi slice from index 12 and skipping 13 positions cards.
    new_deck = deck[12::13]
    print(new_deck)

    """More about slicing:
     https://stackoverflow.com/questions/48351334/slicing-a-list-starting-from-given-index-and-jumping-stepping-it-with-some-integ#48351342
     """