import math


def find_counts(message):
    """
    :rtype: letter frequencies
    :type message: input string to be analyzed
    """
    counter = {}
    for letter in sorted(message):
        counter[letter] = message.count(letter)
    return counter


def probability_vector(letter_freq):
    """
    :rtype: probability vector
    :type letter_freq: counts of letters in message
    """
    freq_list = list(letter_freq.values())
    total_count = sum(letter_freq.values())

    return [i / total_count for i in freq_list]


def calc_entropy(p):
    """
    :param p: list with probability of each letter in alphabet occurring
    :return:  entropy of message
    """
    entropy_sum = 0
    for letter_probability in p:
        entropy_sum += letter_probability * math.log2(letter_probability)
    return -1 * entropy_sum


def main(message):
    letter_freq = find_counts(message)
    p = probability_vector(letter_freq)
    entropy = calc_entropy(p)
    return entropy

