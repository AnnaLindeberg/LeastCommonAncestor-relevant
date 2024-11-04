import networkx as nx
import phylox.newick_parser
from networkx.drawing.nx_pydot import write_dot
from lca_LCA_relevant import *

def main():
    # Example usage:
    # Parse the Viola network, provided in (extended) Newick format

    with open("viola.newick") as newickFile:
        newickStr = newickFile.readline().strip()
        phyloxH = phylox.newick_parser.extended_newick_to_dinetwork(newickStr)
    
    # However, want to work with NetworkX graph – let us generate it
    G = nx.DiGraph()
    G.add_edges_from(phyloxH.edges())
    del phyloxH

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

    # And/or use pydot for nice visualizations
    # Unfortunately, pydot is not actively maintained but still works here
    # It is probably better to use Pygraphviz, but larger dependencies to install
    nxGraphs = [G, LCA_rel_G, lca_rel_G]
    fileNames = ["viola-org", "viola-LCArel", "viola-lowercase-lcarel"]
    for graph, fileName in zip(nxGraphs, fileNames):
        pydotGraph = nx.nx_pydot.to_pydot(graph)
        pydotGraph.write_svg(fileName + '.svg')
        pydotGraph.write_pdf(fileName + '.pdf')


if __name__ == '__main__':
    main()
