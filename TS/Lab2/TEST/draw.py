import igraph as ig

with open("connections.txt", "r") as file:
    lines = file.readlines()

g = ig.Graph()

vertices = set()
edges = []

for line in lines:
    city1, city2, _, _ = line.split()
    vertices.add(city1)
    vertices.add(city2)
    edges.append((city1, city2))

g.add_vertices(list(vertices))

g.add_edges(edges)

layout = g.layout("kk")
plot = ig.plot(g, layout=layout, vertex_label=g.vs["name"])
plot.save("cities_connections.png")
