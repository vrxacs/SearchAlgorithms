import csv
import networkx
import pickle
import math

airports = {}
with open('data/airports.dat') as airportsFile:
    airportsReader = csv.reader(airportsFile, delimiter=',')
    for row in airportsReader:
        airports[row[0]] = {
            'name': row[1],
            'city': row[2],
            'latitude': float(row[6]),
            'longitude': float(row[7])
        }

print "Number of airports: ", len(airports)

routes = []
filteredRoutes = []
with open('data/routes.dat') as routesFile:
    routesReader = csv.reader(routesFile, delimiter=',')
    for row in routesReader:
        # Filter out routes with several stops, or ones that don't have proper airport id's
        if row[7] == '0' and row[3] != '\\N' and row[5] != '\\N':
            tmpDict = {
                'sourceID': row[3],
                'destinationID': row[5]
            }
            routes.append(tmpDict)

print len(routes)

# Remove routes that are not bidirectional
for i in range(len(routes)):
    r1 = routes[i]
    if i % 1000 == 0:
        print "Route #", i
    found = any([r2['sourceID'] == r1['destinationID'] and
                 r2['destinationID'] == r1['sourceID']
                 for r2 in routes])
    if found:
        filteredRoutes.append(r1)

print len(filteredRoutes)

# Create networkx graph:
print "Creating graph"
graph = networkx.Graph()

euclidean_distance = lambda point1, point2: math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

[graph.add_node(key, airports[key]) for key in airports]
[graph.add_edge(r['sourceID'], r['destinationID'],
                weight=euclidean_distance((airports[r['sourceID']]['latitude'], airports[r['sourceID']]['longitude']),
                                          (airports[r['destinationID']]['latitude'], airports[r['destinationID']]['longitude'])))
    for r in filteredRoutes]

# Print node information for the Sofia airport
print graph.node['1194']

pickle.dump(graph, open('data/airport_graph.pickle', 'w'))
