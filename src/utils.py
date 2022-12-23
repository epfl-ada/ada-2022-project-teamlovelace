import dateutil
import pandas as pd
import numpy as np

__all__ = ['autoparse_year', 'get_grid_arrangement']

def autoparse_year(x):
	return dateutil.parser.parse(x).year if not pd.isna(x) else x

def autoparse_month(x):
	# "1988" -> "YYYY"

	# "2011-03-19" -> "YYYY-MM-DD"
	# return dateutil.parser.parse(x).month if not pd.isna(x) else pd.NaT
	pass

def get_grid_arrangement(n: int) -> tuple[int, int]:
	"""
	Retrieves the grid arrangement that is the nearest-to-square rectangular
	arrangement of plots.

	https://github.com/matplotlib/grid-strategy
	"""
	# May not work for very large n because of the float sqrt
	# Get the two closest factors (may have problems for very large n)
	step = 2 if n % 2 else 1
	for i in range(int(np.sqrt(n)), 0, -step):
		if n % i == 0:
			x, y = n // i, i
			break
	else:
		x, y = n, 1

	# Convert this into a grid arrangement
	return x,y