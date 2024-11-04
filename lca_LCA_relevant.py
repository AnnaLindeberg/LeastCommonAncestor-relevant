import networkx as nx

def ominus(dag, node):
    """
    Perform the ominus-operation on the DAG by removing a node and its incident edges,
    and connecting all parents of the node to all its children.
    
    :param dag: A NetworkX DiGraph object.
    :param node: The node to be removed from the graph.
    :return: A modified NetworkX DiGraph with the ominus-operation applied.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    elif node not in dag:
        raise ValueError(f"{node} is not a node of {dag}")
    
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
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    elif v not in dag:
        raise ValueError(f"{v} is not a node of {dag}")

    leaf_descendants = set()
    
    for descendant in nx.dfs_postorder_nodes(dag, v):
        if dag.out_degree(descendant) == 0:
            leaf_descendants.add(descendant)
    
    return leaf_descendants




def LCA_of(dag, A):
    """
    Finds the set of lowest common ancestors (LCA) of a subset A in a DAG.
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :param A: A subset of leaves for which we want to find the LCA.
    :return: A set containing the LCA nodes for the subset A.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    
    leaves = {v for v in dag.nodes if dag.out_degree(v) == 0}
    
    if not isinstance(A, set) or not A.issubset(leaves) or len(A) == 0:
        raise ValueError(f"{A} is not a nonempty subset of leaves.")
    

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
    Computes the LCA-rel DAG by removing vertices v for which v not in LCA(C_G(v)).
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :return: A modified NetworkX DiGraph with vertices in W removed via the ominus-operation.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    
    W = set()
    
    for v in dag.nodes:
        leaf_descendants = cluster_of(dag, v)
        LCA_set = LCA_of(dag, leaf_descendants)
        
        # If v is not in the LCA of its leaf descendants, add it to W
        if v not in LCA_set:
            W.add(v)
    
    # Apply the ominus-operation by removing each node in W from the DAG
    # TODO: OK to remove print?
    # print("W = ", W	)
    modified_dag = dag.copy()
    for node in W:
        modified_dag = ominus(modified_dag, node)
    
    return modified_dag



def lca_relevant_dag(dag):
    """
    Computes the lca-rel DAG by removing vertices v for which v neq lca(C_G(v)).
    
    :param dag: The DAG represented as a NetworkX DiGraph.
    :return: A modified NetworkX DiGraph with vertices removed via the ominus-operation.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    
    modified_dag = dag.copy()
    
    for v in modified_dag.nodes:
        leaf_descendants = cluster_of(modified_dag, v)
        lca = lca_of(modified_dag, leaf_descendants)
        
        # If v is not in the LCA of its leaf descendants, remove it with ominus
        if v != lca:
            modified_dag = ominus(modified_dag, v)
    
    return modified_dag



def is_shortcut(dag, edge):
    """
    Finds out if an edge (u,v) of a DAG G is a shortcut i.e. if there is a directed uv-path in G avoiding the edge.

    :param dag: The DAG represented as a NetworkX DiGraph.
    :param edge: An edge of the DAG, tuple.
    :return: True if edge is a shortcut, otherwise False.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    elif edge not in dag.edges:
        raise ValueError(f"{edge} is not an edge of the DAG")

    u, v = edge
    other_children = [w for w in dag.successors(u) if w != v]
    # (u,v) is a shortcut if and only if there is a path from a child of u distinct from v to v
    # thus start a dfs from all children of u distinct from v, looking for v.
    for child in other_children:
        for descendant in nx.dfs_postorder_nodes(dag, child):
            if descendant == v:
                return True
            
    return False



def remove_shortcuts(dag):
    """
    Finds and removes all shortcuts of a DAG G.

    :param dag: The DAG represented as a NetworkX DiGraph.
    :return: A modified NetworkX DiGraph with shortcuts removed.
    """
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError(f"{dag} is not a DAG")
    
    modified_dag = dag.copy()
    for e in dag.edges():
        if is_shortcut(modified_dag, e):
            modified_dag.remove_edge(*e)

    return modified_dag
