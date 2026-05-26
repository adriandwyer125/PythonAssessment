from deck import Deck
from player import Player
 
class Dealer:
    turn_counter = 0
    PLAYER_COUNT = 3
 
    def __init__(self):
        self.__main_deck = Deck(16)
        self.__secondary_deck = Deck(8)
        self.__players = []
        for i in range(Dealer.PLAYER_COUNT):
            self.__players.append(Player())
 
    def use(self):
        rounds_played = 0
        running = True
        while running:
            choice = input("Choice (p/g/d/x): ")
 
            if choice == "d":
                print("Main deck:")
                for c in self.__main_deck.get_cards():
                    print(c)
                print("Secondary deck:")
                for c in self.__secondary_deck.get_cards():
                    print(c)
 
            elif choice == "g":
                for i in range(len(self.__players)):
                    total = 0
                    for c in self.__players[i].get_hand():
                        total += c.get_health()
                    print("Player " + str(i + 1) + ": " + str(total))
 
            elif choice == "p":
                if len(self.__main_deck.get_cards()) < Dealer.PLAYER_COUNT:
                    print("Not enough cards to play a full round.")
                else:
                    rounds_played += 1
                    print("Playing round " + str(rounds_played))
                    for t in range(Dealer.PLAYER_COUNT):
                        current = Dealer.turn_counter % Dealer.PLAYER_COUNT
                        player = self.__players[current]
                        print("Player " + str(current + 1) + "'s turn")
 
                        main_card = self.__main_deck.deal()
                        n = Dealer.PLAYER_COUNT - 1
                        sec_card = None
                        if Dealer.turn_counter % n == n - 1:
                            sec_card = self.__secondary_deck.deal()
 
                        print("Dealer deals:")
                        print("Main: " + str(main_card))
                        if sec_card:
                            print("Secondary: " + str(sec_card))
 
                        # show hand
                        print("------------------------")
                        print("HAND")
                        print("------------------------")
                        if len(player.get_hand()) == 0:
                            print("Empty")
                        else:
                            for i in range(Player.MAX_HAND_SIZE):
                                if i < len(player.get_hand()):
                                    print(str(i + 1) + ": " + str(player.get_hand()[i]))
                                else:
                                    print(str(i + 1) + ":")
                        print("------------------------")
 
                        # handle secondary
                        if sec_card:
                            ans = input("Would you like to store the secondary card in your hand (y/n): ")
                            if ans == "y" and len(player.get_hand()) < Player.MAX_HAND_SIZE:
                                player.add_to_hand(sec_card)
                            print("------------------------")
                            print("HAND")
                            print("------------------------")
                            if len(player.get_hand()) == 0:
                                print("Empty")
                            else:
                                for i in range(Player.MAX_HAND_SIZE):
                                    if i < len(player.get_hand()):
                                        print(str(i + 1) + ": " + str(player.get_hand()[i]))
                                    else:
                                        print(str(i + 1) + ":")
                            print("------------------------")
 
                        # handle main card
                        card_to_play = None
                        if len(player.get_hand()) >= Player.MAX_HAND_SIZE:
                            print("Hand is full. Main card played automatically!")
                            card_to_play = main_card
                        else:
                            ans = input("Would you like to place main in your hand (h) or play (p): ")
                            if ans == "h":
                                player.add_to_hand(main_card)
                                print("------------------------")
                                print("HAND")
                                print("------------------------")
                                for i in range(Player.MAX_HAND_SIZE):
                                    if i < len(player.get_hand()):
                                        print(str(i + 1) + ": " + str(player.get_hand()[i]))
                                    else:
                                        print(str(i + 1) + ":")
                                print("------------------------")
                                idx = int(input("Card to play: ")) - 1
                                card_to_play = player.remove_card(idx)
                            else:
                                card_to_play = main_card
 
                        # attack
                        next_p = (current + 1) % Dealer.PLAYER_COUNT
                        defender = self.__players[next_p]
                        atk = card_to_play.get_attack()
                        style = card_to_play.get_style()
                        to_remove = []
                        for c in defender.get_hand():
                            if c.get_style() == style:
                                dmg = atk * 2
                            else:
                                dmg = atk
                            c.set_health(c.get_health() - dmg)
                            if c.get_health() <= 0:
                                c.set_is_active(False)
                                to_remove.append(c)
                        for c in to_remove:
                            defender.get_hand().remove(c)
 
                        Dealer.turn_counter += 1
 
            elif choice == "x":
                print("Dealer has called the game!")
                print("Game finished after " + str(rounds_played) + " rounds")
                best = -1
                winner = 0
                for i in range(len(self.__players)):
                    total = 0
                    for c in self.__players[i].get_hand():
                        total += c.get_health()
                    if total > best:
                        best = total
                        winner = i
                print("Player " + str(winner + 1) + " finished with the highest score of " + str(best))
                running = False
 
if __name__ == "__main__":
    dealer = Dealer()
    dealer.use()