# binder-neo4j

Example of a Binderised repo running neo4j.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/psychemedia/binder-neo4j/master)

The neo4j server is installed into `$CONDA_DIR` (by default, `/srv/conda`), the only guaranteed writeable path outside `$HOME`.

Demo test code in the `py/` folder.

(Since this repo also runs `jupytext`, if you  click on the `neo4j-demo.py` file from the notebook server `tree/` page and it will open *as a notebook*.)


To run a container built from this repo locally:

```
pip install jupyter-repo2docker

repo2docker https://github.com/psychemedia/binder-neo4j

```

The container also includes:

- a [`cypher_kernel`](https://github.com/HelgeCPH/cypher_kernel) which allows queries to be entered directly into code cells and interactive network diagrams to be displayed directly from cell query results.

- some simple IPython magic (installed from [innovationOUtside/cypher_magic](https://github.com/innovationOUtside/cypher_magic) repo).

Broken:

- the neo4j GUI doesn't seem to work under local testing at least
