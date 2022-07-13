from numpy import exp
import random

def aimFunction(x):
  """Aim Function"""
  y = x**3 - 60*x**2 - 4*x + 6
  return y

def SA_SV(xmin:float, xmax:float, T:float, Tmin:float, k:int, turb:float):
  """main program"""
  x = random.uniform(xmin, xmax)    # initialize x
  y = 0   # initialize y
  while T >= Tmin:
    for i in range(k):
      y = aimFunction(x)    # calculate y
      xnew = x + random.uniform(-turb, turb)*T  # add turbulence to generate new solution
      if xnew >= xmin and xnew <= xmax:
        ynew = aimFunction(xnew)
        if ynew - y < 0:
          x = xnew
        else:
          # accept it due to Metropolis Law
          p = exp(-(ynew - y) / T)   # Probability
          r = random.uniform(0, 1)
          if r < p:
            x = xnew
    T = 0.9*T  # Temparature Decreasing Function
  print("Lowest x value is %s, lowest y value is %s"%(x, aimFunction(x)))


if __name__ == "__main__":
  """Example of Simulated Annealing for single variable"""
  SA_SV(0, 100, 1000, 10, 50, 0.055)
