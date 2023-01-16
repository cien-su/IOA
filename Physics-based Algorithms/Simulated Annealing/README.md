### Simulated Annealing
Simulated Annealing is a very classic algorithm to solve combination optimization problems, imitating the process of solid substance annealing, which is a randomly optimized algorithm. Simulated Annealing perfectly solve the dilemma of partial optimization in *Climbing Algorithm* etc.

The main idea of this algorithm is Metropolis Law :
- Accept new solution if the energy of new solution is lower than the energy of old solution
- If not, accept new solution based on probability (p): p=exp(-ΔE/kT), which ΔE stands for E(t+1)-E(t), k is Boltzmann constant and T is the system temparature.

Simulated Annealing has many different applications, here are some import packaged functions for you to call.
