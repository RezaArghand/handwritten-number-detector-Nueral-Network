import numpy as np

import dataManager as dm

# parameters of PSO optimization algorithm
number_of_particles = 120  # particle count

# varNum = 10  # variable count
damping_rate_W = 0.9  # inertia damper
max_of_variable = 10  # max domain
min_of_variable = -10  # min domain
satisfaction_cost_number = 1.0e-200  # satisfaction point
W = 0.95  # inertia
C1 = 1.8  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 3000  # max iteration
# end parameters of PSO optimization

# parameters of neural network
layerNum = [len(dm.X[1, :]), 20, 20, 10]
varNum = (layerNum[0] + 1) * layerNum[1] + (layerNum[1] + 1) * layerNum[2] + (layerNum[2] + 1) * layerNum[3]
# end parameters of neural network
print(varNum)
