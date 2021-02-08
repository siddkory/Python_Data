"""
In this challenge, you have to establish which kind of Poker combination is present in a deck of five cards. Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

"Ah" ➞ Ace of hearts
"Ks" ➞ King of spades
"3d" ➞ Three of diamonds
"Qc" ➞ Queen of clubs
There are 10 different combinations. Here's the list, in decreasing order of importance:

Name	Description
Royal Flush	A, K, Q, J, 10, all with the same suit.
Straight Flush	Five cards in sequence, all with the same suit.
Four of a Kind	Four cards of the same rank.
Full House	Three of a Kind with a Pair.
Flush	Any five cards of the same suit, not in sequence.
Straight	Five cards in a sequence, but not of the same suit.
Three of a Kind	Three cards of the same rank.
Two Pair	Two different Pair.
Pair	Two cards of the same rank.
High Card	No other valid combination.
Given a list hand containing five strings being the cards, implement a function that returns a string with the name of the highest combination obtained, accordingly to the table above.

Examples
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"

poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"

poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"

"""


class PokerDeck:
    def __init__(self, hand):
        self.suit = ('h', 'd', 'c', 's')
        self.rank = [x for x in range(2, 15)]


def is_royal_flush(rank, suit):
    if len(set(suit)) == 1 and [10, 11, 12, 13, 14] == rank:
        return True
    else:
        return False


def is_straight_flush(rank, suit):
    if len(set(suit)) == 1 and rank[4] - rank[0] == 4:
        return True
    else:
        return False


def is_four_of_a_kind(rank_counter):
    for v in rank_counter.values():
        if v == 4:
            return True
    return False


def is_full_house(rank_counter):
    three, two = False, False
    for v in rank_counter.values():
        if v == 3:
            three = True
        elif v == 2:
            two = True
    return three and two


def is_straight(rank):
    if rank[4] - rank[0] == 4:
        return True
    return False


def is_three_of_a_kind(rank_counter):
    for v in rank_counter.values():
        if v == 3:
            return True
    return False


def is_two_pair(rank_counter):
    first_pair, second_pair = False, False
    for v in rank_counter.values():
        if v == 2 and not first_pair:
            first_pair = True
        elif v == 2 and first_pair:
            second_pair = True
    return first_pair and second_pair


def is_pair(rank_counter):
    for v in rank_counter.values():
        if v == 2:
            return True
    return False


def is_flush(suit):
    if len(set(suit)) == 1:
        return True
    return False


def poker_hand_ranking(hand):
    rank_to_number = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suit = [x[-1:] for x in hand]
    rank = sorted([(lambda x: int(rank_to_number[x[:-1]]) if x[:-1] in 'JKQA' else int(x[:-1]))(x) for x in hand])
    print(rank)
    from collections import defaultdict
    rank_counter = defaultdict(int)
    for i in rank:
        rank_counter[i] += 1

    if is_royal_flush(rank, suit):
        return "Royal Flush"
    elif is_straight_flush(rank, suit):
        return "Straight Flush"
    elif is_four_of_a_kind(rank_counter):
        return "Four of a Kind"
    elif is_full_house(rank_counter):
        return "Full House"
    elif is_flush(suit):
        return "Flush"
    elif is_straight(rank):
        return "Straight"
    elif is_three_of_a_kind(rank_counter):
        return "Three of a Kind"
    elif is_two_pair(rank_counter):
        return "Two Pair"
    elif is_pair(rank_counter):
        return "Pair"
    else:
        return "High card"


print(poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]))  # "Royal Flush"
print(poker_hand_ranking(["9h", "Jh", "Qh", "10h", "Kh"]))  # "Straight Flush"
print(poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]))  # "Four of a Kind"
print(poker_hand_ranking(["10s", "10c", "8d", "10d", "8h"]))  # "Full House"
print(poker_hand_ranking(["10h", "10h", "2h", "3h", "8h"]))  # "Flush"
print(poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]))  # "High Card"


# def poker_hand_ranking(deck):
#     order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     ranks = sorted([i[:-1] for i in deck], key=order.index)
#     flush = len(set(i[-1] for i in deck)) == 1
#     group = tuple(sorted([ranks.count(r) for r in set(ranks)], reverse=True))
#     straight = len(set(ranks)) == 5 and order.index(ranks[-1]) - order.index(ranks[0]) == 4
#
#     if straight and flush:
#         return 'Royal Flush' if ranks[-1] == 'A' else 'Straight Flush'
#     if straight:
#         return 'Straight'
#     if flush:
#         return 'Flush'
#
#     hands = {(4, 1): 'Four of a Kind',
#              (3, 2): 'Full House',
#              (3, 1, 1): 'Three of a Kind',
#              (2, 2, 1): 'Two Pair',
#              (2, 1, 1, 1): 'Pair',
#              (1, 1, 1, 1, 1): 'High Card'}
#
#     return hands[group]