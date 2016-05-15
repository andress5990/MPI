"""
Simple example showing how to send python objects using isend and irecv
To execute this run: mpirun -np 2 python send_recv_async_wait.py
"""
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    # Introduce simulated waiting. In real life, this waiting can be
    # due to processing in the root, getting resources from the network, etc
    for i in range(5):
        time.sleep(1)
    req = comm.isend(data, dest=1)
    req.wait()
    print "Send completed from root node"
elif rank == 1:
    # parameter here is dest, not source, probably a bug TODO report it!
    req = comm.irecv(dest=0)
    test_result = req.test()
    while not test_result[0]:
        print "Waiting for data from root node..."
        time.sleep(0.5)
        test_result = req.test()

    data = test_result[1]
    print "Data received on slave node: {data}".format(data=data)
