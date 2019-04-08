#!/usr/bin/env

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print("I am rank {}. I can print from data: {}".format(rank, data['a']))
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print("I am rank {}. I have received object data: {}".format(rank,
                                                                 data['b']))
