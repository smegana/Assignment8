from undirected_graph import Graph
import heapq
import time


def read_weighted_undirected_graph(filename):
    g = []
    with open(filename) as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                g.append((v1, v2, int(w)))
            except:
                pass
    return g




def write_tree_edges_to_file(edges, filename):
    # TODO write out the edges, one per line. The same format as produced by generate_mst_input
    with open(filename, mode='w') as f:
        for v1, v2, w in edges:
            f.write("{} {} {}\n".format(v1, v2, w))




# Do not change this function's name or the arguments it takes. Also, do not change
# that it writes out the results at the end.
# This is the full contract of you code (this function in this file). Otherwise,
# please feel free to create helpers, modify provided code, create new helper files, etc.
# Whatever you turn in is what we will grade (ie we won't provide any files or overwrite
# any of yours)
# Have fun!
def compute_mst(filename):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''
    # TODO compute the edges of a minimum spanning tree

    edges = read_weighted_undirected_graph(filename)
    nodes = []

    '''Add all nodes to node list'''
    for node1, node2, weight in edges:
        if node1 not in nodes:
            nodes.append(node1)
        if node2 not in nodes:
            nodes.append(node2)

    '''Make a dictionary of connected nodes for easy access'''
    from collections import defaultdict
    connections = defaultdict(list)
    for node1, node2, weight in edges:
        connections[node1].append((weight, node1, node2))
        connections[node2].append((weight, node2, node1))
 
    tree_edges = []
    '''Start with first node so it gets used first'''
    used = set([nodes[0]])

    '''The rest of the nodes are available'''
    available = connections[nodes[0]][:]
    heapq.heapify(available)
    
    start_time = time.time()

    '''while there are available nodes'''
    while available:
        '''get one'''
        weight, node1, node2 = heapq.heappop(available)
        '''if it isn't in used'''
        if node2 not in used:
            '''add it to used and the final tree edges'''
            used.add(node2)
            tree_edges.append((node1, node2, weight))
 
            '''if the next edge connected to node2 is not used, add it to available''' 
            for edge in connections[node2]:
                if edge[2] not in used:
                    heapq.heappush(available, edge)

    end_time = time.time()    

    print("Ran in: {:.5f} secs".format(end_time - start_time))

    write_tree_edges_to_file(tree_edges, filename + '.mst')
