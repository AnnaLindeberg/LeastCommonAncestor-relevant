import networkx as nx
import phylox.newick_parser
from phylox import DiNetwork
from phylox.constants import LENGTH_ATTR
from phylox.newick_parser import dinetwork_to_extended_newick
from networkx.drawing.nx_pydot import write_dot
from lca_LCA_relevant import *
import warnings

def main():
    # Example usage:
    # Parse the Viola network, provided in (extended) Newick format

    with open("viola.newick") as newickFile:
        newickStr = newickFile.readline().strip()
        phyloxH = phylox.newick_parser.extended_newick_to_dinetwork(newickStr)
    
    # However, want to work with NetworkX graph – let us generate it
    G_tmp = nx.DiGraph()
    G_tmp.add_edges_from(phyloxH.edges())
    G = nx.DiGraph()
    G = nx.convert_node_labels_to_integers(G_tmp)
    del phyloxH
    del G_tmp

    # Compute the LCA-relevant DAG without shortcuts
    LCA_rel_G = LCA_relevant_dag(G)
    LCA_rel_G = remove_shortcuts(LCA_rel_G)

    # Compute the lca-relevant DAG
    lca_rel_G = lca_relevant_dag(G)
    lca_rel_G = remove_shortcuts(lca_rel_G)


    # Display the edges of the LCA-relevant DAG
    print("Edges of the LCA-relevant DAG:", list(LCA_rel_G.edges))
    # Display the edges of the lca-relevant DAG
    print("Edges of the lca-relevant DAG:", list(lca_rel_G.edges))

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        # And/or use pydot for nice visualizations
        # Unfortunately, pydot is not actively maintained but still works here
        # It is probably better to use Pygraphviz, but larger dependencies to install
        nxGraphs = [G, LCA_rel_G, lca_rel_G]
        fileNames = ["viola-org", "viola-LCArel", "viola-lowercase-lcarel"]
        for graph, fileName in zip(nxGraphs, fileNames):
            pydotGraph = nx.nx_pydot.to_pydot(graph)
            pydotGraph.write_png(fileName + '.png')
        
        # If you DO have pygraphviz installed and working, the following can be used
#        dotGraph = nx.nx_agraph.to_agraph(graph)
#        fileType = '.png'
#        dotGraph.draw(fileName + fileType, format=fileType[1:], prog='dot' )

if __name__ == '__main__':
    main()
