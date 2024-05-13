import random

output_file = "MATRIX.txt"


def generate_traffic_matrix():
    populations = {
        "Amsterdam": 821,
        "Berlin": 3645,
        "Bruksela": 1212,
        "Budapeszt": 1756,
        "Dublin": 544,
        "Helsinki": 631,
        "Londyn": 8982,
        "Madryt": 3223,
        "Moskwa": 12641,
        "Paryż": 2161,
        "Praga": 1309,
        "Rzym": 2873,
        "Sztokholm": 975,
        "Warszawa": 1765,
        "Wiedeń": 1897,
        "Zagrzeb": 806,
        "Zurych": 402,
        "Ateny": 3154,
        "Lizbona": 504,
        "Oslo": 634,
    }

    total_population = sum(populations.values())

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
    with open(output_file, "w") as f:
        for city_a in traffic_matrix:
            for city_b in traffic_matrix[city_a]:
                f.write(f"{traffic_matrix[city_a][city_b]:<10}")
            f.write("\n")

    return traffic_matrix
