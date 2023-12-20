import math
from manimlib import *

def calc_entropy(p):
    """
    :param p: list with probability of each letter in alphabet occurring
    :return:  entropy of message
    """
    entropy_sum = 0
    for letter_probability in p:
        entropy_sum += letter_probability * math.log2(letter_probability)
    return -1 * entropy_sum


# consider average % of letters from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
probability_avg = [8.4966, 2.0720, 4.5388, 3.3844, 11.1607, 1.8121, 2.4705, 3.0034, 7.5448, 0.1965, 1.1016, 5.4893,
                   3.0129, 6.6544, 7.1635, 3.1671, 0.1962, 7.5809, 5.7351, 6.9509, 3.6308, 1.0074, 1.2899, 0.2902,
                   1.7779, 0.2722]
probability_avg = [char_percent / 100 for char_percent in probability_avg]


class EntropyAvgMessage(Scene):
    def construct(self):
        axes = Axes((0, 50, 10), (0, 250, 50))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        egraph = axes.get_graph(lambda x: x * calc_entropy(probability_avg))

        graph_label = axes.get_graph_label(egraph, Text("Information Gain wrt. Message Length"))

        self.play(
            ShowCreation(egraph),
            FadeIn(graph_label, TOP),
        )
        self.wait()
