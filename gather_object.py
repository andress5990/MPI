"""
Collective communications example showing how to gather python objects
To execute this run: mpirun -np 3 python gather_object.py
"""

import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = {'number': random.random()}

print "I am node {id} and this is my data: {data}".format(id=rank, data=data)

received_data = comm.gather(data, root=0)

if rank == 0:
    print "\nThis is the data received on root from child nodes: {data}".format(data=received_data)
