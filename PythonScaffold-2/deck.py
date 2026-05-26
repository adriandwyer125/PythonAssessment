from card_library import CardLibrary

class Deck:
    def __init__(self, size):
        # Initialize the deck with copies of the first `size` cards from the card library
        self.__cards = [card.copy() for card in CardLibrary.ALL_CARDS[:size]]

    def deal(self):
        """Remove and return the top card. Returns None if the deck is empty."""
        if self.is_empty():
            return None
        return self.__cards.pop(0)

    def size(self):
        return len(self.__cards)

    def is_empty(self):
        return len(self.__cards) == 0

    def __str__(self):
        if self.is_empty():
            return " (empty)"
        return "\n".join(f" {i + 1}. {card}" for i, card in enumerate(self.__cards))