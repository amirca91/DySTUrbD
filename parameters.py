import numpy as np
from scipy.stats import gamma

# data generation
jobs_per_m = [0, 0.0004733, 0, 0.0315060, 0.0479474] # job density by land use
avgIncome = 7177.493
stdIncome = 1624.297
risk_by_age = {i: i/90 for i in range(0, 91)}
risk_func = np.vectorize(lambda t:risk_by_age[t]) # fucntion for computing contagion risk

# network generation
beta = 2 # distance influence in gravity model
w_a = 1 # weight of age in network distance
w_i = 1 # weight of income in network distance
w_d = 1 # weight of spatial distance in network distance
b_min_prob = 0.00161 # minimum probability for a strongly connected  network of buildings
a_min_prob = 0.95 # minimum probability for edge between agents

# activities
k = 2 # number of flexible activites between a pair of fixed activities
a_dist = 1 # maximum distance between agents and buildings
bld_dist = 6 # maximum distance between buildings and buildings

# infection
norm_factor = 0.04 # normalizing factor for contagion probability
recover = 21 # days to recover from infection
contagious_risk_day= gamma((4.5/3.5)**2, scale=3.5**2/4.5) #np.array([0.05,0.5,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]) # contagion factor by days
diagnosis = 7
quarantine = 7



