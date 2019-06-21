# test the ARMA problem class

import ctsb
import ctsb.core
from ctsb.core import Problem
from ctsb.problems.simulated.lstm_output import LSTM_Output
import jax.numpy as np
import matplotlib.pyplot as plt


def test_lstm():
    T = 10000
    n, m, l, h = 5, 3, 5, 10
    problem = LSTM_Output(n, m, l, h)
    assert problem.T == 0

    test_output = []
    for t in range(T):
        if (t+1) * 10 % T == 0:
            print("{} timesteps".format(t+1))
        u = np.random.normal(size=(n,))
        test_output.append(problem.step(u))

    assert problem.T == T
    plt.plot(test_output)
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    return


if __name__=="__main__":
    test_lstm()