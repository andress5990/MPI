"""
Simple example showing how to send buffers using Send and Recv
Based on: https://mpi4py.scipy.org/docs/usrman/tutorial.html
To execute this run: mpirun -np 2 python send_recv_buffer.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# pass explicit MPI datatypes
if rank == 0:
   data = np.arange(50, dtype='int64')
   comm.Send([data, MPI.INT], dest=1)
   print "Done sending explicit data from root node"
elif rank == 1:
   data = np.empty(50, dtype='int64')
   comm.Recv([data, MPI.INT], source=0)
   print "Received data from root node (1): {data}".format(data=data)

# automatic MPI datatype discovery on Receive
if rank == 0:
   data = np.arange(50, dtype=np.float64)
   comm.Send(data, dest=1)
   print "Done sending implicit data from root node"
elif rank == 1:
   data = np.empty(50)
   comm.Recv(data, source=0)
   print "Received data from root node (2): {data}".format(data=data)
