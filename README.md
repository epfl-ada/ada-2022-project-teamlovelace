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
conda env update -n dataenv --file env.yaml
conda activate dataenv  # activate the environment
```

To re-export with updated dependencies, run

```sh
conda env export -n dataenv > env.new.yaml
```

## Project description

TODO