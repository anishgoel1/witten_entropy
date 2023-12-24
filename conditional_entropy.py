import math


def conditional_entropy(mat):
    """
    :param mat: probability matrix
    :return: conditional entropy H(Y|X) {amount of uncertainty in Y given we know X}
    """
    results = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != 0:
                results.append(mat[i][j] * math.log2(mat[i][j] / sum(row[j] for row in mat)))
            else:
                results.append(0)
    return -sum(results)


def joint_entropy(mat):
    """
    :param mat: probability matrix
    :return: joint entropy H(Y,X) = H(Y|X) + H(X)
    """
    values = []
    for k in range(len(mat)):
        values.append(sum(row[k] for row in mat))
    entropy_x = -sum([p * math.log2(p) for p in values])

    return conditional_entropy(mat) + entropy_x


def mutual_information(mat):
    """
    :param mat: probability matrix
    :return: mutual information I(Y, X) = H(Y) - H(Y|X)
    """
    values = [sum(row) for row in mat]
    entropy_y = -sum([p * math.log2(p) for p in values])
    mi = entropy_y - conditional_entropy(mat)
    return mi if mi > 0 else 0


# Suppose Alice flips a coin, and the result is
# communicated in a noisy channel to Bob with
# the following probabilities
#                BOB    BOB
#                 H      T
#  ALICE      H  1/5    1/30
#  ALICE      T  1/6    3/7
# note that Bob == X, Alice == Y {impl. assumes rows == Y, cols == X}
# Alice doesn't have to flip the coin
# find MI, JE, CE of the above matrix


p_mat = [[1/5, 1/30], [1/6, 3/7]]

# conditional entropy : entropy remaining in Alice given we know Bob's result
print("CONDITIONAL ENTROPY:", conditional_entropy(p_mat))
# joint entropy : amount of uncertainty in both Alice & Bob
print("JOINT ENTROPY:", joint_entropy(p_mat))
# mutual information : how much we learn about Alice by observing Bob
print("MUTUAL INFORMATION:", mutual_information(p_mat))





