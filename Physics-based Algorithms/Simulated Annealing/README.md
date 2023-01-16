### Simulated Annealing
Simulated Annealing is a very classic algorithm to solve combination optimization problems, imitating the process of solid substance annealing, which is a randomly optimized algorithm. Simulated Annealing perfectly solve the dilemma of partial optimization in *Climbing Algorithm* etc.

The main idea of this algorithm is Metropolis Law :
- Accept new solution if the energy of new solution is lower than the energy of old solution
- If not, accept new solution based on probability (p): p=exp(-ΔE/kT), which ΔE stands for E(t+1)-E(t), k is Boltzmann constant and T is the system temparature.

Simulated Annealing has many different applications, here are some modules for you to call.

#### 1.SAtsp
This is for solving TSP problem using Simulated Annealing. If you want to use this module, you have to prepare:
- The locations of cities in list format. For example: `city_loc = [(1,1),(2,2),(3,3)]`
- The names of cities in list format. For example: `city_name = ['Beijing','Shanghai','Guangzhou']`

Then you download SA.py into the same directory of your own py file, and call the module like: 

```python
from SA import SAtsp
city_loc = [(1,1),(2,2),(3,3)]
city_name = ['Beijing','Shanghai','Guangzhou']
tsp = SAtsp()
```

Then you get the instance of SAtsp. All parameters have their own default values and definitely you can update the values of these parameters.

```
t0: Initial Temperature(>0, float)
cool: Cooling Factor(0~1)
inIter: Inner Iteration Times(int)
maxIter: Max Iteration Times(int)
```

Finally, you can run the SA code: 

```python
tsp.solveTSP(city_loc, city_name, "roulette", (0.6, 0.2))
tsp.report()
tsp.visual()
```

In solveTSP(), you must input the location list and name list, and choose a method to generate new solution. Methods are:

- "exchange": Choose two cities and exchange their order.
- "reverse": Reverse the order of inner cities between two chosen cities.
- "insert": Insert the order of the first chosen city after the second chosen city.
- "roulette": Use roulette to choose one method of the three above, with the weights of exchange and reverse method in tuple format.

After solving, you can use report() to show the final result and visual() to plot the map.

#### 2.
To be continued...
