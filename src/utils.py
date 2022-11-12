import dateutil
import pandas as pd

__all__ = ['autoparse_year']

def autoparse_year(x):
	return dateutil.parser.parse(x).year if not pd.isna(x) else x

def autoparse_month(x):
	# "1988" -> "YYYY"

	# "2011-03-19" -> "YYYY-MM-DD"
	# return dateutil.parser.parse(x).month if not pd.isna(x) else pd.NaT
	pass