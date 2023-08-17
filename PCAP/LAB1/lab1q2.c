#include"mpi.h"
#include<math.h>
#include<stdio.h>
int main(int argc,char *argv[])
{

  int rank,size;int x=4;

  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);

  if(rank%2==0)
  {
    printf("Process %d printing Hello",rank);
  }
  else 
  {
    printf("Process %d printing World",rank);
  }
  MPI_Finalize();
  return 0;
}