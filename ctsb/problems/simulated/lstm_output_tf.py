"""
--- DEPRECATED --

Long-short term memory output
"""
import jax
import jax.numpy as np
import tensorflow as tf

from keras.models import Sequential, Model
from keras.layers import Input, Dense, LSTM

import ctsb


# class for online control tests
class LSTM_Output(ctsb.Problem):
    """
    Produces outputs from a randomly initialized long-short term memory LSTM (LSTM).
    """

    def __init__(self):
        self.initialized = False

    def initialize(self, n, m, l=32, h=128, lstm=None):
        """
        Description:
            Randomly initialize the LSTM.
        Args:
            n (int): Input dimension.
            m (int): Observation/output dimension.
            l (int): Default value 32. Length of LSTM memory, i.e. only consider last l inputs when producing next output.
            h (int): Default value 128. Hidden dimension of LSTM.
            lstm (model): Default value None. Pretrained LSTM to replace the hidden dynamics (must still specify
                dimensions n and m), provided by the user.
        Returns:
            The first value in the time-series
        """
        self.initialized = True
        self.T = 0
        self.n, self.m, self.l, self.h = n, m, l, h

        if lstm == None:
            hidden = LSTM(h, input_shape=(l,n))
            output = Dense(m)
            model = Sequential()
            model.add(hidden)
            model.add(output)
            model.compile(loss='mse', optimizer='sgd')
            hidden_model = Sequential()
            hidden_model.add(hidden)
            hidden_model.compile(loss='mse', optimizer='sgd')

            self.model = model
            self.hidden_model = hidden_model
        else:
            self.model = lstm
        self.x = np.zeros(shape=(l,n))

        y = self.model.predict(self.x.reshape(1, self.l, self.n))[0]
        return y

    def step(self, x):
        """
        Description:
            Takes an input and produces the next output of the LSTM.
        Args:
            x (numpy.ndarray): LSTM input, an n-dimensional real-valued vector.
        Returns:
            The output of the LSTM computed on the past l inputs, including the new x.
        """
        assert self.initialized
        assert x.shape == (self.n,)
        self.T += 1
        self.x = jax.ops.index_update(self.x, jax.ops.index[1:,:], self.x[:-1,:]) # equivalent to self.x[1:,:] = self.x[:-1,:]
        self.x = jax.ops.index_update(self.x, jax.ops.index[0,:], x) # equivalent to self.x[0,:] = x
        y = self.model.predict(self.x.reshape(1, self.l, self.n))[0]
        return y

    def hidden(self):
        """
        Description:
            Return the hidden state of the LSTM when computed on the last l inputs.
        Args:
            None
        Returns:
            h: The hidden state.
        """
        assert self.initialized
        return self.hidden_model.predict(self.x.reshape(1, self.l, self.n))[0]

    def close(self):
        """
        Not implemented
        """
        pass

    def help(self):
        """
        Description:
            Prints information about this class and its methods.
        Args:
            None
        Returns:
            None
        """
        print(LSTM_Output_help)




# string to print when calling help() method
LSTM_Output_help = """

-------------------- *** --------------------

Id: LSTM-v0
Description: Produces outputs from a randomly initialized recurrent neural network.

Methods:

    initialize(n, m, l=32, h=128, lstm=None)
        Description:
            Randomly initialize the LSTM.
        Args:
            n (int): Input dimension.
            m (int): Observation/output dimension.
            l (int): Default value 32. Length of LSTM memory, i.e. only consider last l inputs when producing next output.
            h (int): Default value 128. Hidden dimension of LSTM.
            lstm (model): Default value None. Pretrained LSTM to replace the hidden dynamics (must still specify
                dimensions n and m), provided by the user.
        Returns:
            The first value in the time-series

    step(x)
        Description:
            Takes an input and produces the next output of the LSTM.
        Args:
            x (numpy.ndarray): LSTM input, an n-dimensional real-valued vector.
        Returns:
            The output of the LSTM computed on the past l inputs, including the new x.

    hidden()
        Description:
            Return the hidden state of the LSTM when computed on the last l inputs.
        Args:
            None
        Returns:
            h: The hidden state.

    help()
        Description:
            Prints information about this class and its methods.
        Args:
            None
        Returns:
            None

-------------------- *** --------------------

"""
