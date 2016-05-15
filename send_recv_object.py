"""
Simple example showing how to send python objects using send and recv
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 2 python send_recv_object.py
"""

from mpi4py import MPI

if not MPI.Is_initialized():
    MPI.Init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    # Data is serialized using pickle under the hood
    comm.send(data, dest=1)
elif rank == 1:
    # Data is deserialized using pickle under the hood
    data = comm.recv(source=0)
    print "I am node {rank}. Received {data} from node 0".format(data=data, rank=rank)

MPI.Finalize()
