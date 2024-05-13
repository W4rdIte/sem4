import igraph as ig


def generate_traffic_matrix():
    # Population data for each city
    populations = {
        "Warszawa": 1700,
        "Krakow": 760,
        "Wroclaw": 640,
        "Poznan": 540,
        "Lublin": 340,
        "Szczecin": 400,
        "Gdansk": 460,
        "Bialystok": 300,
        "Katowice": 300,
        "Rzeszow": 180,
        "Berlin": 3600,
        "Hamburg": 1800,
        "Drezno": 500,
        "Monachium": 1400,
        "Frankfurt": 2300,
        "Kolonia": 1000,
        "Dortmund": 580,
        "Stuttgart": 600,
        "Brema": 550,
        "Hanower": 520,
    }

    # Calculate the total population
    total_population = sum(populations.values())

    # Create an empty traffic matrix
    traffic_matrix = {}

    #! Calculate the traffic from each city to each other city
    for city_a in populations:
        traffic_matrix[city_a] = {}
        for city_b in populations:
            if city_a == city_b:
                traffic_matrix[city_a][city_b] = 0
            else:
                traffic = (
                    populations[city_a]
                    * 1000
                    * 20
                    / 3
                    * (populations[city_b] / total_population)
                )
                traffic_matrix[city_a][city_b] = round(traffic)

    #! DRAW MATRIX
    with open("Matrix.txt", "w") as f:
        for city_a in traffic_matrix:
            for city_b in traffic_matrix[city_a]:
                f.write(f"{traffic_matrix[city_a][city_b]:<10}")
            f.write("\n")

    return traffic_matrix
