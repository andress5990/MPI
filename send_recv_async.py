"""
Simple example showing how to send python objects using isend and irecv
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 2 python send_recv_async.py
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    req = comm.isend(data, dest=1)
    req.wait()
    print "Send completed from root node"
elif rank == 1:
    # parameter here is dest, not source, probably a bug TODO report it
    req = comm.irecv(dest=0)
    data = req.wait()
    print "Data received on slave node: {data}".format(data=data)
