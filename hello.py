"""
Simplest mpi program
To execute this run: mpirun -np 4 python hello.py
"""

import mpi4py.MPI as MPI

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
size = comm.Get_size()

print "I am process {id}. Total size: {size}".format(id=myid, size=size)

MPI.Finalize()
