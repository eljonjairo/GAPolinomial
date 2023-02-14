#!/usr/bin/env python3

# Genetic Algorithm to calculate the coefficients of a n order polynomial
# 
# John Diaz january 2023
#TO DO List:
#
#
import os 
import warnings

import numpy as np


from IPython import get_ipython
get_ipython().magic('reset -sf')
warnings.filterwarnings("ignore")

os.system('clear')


# Input Parameters

np = 3                                    # Number of parameters (Polynomial order)
P1ini = 0.0;   P1end = 10.0; P1stp = 0.5  # Initial, final and incremental values for parameter 1
P2ini = -10.0; P2end = 0.0;  P2stp = 0.5  # Initial, final and incremental values for parameter 2
P3ini = 0.0;   P3end = 20.0; P3stp = 0.5  # Initial, final and incremental values for parameter 3

xini = 0.0; xend = 100.0; xstp = 0.2      # Initial, final and incremental values for abscise

nPop = 10                        # Population size
MutProb = 0.3                     # Mutation probability (0-1)
nGen = 5                          # Number of generations
ElitPerc = 0.1                    # Portion of elitism

# Third order Polynomio ax2+bx+c
a = 2.5;  b = -4.0;  c = 15.0

# Create the parameters vectors
P1 = np.arange(P1ini,P1end,P1stp)




















 