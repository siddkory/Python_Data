"""
PlayingCard

Things to Consider
-> Use dict with immutable objects ( Tuple ) as key instead of if-else
-> Use list.index to use at as the 'value' for sorting ( comparing card_ranks with hand )
-> Use list.count to get the count of elements in the list
"""


class PlayingCard:

    def __init__(self, hand):
        self.card_suits = ('h', 'd', 'c', 's')
        self.card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.rank = sorted([r[:-1] for r in hand], key=self.card_ranks.index)
        self.suit = [s[-1:] for s in hand]
        # for Hashing purpose use immutable tuple
        self.group = tuple(sorted([self.rank.count(x) for x in set(self.rank)], reverse=True))

    def get_poker_ranking(self):
        flush = True if len(set(self.suit)) == 1 else False
        straight = True if len(set(self.rank)) == 5 and self.card_ranks.index(self.rank[4]) - self.card_ranks.index(
            self.rank[0]) == 4 else False

        if flush and straight:
            if self.rank[4] == 'A':
                return "Royal Flush"
            return "Straight Flush"
        elif flush:
            return "Flush"
        elif straight:
            return "Straight"

        rank_count = {
            (4, 1): "Four of a Kind",
            (3, 2): "Full House",
            (3, 1, 1): "Three of a kind",
            (2, 2, 1): "Two Pair",
            (2, 1, 1, 1): "Pair",
            (1, 1, 1, 1, 1): "High Card"
        }

        return rank_count[self.group]


""" Test Poker """
print(PlayingCard(["10h", "Jh", "Qh", "Ah", "Kh"]).get_poker_ranking())  # "Royal Flush"
print(PlayingCard(["9h", "Jh", "Qh", "10h", "Kh"]).get_poker_ranking())  # "Straight Flush"
print(PlayingCard(["10s", "10c", "8d", "10d", "10h"]).get_poker_ranking())  # "Four of a Kind"
print(PlayingCard(["10s", "10c", "8d", "10d", "8h"]).get_poker_ranking())  # "Full House"
print(PlayingCard(["10h", "10h", "2h", "3h", "8h"]).get_poker_ranking())  # "Flush"
print(PlayingCard(["3h", "5h", "Qs", "9h", "Ad"]).get_poker_ranking())  # "High Card"
