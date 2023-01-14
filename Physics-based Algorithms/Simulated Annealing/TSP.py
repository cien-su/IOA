"""
This script is for TSP problem using Simulated Annealing
"""
__version__ = "1.0.0"
__author__ = "domain"
__all__ = ['tsp']

from random import randint, shuffle, uniform

def get_dist(a: tuple, b: tuple):
    """Get the Euclidean metric of two cities"""
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def route_length(route: list, loc_list: list):
    """Compute the length of a route"""
    whole_len = 0
    for i in range(1, len(route)):
        whole_len += get_dist(loc_list[route[i]], loc_list[route[i-1]])
    whole_len += get_dist(loc_list[route[0]], loc_list[route[-1]])
    return whole_len

def exchange_site(route: list):
    """Exchange two cities"""
    while True:
        a = randint(0, len(route) - 1)
        b = randint(0, len(route) - 1)
        if a != b:
            route[a], route[b] = route[b], route[a]
            break
    return route

def reverse_site(route: list):
    """Reverse cities between two specific cities"""
    while True:
        a = randint(0, len(route) - 1)
        b = randint(0, len(route) - 1)
        if a < b:
            route[a:b+1] = route[b:a-1:-1]
            break
        elif a > b:
            route[b:a+1] = route[a:b-1:-1]
            break
    return route

def insert_site(route: list):
    """Insert the first city behind the second city"""
    while True:
        a = randint(0, len(route) - 1)
        b = randint(0, len(route) - 1)
        if a < b:
            temp = route[a]
            route[a:b] = route[a+1:b+1]
            route[b] = temp
            break
        elif a > b:
            temp = route[b]
            route[b:a] = route[b+1:a+1]
            route[a] = temp
            break
    return route

def generate_new(route: list, method: str, w1, w2):
    """Choose a method to generate new solution"""
    if method == "exchange":
        return exchange_site(route=route)
    elif method == "reverse":
        return reverse_site(route=route)
    elif method == "insert":
        return insert_site(route=route)
    elif method == "roulette":
        p = uniform(0, 1)
        if p < w1:
            return exchange_site(route=route)
        elif p < w1 + w2:
            return reverse_site(route=route)
        else:
            return insert_site(route=route)

def sa_tsp(loc_list: list, generate_method: str, w1, w2, t0: float, threshold: float, alpha: float, iteration: int):
    """Simulated Annealing for TSP"""
    # Initial Solution
    route = [i for i in range(len(loc_list))]
    shuffle(route)
    distance = route_length(route, loc_list)
    # Annealing
    from math import exp
    count = 0
    while t0 > threshold:
        for i in range(iteration):
            new_route = generate_new(route, generate_method, w1, w2)
            new_distance = route_length(new_route, loc_list)
            p = exp((distance-new_distance)/t0)
            if new_distance < distance or uniform(0, 1) < p:
                distance = new_distance
                route = new_route
            count += 1
        t0 *= alpha
    return route, distance, count

def tsp_visual(route: list, city_name: list, loc_list: list):
    """Visualize the graph"""
    import matplotlib.pyplot as plt
    # scatter
    x1 = []
    y1 = []
    for i in loc_list:
        x1.append(i[0])
        y1.append(i[1])
    plt.scatter(x1, y1)
    # Tag
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    for i in range(len(city_name)):
        plt.text(x1[i], y1[i], city_name[i], fontsize = 12, color = "#E58CAF")
    # line
    route.append(route[0])
    x2 = []
    y2 = []
    for i in route:
        x2.append(loc_list[i][0])
        y2.append(loc_list[i][1])
    plt.plot(x2, y2)
    # Other set
    plt.title("TSP Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(alpha=0.5, linestyle="-.")
    plt.show()

def report(route: list, city_name: list, distance: float, iteration_count: int):
    """Output in format"""
    print("---------------------------")
    # path
    print("The optimal path is: ")
    route.append(route[0])
    print("\t", city_name[route[0]], end="")
    for i in route[1:]:
        print(" ->", city_name[i], end="")
    # distance
    print("\nDistance: %.2f"%distance)
    # iteration
    print("Iteration Count: %d"%iteration_count)

def tsp(loc: list, city_name: list, t0: float, threshold: float, alpha: float, inIter: int, method = "exchange", w1=0.4, w2=0.4, plot = True):
    """Main function of TSP"""
    route, distance, count = sa_tsp(loc, method, w1, w2, t0, threshold, alpha, inIter)
    report(route, city_name, distance, count)
    if plot:
        tsp_visual(route, city_name, loc)
