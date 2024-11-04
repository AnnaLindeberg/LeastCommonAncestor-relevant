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

In a DAG or network G with leaf set L(G), a  least common ancestor (LCA) of a subset A ⊆ L(G) is a vertex v that is an ancestor of all x ∈ A and has no descendant that also satisfies this property. A DAG or network G is *LCA-relevant* if each vertex is the LCA of some subset of leaves. Moreover, G is *lca-relevant* if each vertex is a unique LCA in G.  DAGs and networks inferred from genomic sequence data can be highly complex and tangled, often containing redundant information. In particular, vertices that are not LCAs of any subset of leaves  can be considered less significant and redundant in an evolutionary contex as they lack direct relevance to the observed ancestral relationships. To reduce unnecessary complexity and eliminate unsupported vertices, we aim to simplify a DAG to retain only LCA vertices while preserving essential evolutionary information. This python tool allows to simplify a DAG by ``removal'' of such vertices resulting in an LCA-relevant, resp., lca-relevant DAG  while preserving key structural
properties of the original DAG or network.

As input an extended Newick format in a file `FILE` is expected (see [article](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-9-532) for details about the extended Newick format).
In the `main.py` the file name we used is `FILE` = `violaN` which is also provided in the repository.

As output you will get the original network, the LCA-relevant and an lca-relevant version stored in

* `FILE-orig.txt`,  `FILE-LCArel.txt`, `FILE-lowercase-lcarel.txt` (edge list)
* `FILE-orig.newick`,  `FILE-LCArel.newick`, `FILE-lowercase-lcarel.newick` (extended Newick format)
* `FILE-orig.png`,  `FILE-LCArel.png`, `FILE-lowercase-lcarel.png` (png file containing a drawing of the DAG or networks)


## Citation and references

If you use this program in your project or code from it, please consider citing:

#### Simplifying and Characterizing DAGs and Phylogenetic Networks via Least Common Ancestor Constraints,  A. Lindeberg and M. Hellmuth, arXiv:2411.00708, 2024

Please report any bugs and questions in the [Issues](https://github.com/AnnaLindeberg/LeastCommonAncestor-relevant/issues) section.


		
