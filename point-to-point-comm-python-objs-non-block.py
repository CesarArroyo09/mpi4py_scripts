#!/usr/bin/env

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print("I am rank {}. I have data: {}".format(rank, data.items()))
    req = comm.isend(data, dest=1, tag=11)
    req.wait()
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print("I am rank {}. I also have data: {}".format(rank, data.items()))
