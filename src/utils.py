import dateutil
import pandas as pd
import numpy as np
import pickle

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


## Utility for getting pageviews

from mwviews.api import PageviewsClient
from collections import defaultdict

p = PageviewsClient(user_agent="<TeamLovelace@EPFL-CS401-2022> Analysis of actors")

# This queries wikipedia, don't abuse of it
def get_pageviews(names, langs):
    counts = {}
    actors = {}
    for lang in langs:
        actors[lang] = set()
        counts[lang] = defaultdict(lambda: None)
        project = "{}.wikipedia".format(lang)
        time_series = p.article_views(project, names)
        for time in time_series.values():
            for actor, count in time.items():
                if not count is None:
                    if counts[lang][actor] is None:
                        actors[lang].add(actor)
                        counts[lang][actor] = count
                    else:
                        counts[lang][actor] = counts[lang][actor] + count
    actors_to_keep = set.intersection(*actors.values())
    total_counts = {}
    for actor in actors_to_keep:
        total_counts[actor] = 0
        for lang, count in counts.items():
            total_counts[actor] += total_counts[actor] + count[actor]
    return total_counts

def get_or_init_pickle(path, init):
    try:
        value = pickle.load(open(path, "rb"))
        return value
    except (OSError, IOError) as e:
        print(path + " not found, computing it from init()")
        value = init()
        try:
            pickle.dump(value, open(path, "wb"))
        except Exception as e:
            print("could not pickle: " + e)
        return value