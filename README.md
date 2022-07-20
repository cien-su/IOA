# IOA
Programs and codes for Intelligent Optimization Algorithms in Python.

## Preface
It's widely known that Intelligent Optimization Algorithms can be divided into 4 categories and many sub-categories: 
- Evolutionary Algorithms
- Swarm-based Algorithms
- Physics-based Algorithms
    - Simulated Annealing Algorithm
- Others

This repository is for these kinds of codes and programs. All codes are programmed by Python 3.9.6.

Some explanations are given to help you use these Python files.

## Evolutionary Algorithms

## Swarm-based Algorithms

## Physics-based Algorithms
Physics-based Algorithms are inspired by physical laws and turn objective rules into algorithms. Representative algorithms are *Simulated Annealing*, *Gravitational Search Algorithm* and so on.

This folder contains different kinds of physics-based algorithms. Every sub-folder will give you an explanation to one specific algorithm.
### Simulated Annealing
Simulated Annealing is a very classic algorithm to solve combination optimization problems, imitating the process of solid substance annealing, which is a randomly optimized algorithm. Simulated Annealing perfectly solve the dilemma of partial optimization in *Climbing Algorithm* etc.

The main idea of this algorithm is Metropolis Law :
- Accept new solution if the energy of new solution is lower than the energy of old solution
- If not, accept new solution based on probability (p): p=exp(-ΔE/kT), which ΔE stands for E(t+1)-E(t), k is Boltzmann constant and T is the system temparature.

Simulated Annealing has many different applications, here gives you some import packaged functions for you to rewrite and call.

> SA_SV.py

This Python file is to find the lowest point of single-variable function using Simulated Annealing. Two functions are contained in the file:
- aimFunction() return the value of a specific functiion using the input single variable. You can change the function into your own ones.
- SA_SV() return the result of Simulated Annealing. Input parameters are as follows:
    - xmin: the minimum of the domain
    - xmax: the maximum of the domain
    - T: the initial temparature
    - Tmin: the minimum temparature
    - k: iteration times in inernal circles
    - turb: turbulence you need to generate new solution

> SA_MV.py

To be continued...

> SA_TSP.py

This Python file is to solve one kind of classical problem - TSP (Travelling Salesman Problem), using Simulated Annealing. Main functions:
- SA_TSP() return the shortest path and visualize them. Input parameters:
    - city_loc: the coordinates list of cities, such as: city_loc = [(1304,2312),(3639,1315),(4177,2244),(3712,1399)]
    - V: the list of cities' name or number, such as: V = ['A', 'B', 'C']
    - T: the initial temparature
    - Tmin: the minimum temparatur
    - L: iteration times in inernal circles
    - q: the rate to decrease temperature, between 0~1
    
However, the other common form of data is the distance of each two cities rather than their coordinates. So another function is given:
- SA_TSP2() return the shortest path and visualize them based on adjacency matrix. Input parameters:
    - city_dist: the adjacency matrix of cities, while setting the distance from one city to itself as Infinity (See my code)
    - V: the list of cities' name or number, such as: V = ['A', 'B', 'C']
    - T: the initial temparature
    - Tmin: the minimum temparatur
    - L: iteration times in inernal circles
    - q: the rate to decrease temperature, between 0~1
    
> SA_SP.py

To be continued...

### xxx

## Others

## Backwords
For any other questions, my mail is 2847724403@qq.com
