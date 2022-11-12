#!/bin/bash
jupyter run src/preprocess.ipynb > /dev/null
tree -I "__pycache__" > tree.txt
conda env export -n ada2022teamlovelace > env.yaml