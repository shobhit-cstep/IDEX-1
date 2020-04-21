import matplotlib.pyplot as plt
from numpy import array


def plot_fig(desc, x, ys):
    for y in ys:
        plt.plot(x, y)
        plt.plot(x, y)
        plt.savefig("figures/plot_"+desc+".png")


def split_sequence(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)


def print_observation_against_actual(actuals, observations):
    for actual, observation in zip(actuals, observations):
        print('predicted=%f, expected=%f' % (actual, observation))