#!/bin/bash
jupyter run src/preprocess.ipynb > /dev/null
jupyter run src/preprocess_graph.ipynb > /dev/null
tree -I "__pycache__|site_libs|*.old.*" > tree.txt
conda env export -n ada2022teamlovelace > env.yaml
