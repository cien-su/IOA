import random
from numpy import exp
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

def dist(city_loc: list, a: int, b: int):
  """
  Calculate the distance between two cities
  Mainly for dealing with coordinates list of cities
  Assume that every two cities are mutually reachable
  """
  x1 = city_loc[a][0]
  x2 = city_loc[b][0]
  y1 = city_loc[a][1]
  y2 = city_loc[b][1]
  distance = ((x2-x1)**2 + (y1-y2)**2) ** 0.5
  return distance


def totaldistance(city_loc: list, seq: list):
  """Calculate the total distance of TSP path"""
  value = 0
  for j in range(len(seq)-1):
    value += dist(city_loc, seq[j], seq[j+1])
  value += dist(city_loc, seq[-1], seq[0])
  return value


def totaldistance2(city_dist, seq: list):
  """
  If adjacency matrix is given rather than coordinates list, 
  use this function to calculate the total distance of TSP path
  """
  value = 0
  for i in range(len(seq) - 1):
    value += city_dist[seq[i]][seq[i+1]]
  value += city_dist[seq[-1]][seq[0]]
  return value


def init_ans(city_loc: list):
  """Initailize a new solution: [0, 1, 2, 3...]"""
  ans = []
  for i in range(len(city_loc)):
    ans.append(i)
  return ans


def init_ans2(V: list):
  """
  If adjacency matrix is given rather than coordinates list, 
  use this function to initailize a new solution
  """
  ans = [i for i in range(len(V))]
  return ans


def create_new(ans_before):
  """
  From old solution to get new solution:
  Randomly exchange the location of two vertexs
  """
  ans_after = []
  for i in range(len(ans_before)):
    ans_after.append(ans_before[i])
  a = random.randint(0, len(ans_before)-1)
  b = random.randint(0, len(ans_before)-1)
  ans_after[a], ans_after[b] = ans_after[b], ans_after[a]
  return ans_after


def SA_TSP(city_loc, V: list, T: int, Tmin: int, L: int, q: float):
  """Main function of Simulated Annealing"""
  count = 0   # Times of Temperature Changes
  trend = []    # Distance in different Temparature
  ans0 = init_ans(city_loc)   # Initial solution
  while T > Tmin:
    for i in range(L):
      newans = create_new(ans0)   # generate new solution
      old_dist = totaldistance(city_loc, ans0)
      new_dist = totaldistance(city_loc, newans)
      df = new_dist - old_dist  # distance difference
      if df >= 0:   # accept new solution on probability
        rand = random.uniform(0, 1)
        if rand < 1/(exp(df/T)):
          ans0 = newans
      else:
        ans0 = newans
    T = T * q   # update temperature
    count += 1
    now_dist = totaldistance(city_loc, ans0)
    trend.append(now_dist)
    # print(count, "times temperature decrease, Temperature: ", T, " Distance: ", now_dist)
  # final result
  distance = totaldistance(city_loc, ans0)
  print("The shortest distance: ", distance)
  print("Path:", end=" ")
  for i in ans0:
    print(V[i], "-->", end=" ")
  print(V[ans0[0]])
  # visualize
  visualize_SA(city_loc, ans0, trend, distance)


def SA_TSP2(city_dist, V: list, T: int, Tmin: int, L: int, q: float):
  """Main function of Simulated Annealing, based on adjacency matrix"""
  count = 0   # Times of Temperature Changes
  trend = []    # Distance in different Temparature
  ans0 = init_ans2(V)   # Initial solution
  while T > Tmin:
    for i in range(L):
      newans = create_new(ans0)   # generate new solution
      old_dist = totaldistance2(city_dist, ans0)
      new_dist = totaldistance2(city_dist, newans)
      df = new_dist - old_dist  # distance difference
      if df >= 0:   # accept new solution on probability
        rand = random.uniform(0, 1)
        if rand < 1/(exp(df/T)):
          ans0 = newans
      else:
        ans0 = newans
    T = T * q   # update temperature
    count += 1
    now_dist = totaldistance2(city_dist, ans0)
    trend.append(now_dist)
    # print(count, "times temperature decrease, Temperature: ", T, " Distance: ", now_dist)
  # final result
  distance = totaldistance2(city_dist, ans0)
  print("The shortest distance: ", distance)
  print("Path:", end=" ")
  for i in ans0:
    print(V[i], "-->", end=" ")
  print(V[ans0[0]])
  # visualize
  visualize_SA2(city_dist, V, ans0, trend, distance)


def visualize_SA(city_loc, ans0: list, trend: list, minD):
  """visualize simulated annealing results"""
  # visualize coordinates
  x_list = []
  y_list = []
  for i in ans0:
    x_list.append(city_loc[i][0])
    y_list.append(city_loc[i][1])
  x_list.append(city_loc[ans0[0]][0])
  y_list.append(city_loc[ans0[0]][1])
  plt.subplot(1, 2, 1)
  plt.scatter(x_list, y_list, color = 'b')
  plt.plot(x_list, y_list, color = 'r')
  for i in ans0:
    plt.annotate(V[i], (x_list[i], y_list[i]))
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title("Maps of TSP")
  # visualize iteration
  plt.subplot(1, 2, 2)
  plt.plot(trend)
  plt.axhline(minD, color ="#b2996e", linestyle ="--", label="Minimum Distance")
  plt.xlabel('Times')
  plt.ylabel('Distance')
  plt.title("Distance Change with Iteration Times")
  plt.show()


def visualize_SA2(city_dist, V: list, ans0: list, trend: list, minD):
  """visualize simulated annealing results, based on adjacency matrix"""
  # visualize path
  G = nx.Graph()
  e = []
  for i in range(len(ans0)-1):
    val = city_dist[ans0[i]][ans0[i+1]]
    if val != float('inf'):
      temp = (V[ans0[i]], V[ans0[i+1]], val)
      e.append(temp)
  e.append((V[ans0[-1]], V[ans0[0]], city_dist[ans0[-1]][ans0[0]]))
  G.add_weighted_edges_from(e)
  plt.subplot(1, 2, 1)
  mpl.rcParams["font.sans-serif"]=["SimHei"]    # Chinese Character Set
  nx.draw(G, with_labels = True, pos = nx.spring_layout(G))
  plt.title("Maps of TSP")
  # visualize iteration
  plt.subplot(1, 2, 2)
  plt.plot(trend)
  plt.axhline(minD, color ="#b2996e", linestyle ="--", label="Minimum Distance")
  plt.xlabel('Times')
  plt.ylabel('Distance')
  plt.title("Distance Change with Iteration Times")
  plt.show()



if __name__ == "__main__":
  city_loc = [(1304,2312),(3639,1315),(4177,2244),(3712,1399),(3488,1535),
  (3326,1556),(3238,1229),(4196,1004),(4312,790),(4380,570),
  (3007,1970),(2562,1756),(2788,1491),(2381,1676),(1332,695),
  (3715,1678),(3918,2179),(4061,2370),(3780,2212),(3676,2578),
  (4029,2838),(4263,2931),(3429,1908),(3507,2367),(3394,2643),
  (3439,3201),(2935,3240),(3140,3550),(2545,2357),(2778,2826),(2370,2975)]
  V = [str(i) for i in range(1, 32)]
  T = 5000
  Tmin = 25
  q = 0.98
  L = 1000
  SA_TSP(city_loc, V, T, Tmin, L, q)

if __name__ == "__main__":
  city_dist = [
    [float('inf'),110.003361,224.418701,406.036237,451.53583,621.97118,860.203885,1249.863325,1074.359837,925.494706],
    [110.003361,float('inf'),192.933531,429.770471,554.672663,601.056023,859.246155,1273.454285,966.501145,821.429451],
    [224.418701,192.933531,float('inf'),259.315353,531.685916,792.812008,1052.10699,1461.829012,940.693998,771.702052],
    [406.036237,429.770471,259.315353,float('inf'),445.52285,1023.483202,1266.210725,1645.460596,1109.006074,923.983699],
    [451.53583,554.672663,531.685916,445.52285,float('inf'),969.999049,1137.108665,1418.245064,1472.268744,1302.305682],
    [621.97118,601.056023,792.812008,1023.483202,969.999049,float('inf'),281.716395,741.514693,1189.877177,1130.092836],
    [860.203885,859.246155,1052.10699,1266.210725,1137.108665,281.716395,float('inf'),464.888496,1449.059656,1402.501067],
    [1249.863325,1273.454285,1461.829012,1645.460596,1418.245064,741.514693,464.888496,float('inf'),1911.300531,1867.372744],
    [1074.359837,966.501145,940.693998,1109.006074,1472.268744,1189.877177,1449.059656,1911.300531,float('inf'),192.398329],
    [925.494706,821.429451,771.702052,923.983699,1302.305682,1130.092836,1402.501067,1867.372744,192.398329,float('inf')]
  ]
  V = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏']
  T = 5000
  Tmin = 25
  q = 0.98
  L = 1000
  SA_TSP2(city_dist, V, T, Tmin, L, q)