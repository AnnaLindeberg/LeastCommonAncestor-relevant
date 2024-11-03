import networkx as nx

def ominus(dag, node):
    """
    Perform the \ominus-operation on the DAG by removing a node and its incident edges,
    and connecting all parents of the node to all its children.
    
    :param dag: A NetworkX DiGraph object.
    :param node: The node to be removed from the graph.
    :return: A modified NetworkX DiGraph with the \ominus-operation applied.
    """
    # Create a copy to avoid modifying the original graph
    modified_dag = dag.copy()
    
    # Get parents (predecessors) and children (successors) of the node
    parents = list(modified_dag.predecessors(node))
    children = list(modified_dag.successors(node))
    
    # Add edges from each parent to each child
    for parent in parents:
        for child in children:
            if not modified_dag.has_edge(parent, child):
                modified_dag.add_edge(parent, child)
    
    # Remove the node
    modified_dag.remove_node(node)
    
    return modified_dag

def cluster_of(dag, v):
    """
    Finds all leaf nodes that are descendants of a given node v in a DAG G i.e. the cluster C_G(v) of v
    
    :param dag: A NetworkX DiGraph object.
    :param v: The node for which we want to find all leaf descendants.
    :return: A set containing all leaf nodes that are descendants of v.
    """
    leaf_descendants = set()
    
    for descendant in nx.dfs_postorder_nodes(dag, v):
        if dag.out_degree(descendant) == 0:
            leaf_descendants.add(descendant)
    
    return leaf_descendants

def LCA_of(dag, A):
    """
    Finds the set of lowest common ancestors (LCA) of a subset A in a DAG.
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :param A: A subset of nodes for which we want to find the LCA.
    :return: A set containing the LCA nodes for the subset A.
    """
    if len(A) == 1:
        return A
    
    topo_order = list(nx.topological_sort(dag))[::-1]
    topo_index = {node: idx for idx, node in enumerate(topo_order)}
    A_sorted = sorted(A, key=lambda x: topo_index[x])
    
    C = {node: set() for node in dag.nodes}
    LCA = set()

    for v in topo_order:
        if dag.out_degree(v) == 0:
            C[v] = set(A_sorted) - {v}
        else:
            children = list(dag.successors(v))
            C[v] = set.intersection(*(C[child] for child in children)) if children else set()
            if not C[v] and all(C[child] for child in children):
                LCA.add(v)

    # TODO: OK to remove print?
    # if len(LCA)>1:
    #     print(A, "with LCAs:",LCA)
            
    return LCA

def lca_of(dag, A):
    """
    Finds the unique lowest common ancestors (lca) of a subset A in a DAG, if such exist
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :param A: A subset of nodes for which we want to find the LCA.
    :return: The vertex v such that v = lca(A) if well-defined, otherwise None
    """
    allLCA = LCA_of(dag, A)
    if len(allLCA) == 1:
        return next(iter(allLCA))


def LCA_relevant_dag(dag):
    """
    Computes the $\LCA$-\rel DAG by removing vertices v for which v \notin LCA(C_G(v)).
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :return: A modified NetworkX DiGraph with vertices in W removed via the \ominus-operation.
    """
    W = set()
    
    for v in dag.nodes:
        leaf_descendants = cluster_of(dag, v)
        lca_set = LCA_of(dag, leaf_descendants)
        
        # If v is not in the LCA of its leaf descendants, add it to W
        if v not in lca_set:
            W.add(v)
    
    # Apply the \ominus-operation by removing each node in W from the DAG
    # TODO: OK to remove print?
    # print("W = ", W	)
    modified_dag = dag.copy()
    for node in W:
        modified_dag = ominus(modified_dag, node)
    
    return modified_dag


def lca_relevant_dag(dag):
    """
    Computes the $\lca$-\rel DAG by removing vertices v for which v \neq lca(C_G(v)).
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :return: A modified NetworkX DiGraph with vertices removed via the \ominus-operation.
    """
    modified_dag = dag.copy()
    
    for v in modified_dag.nodes:
        leaf_descendants = cluster_of(modified_dag, v)
        lca = lca_of(modified_dag, leaf_descendants)
        
        # If v is not in the LCA of its leaf descendants, remove it with ominus
        if v != lca:
            modified_dag = ominus(modified_dag, v)
    
    return modified_dag
    