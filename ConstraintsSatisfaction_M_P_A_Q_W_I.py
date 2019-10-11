#constraints satisfaction
from __future__ import print_function
from simpleai.search import (CspProblem, backtrack,
                             min_conflicts,MOST_CONSTRAINED_VARIABLE,
                             HIGHEST_DEGREE_VARIABLE,LEAST_CONSTRAINING_VALUE)
variables=("M","P","A","Q","W","I")
domains=dict((v,['red','green','blue']) for v in variables)
def const_different(variables,values):
      return values[0]!=values[1] #expect the value of neighbors to be different
constraints=[
      (("M","P"),const_different),
      (("M","A"),const_different),
      (("A","Q"),const_different),
      (("A","W"),const_different),
      ]

my_problem=CspProblem(variables,domains,constraints)
print(backtrack(my_problem))
print(backtrack(my_problem,variable_heuristic=MOST_CONSTRAINED_VARIABLE))
print(backtrack(my_problem,variable_heuristic=HIGHEST_DEGREE_VARIABLE))
print(backtrack(my_problem,value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem,variable_heuristic=MOST_CONSTRAINED_VARIABLE,value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem,variable_heuristic=HIGHEST_DEGREE_VARIABLE,value_heuristic=LEAST_CONSTRAINING_VALUE))
print(min_conflicts(my_problem))
