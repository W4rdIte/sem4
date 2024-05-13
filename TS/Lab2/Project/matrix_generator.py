import os
import igraph as ig

folder_name = "data"
cities_file = "cities.txt"
connections_file = "connections.txt"


def load_cities(folder, filename):
    cities = {}
    file_path = os.path.join(folder, filename)
    with open(file_path, "r") as file:
        for line in file:
            city, population = line.strip().split()
            cities[city] = int(population)
    return cities


def load_edges(folder, filename):
    edges = []
    file_path = os.path.join(folder, filename)
    with open(file_path, "r") as file:
        for line in file:
            start, end, capacity, reliability = line.strip().split()
            edges.append((start, end, int(capacity), float(reliability)))
    return edges


def generate_traffic_matrix():

    miasta = load_cities(folder_name, cities_file)
    krawedzie = load_edges(folder_name, connections_file)

    total_population = sum(miasta.values())

    traffic_matrix = {}

    #! Calculate the traffic from each city to each other city
    for city_a in miasta:
        traffic_matrix[city_a] = {}
        for city_b in miasta:
            if city_a == city_b:
                traffic_matrix[city_a][city_b] = 0
            else:
                traffic = (
                    miasta[city_a] * 1000 * 20 / 3 * (miasta[city_b] / total_population)
                )
                traffic_matrix[city_a][city_b] = round(traffic) * 1.1

    g = ig.Graph()
    g.add_vertices(list(miasta.keys()))

    for edge in krawedzie:
        g.add_edge(
            edge[0],
            edge[1],
            capacity=edge[2],
            reliability=edge[3],
        )

    #! DRAW MATRIX
    output_file = os.path.join(folder_name, "MATRIX.txt")
    with open(output_file, "w") as f:
        for city_a in traffic_matrix:
            for city_b in traffic_matrix[city_a]:
                f.write(f"{traffic_matrix[city_a][city_b]:<10}")
            f.write("\n")

    return traffic_matrix
