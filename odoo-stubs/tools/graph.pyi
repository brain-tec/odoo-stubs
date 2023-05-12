from typing import Any, Optional

class graph:
    nodes: Any
    edges: Any
    no_ancester: Any
    transitions: Any
    result: Any
    def __init__(self, nodes, transitions, no_ancester: Optional[Any] = ...) -> None: ...
    edge_wt: Any
    def init_rank(self) -> None: ...
    reachable_nodes: Any
    tree_edges: Any
    def tight_tree(self): ...
    def reachable_node(self, node) -> None: ...
    cut_edges: Any
    head_nodes: Any
    def init_cutvalues(self) -> None: ...
    def head_component(self, node, rest_edges) -> None: ...
    def process_ranking(self, node, level: int = ...) -> None: ...
    def make_acyclic(self, parent, node, level, tree): ...
    def rev_edges(self, tree): ...
    def exchange(self, e, f) -> None: ...
    def enter_edge(self, edge): ...
    def leave_edge(self): ...
    def finalize_rank(self, node, level) -> None: ...
    def normalize(self) -> None: ...
    def make_chain(self) -> None: ...
    def init_order(self, node, level) -> None: ...
    def order_heuristic(self) -> None: ...
    def wmedian(self) -> None: ...
    def median_value(self, node, adj_rank): ...
    def adj_position(self, node, adj_rank): ...
    levels: Any
    def preprocess_order(self) -> None: ...
    def graph_order(self) -> None: ...
    def tree_order(self, node, last: int = ...): ...
    max_order: Any
    def process_order(self) -> None: ...
    partial_order: Any
    def find_starts(self) -> None: ...
    critical_edges: Any
    links: Any
    Is_Cyclic: bool
    def rank(self) -> None: ...
    order: Any
    def order_in_rank(self): ...
    start_nodes: Any
    tree_list: Any
    start: Any
    def process(self, starting_node) -> None: ...
    def __str__(self): ...
    def scale(self, maxx, maxy, nwidth: int = ..., nheight: int = ..., margin: int = ...) -> None: ...
    def result_get(self): ...
