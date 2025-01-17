# test the LDS problem class

import jax.numpy as np
import jax.random as random
import ctsb
import matplotlib.pyplot as plt
from ctsb.problems.simulated.lds import LDS
from ctsb.utils.random import generate_key



def test_lds(steps=100, show_plot=False):
    T = steps
    n, m, d = 5, 3, 10
    problem = LDS()
    problem.initialize(n, m, d)
    assert problem.T == 0

    test_output = []
    for t in range(T):
        u = random.normal(generate_key(),shape=(n,))
        test_output.append(problem.step(u))

    info = problem.hidden()
    if verbose:
        print(info)

    assert problem.T == T
    if show_plot:
        plt.plot(test_output)
        plt.title("lds")
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    print("test_lds passed")
    return


if __name__=="__main__":
    test_lds()