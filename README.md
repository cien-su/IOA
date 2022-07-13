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
### <span id=Simulated Annealing>Simulated Annealing</span>
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

### xxx

## Others

## Backwords
For any other questions, my mail is 2847724403@qq.com
