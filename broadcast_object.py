"""
Collective communications example showing how to send python objects using broadcast
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 4 python broadcast_object.py
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
   data = {'key1' : [7, 2.72, 2+3j],
           'key2' : ( 'abc', 'xyz')}
else:
   data = None

data = comm.bcast(data, root=0)

print "I am node {id} and I got this data: {data}".format(id=rank, data=data)
