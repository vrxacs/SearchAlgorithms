import pickle
import networkx
import matplotlib.pyplot as plt
import searchAlgorithms as search

def prettyPrintPath(graph, path):
    pathStr = ''
    for node in path:
        pathStr += graph.node[node]['name'] + ' - ' + graph.node[node]['city'] + '; '
    print pathStr

def quickVisualize(drawNodes = True, drawEdges = True):
    graph = pickle.load(open('data/airport_graph.pickle', 'r'))
    positions = {nodeID: (graph.node[nodeID]['longitude'], graph.node[nodeID]['latitude'])
                 for nodeID in graph.node.keys()}

    if drawNodes:
        networkx.draw_networkx_nodes(graph, positions)
    if drawEdges:
        networkx.draw_networkx_edges(graph, positions)

    plt.plot()
    plt.show()

def testSingleRoute():
    graph = pickle.load(open('data/airport_graph.pickle', 'r'))
    positions = {nodeID: (graph.node[nodeID]['longitude'], graph.node[nodeID]['latitude'])
             for nodeID in graph.node.keys()}

    start = '1194'# Sofia
    goal = '3621'# San Antonio Intl

    path = search.breadth_first_search(graph, start, goal)
    print path
    prettyPrintPath(graph, path)

    networkx.draw_networkx_edges(graph, positions)
    # Path
    edges = [(path[i], path[i + 1]) for i in range(0, len(path) - 1)]
    networkx.draw_networkx_edges(graph, positions, edgelist=edges, edge_color='b')

    plt.plot()
    plt.show()

#quickVisualize()
testSingleRoute()