import networkx as nx
from lca_LCA_relevant import *

def main():
    # Example usage:
    # Create a directed graph in NetworkX
    G = nx.DiGraph()

    edges = [
    (1, 2),
    (1, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (3, 6),
    (6, 7),
    (5, 8),
    (4, 9),
    (9, 10),
    (10, 8),
    (9, 11),
    (11, 12),
    (12, 13),
    (13, 14),
    (14, 10),
    (14, 15),
    (12, 16),
    (15, 17),
    (17, 18),
    (8, 18),
    (18, 19),
    (17, 20),
    (11, 21),
    (21, 22),
    (22, 13),
    (22, 23),
    (23, 24),
    (15, 24),
    (24, 20),
    (20, 25),
    (25, 26),
    (25, 27),
    (23, 28),
    (28, 29),
    (29, 30),
    (28, 31),
    (28, 32),
    (28, 33),
    (28, 34),
    (28, 35),
    (28, 36),
    (28, 37),
    (21, 38),
    (38, 39),
    (38, 40),
    (40, 39),
    (40, 41),
    (41, 42),
    (42, 32),
    (42, 33),
    (42, 37),
    (42, 34),
    (42, 35),
    (42, 36),
    (39, 43),
    (28, 44),
    (42, 44),
    (41, 43),
    (43, 31),
    (31, 45),
    (44, 46),
    (46, 47),
    (29, 48),
    (48, 47),
    (32, 49),
    (49, 48),
    (49, 50),
    (46, 51),
    (47, 52),
    (33, 53),
    (34, 54),
    (35, 55),
    (37, 56),
    (36, 57),
    (56, 57),
    (57, 58),
    (56, 59),
    (58, 59),
    (58, 60),
    (59, 61)
    ]

    # Step 3: Add edges to the DAG
    for start, end in edges:
        G.add_edge(start, end)

    # TODO: why not this?
    #G.add_edges_from(edges)

    # Compute the LCA-relevant DAG
    LCA_rel_G = LCA_relevant_dag(G)

    # Display the edges of the LCA-relevant DAG
    print("Edges of the LCA-relevant DAG:", list(LCA_rel_G.edges))

    # Compute the lca-relevant DAG
    lca_rel_G = LCA_relevant_dag(G)

    # Display the edges of the LCA-relevant DAG
    print("Edges of the LCA-relevant DAG:", list(lca_rel_G.edges))

    

if __name__ == '__main__':
    main()
