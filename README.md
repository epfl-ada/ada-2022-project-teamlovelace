# ada 2022 project teamlovelace

## Data

Original data from :
- [http://www.cs.cmu.edu/~ark/personas/](http://www.cs.cmu.edu/~ark/personas/)

Tree format : see ``tree.txt``

Run pipeline :

```sh
./runall.sh
```

## Conda environment

Install a replica of the conda environment by running

```sh
conda env update -n ada2022teamlovelace --file env.yaml
conda activate ada2022teamlovelace
```

To re-export with updated dependencies (this is also run in ``runall.sh``), run

```sh
conda env export -n ada2022teamlovelace > env.yaml
```

## Project description

TODO