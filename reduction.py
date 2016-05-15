"""
Collective communications example showing reduce operations SUM, PROD, MAX, MIN
To execute this run: mpirun -np 3 python reduction.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Initialize arrays for operations results
result_sum = np.array([0, 0, 0, 0], dtype='int64')
result_prod = np.array([1, 1, 1, 1], dtype='int64')
data = np.random.random_integers(1, 10, 4)

print "I am node {id} and this is my data: {data}".format(id=rank, data=data)

comm.Reduce([data, MPI.INT], [result_sum, MPI.INT] , op=MPI.SUM, root=0)
if rank == 0:
    print "Reduced sum is: {result}".format(result=result_sum)

comm.Reduce([data, MPI.INT], [result_prod, MPI.INT] , op=MPI.PROD, root=0)
if rank == 0:
    print "Reduced multiplication is: {result}".format(result=result_prod)

max_result = np.empty(4, dtype='int64')
comm.Reduce([data, MPI.INT], [max_result, MPI.INT] , op=MPI.MAX, root=0)
if rank == 0:
    print "Reduced Max is: {result}".format(result=max_result)

min_result = np.empty(4, dtype='int64')
comm.Reduce([data, MPI.INT], [min_result, MPI.INT] , op=MPI.MIN, root=0)
if rank == 0:
    print "Reduced Min is: {result}".format(result=min_result)

MPI.Finalize()
