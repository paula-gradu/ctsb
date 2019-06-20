"""
S&P 500 daily opening price
"""

import ctsb
import os.path as osp
import numpy as np
import pandas as pd
from ctsb.utils import seeding, sp500


class SP500(ctsb.Problem):
	"""
	Description: Outputs the daily opening price of the S&P 500 stock market index 
		from January 3, 1986 to June 29, 2018.
	"""

	def __init__(self):
		self.initialized = False
		self.data_path = "../data/sp500.csv" # TODO: change to absolute path - os.path.abspath(ctsb)

	def initialize(self):
		"""
		Description:
			Check if data exists, else download, clean, and setup.
		Args:
			None
		Returns:
			The first S&P 500 value
		"""
		self.initialized = True
		self.T = 0

		# calls function that downloads data from online source
		if not osp.isfile(self.data_path): sp500()
		self.df = pd.read_csv(self.data_path)	

		return self.df.iloc[self.T, 1]

	def step(self):
		"""
		Description:
			Moves time forward by one day and returns value of the stock index
		Args:
			None
		Returns:
			The next S&P 500 value
		"""
		assert self.initialized
		self.T += 1
		return self.df.iloc[self.T, 1]

	def hidden(self):
		"""
		Description:
			Return the date corresponding to the last value of the S&P 500 that was returned
		Args:
			None
		Returns:
			Date (string)
		"""
		assert self.initialized
		return self.df.iloc[self.T, 0]

	def seed(self, seed=None):
		"""
		Description:
			Seeds the random number generator to produce deterministic, reproducible results. 
		Args:
			seed (int): Default value None. The number that determines the seed of the random
			number generator for the system.
		Returns:
			A list containing the resulting NumPy seed.
		"""
		self.np_random, seed = seeding.np_random(seed)
		return [seed]

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
		print(ARMA_help)


# string to print when calling help() method
ARMA_help = """

-------------------- *** --------------------

Id: SP500-v0
Description: Outputs the daily opening price of the S&P 500 stock market index from
	January 3, 1986 to June 29, 2018.

Methods:

	initialize()
			Check if data exists, else download, clean, and setup.
		Args:
			None
		Returns:
			The first S&P 500 value

	step()
		Description:
			Moves time forward by one day and returns value of the stock index
		Args:
			None
		Returns:
			The next S&P 500 value

	hidden()
		Description:
			Return the date corresponding to the last value of the S&P 500 that was returned
		Args:
			None
		Returns:
			Date (string)

	seed(seed)
		Description:
			Seeds the random number generator to produce deterministic, reproducible results. 
		Args:
			seed (int): Default value None. The number that determines the seed of the random
			number generator for the system.
		Returns:
			A list containing the resulting NumPy seed.

	help()
		Description:
			Prints information about this class and its methods.
		Args:
			None
		Returns:
			None

-------------------- *** --------------------

"""

