#include"mpi.h"
#include<math.h>
#include<stdio.h>
int main(int argc,char *argv[])
{

  int rank,size;int x=4;

  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);

  int output=pow(x,rank);

  printf("process %d printing value %d",rank,output);
  MPI_Finalize();
  return 0;

}