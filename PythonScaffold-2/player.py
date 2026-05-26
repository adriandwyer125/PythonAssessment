class Player:
    MAX_HAND_SIZE = 2

    def __init__(self):
        self.__hand = []

    # ------------------------------------------------------------------
    # Hand state queries
    # ------------------------------------------------------------------
    def hand_is_full(self):
        return len(self.__hand) >= Player.MAX_HAND_SIZE

    def hand_is_empty(self):
        return len(self.__hand) == 0

    def get_hand_size(self):
        return len(self.__hand)

    def get_hand(self):
        return list(self.__hand)

    # ------------------------------------------------------------------
    # Hand mutations
    # ------------------------------------------------------------------
    def add_to_hand(self, card):
        """Add card to hand. Returns True if added, False if hand is full."""
        if self.hand_is_full():
            return False
        self.__hand.append(card)
        return True

    def remove_card(self, index):
        """Remove and return the card at the given 0-based index."""
        return self.__hand.pop(index)

    # ------------------------------------------------------------------
    # Game logic
    # ------------------------------------------------------------------
    def total_health(self):
        """Return the sum of health across all cards currently in hand."""
        return sum(card.get_health() for card in self.__hand)

    def receive_attack(self, attack_value, attack_style):
        """
        Apply an attack to every card in this player's hand.
        Cards matching attack_style take double damage.
        Cards whose health drops to 0 or below are automatically discarded.
        Returns a list of discarded cards.
        """
        destroyed = []
        for card in self.__hand:
            damage = attack_value * 2 if card.get_style() == attack_style else attack_value
            card.take_damage(damage)
            if not card.is_active():
                destroyed.append(card)

        for card in destroyed:
            self.__hand.remove(card)

        return destroyed

    # ------------------------------------------------------------------
    # Display and input
    # ------------------------------------------------------------------
    def display_hand(self, player_number):
        """Print the player's hand with 1-based indices."""
        print(f"Player {player_number}'s hand:")
        if self.hand_is_empty():
            print(" (empty)")
        else:
            for i, card in enumerate(self.__hand):
                print(f" {i + 1}. {card}")

    def prompt_choose_card(self):
        """
        Interactively prompt the player to select a card from their hand.
        Loops until a valid choice is made. Returns the chosen card (removed from hand).
        """
        while True:
            raw = input("Select a card number to play: ").strip()
            if raw.isdigit():
                index = int(raw) - 1
                if 0 <= index < len(self.__hand):
                    return self.remove_card(index)
            print(f" Please enter a number between 1 and {len(self.__hand)}.")