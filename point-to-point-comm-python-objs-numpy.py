from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(1000, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print("Rank {} is passing integer array to rank 1 ".format(rank))
    print("First integer is: {}".format(data[0]))
elif rank == 1:
    data = numpy.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print("Rank {} is receiving integer array from rank 0".format(rank))
    print("First integer is: {}".format(data[0]))

# automatic MPI datatype discovery
if rank == 0:
    data = numpy.arange(100, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
    print("Rank {} is passing float array to rank 1 ".format(rank))
    print("I am not telling it contains floats.")
    print("First number is: {}".format(data[0]))
elif rank == 1:
    data = numpy.empty(100, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print("Rank {} is receiving float array from rank 0".format(rank))
    print("First number is: {}".format(data[0]))
    print("I didn't know they were floats!")
