# LeastCommonAncestor-relevant
Simplifying DAGs and networks to lca-relevant and LCA-relevant DAGs.

## Installation

The program requires Python 3.10 or higher.

#### Dependencies

* [NetworkX](https://networkx.github.io/)
* [PhyloX](https://github.com/RemieJanssen/PhyloX) for parsing Newick format network
* [Pydot](https://pypi.org/project/pydot/) 

  Since Pydot is no longer maintained you can, instead  also uncomment the three lines following "If you DO have pygraphviz installed and working, the following can be used" 
  and use [PyGraphviz](https://pygraphviz.github.io/). However, Pygraphviz can be difficult to install properly and Pydot still works very well.



## Usage and description

As input an extended Newick format in a file `FILE` is expected (see [article](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-9-532) for details about the extended Newick format).
In the `main.py` the file name we used is `FILE` = `violaN` which is also provided in the repository.

As output you will get the original network, the LCA-relevant and an lca-relevant version stored in

* `FILE-orig.txt`,  `FILE-LCArel.txt`, `FILE-lowercase-lcarel.txt` (edge list)
* `FILE-orig.newick`,  `FILE-LCArel.newick`, `FILE-lowercase-lcarel.newick` (extended Newick format)
* `FILE-orig.png`,  `FILE-LCArel.png`, `FILE-lowercase-lcarel.png` (png file containing a drawing of the DAG or networks)


## Citation and references

If you use this program in your project or code from it, please consider citing:

#### Simplifying and Characterizing DAGs and Phylogenetic Networks via Least Common Ancestor Constraints,  A. Lindeberg, M. Hellmuth, arXiv:2411.00708, 2024

Please report any bugs and questions in the [Issues](https://github.com/AnnaLindeberg/LeastCommonAncestor-relevant/issues) section.


		
