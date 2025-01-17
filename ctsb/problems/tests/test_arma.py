# test the ARMA problem class

import ctsb
from ctsb.problems.simulated.arma import ARMA
import jax.numpy as np
import matplotlib.pyplot as plt


def test_arma(steps=100, show_plot=False, verbose=False):
    T = steps
    p, q = 3, 3
    problem = ARMA()
    problem.initialize(p,q)
    assert problem.T == 0

    test_output = []
    for t in range(T):
        test_output.append(problem.step())
        
    info = problem.hidden()
    if verbose:
        print(info)

    assert problem.T == T
    if verbose:
        print(problem.phi)
        print(problem.psi)
    if show_plot:
        plt.plot(test_output)
        plt.title("arma")
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    print("test_arma passed")
    return


if __name__=="__main__":
    test_arma()