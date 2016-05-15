"""
Collective communications example showing how to scatter python objects
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 4 python scatter_object.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if size != 4:
    print "Please run this example with 4 processes"
    exit()

if rank == 0:
   data = [{'x': 1}, True, 3.14, 'HELLO']
else:
   data = None

data = comm.scatter(data, root=0)

print "I am node {id} and this is the data I got: {data}".format(id=rank, data=data)

MPI.Finalize()
