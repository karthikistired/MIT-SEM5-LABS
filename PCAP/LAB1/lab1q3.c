#include"mpi.h"
#include<math.h>
#include<stdio.h>
int main(int argc,char *argv[])
{

  int rank,size;

  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);
  double result=0;int a=8,b=5;

  switch(rank){
    case 0:
    printf("process %d performing addition",rank);
    result=a+b;
    printf("\n Result of  process %d is %f",rank,result);
    break;

    case 1:
    printf("process %d performing subtraction",rank);
    result=a-b;
    printf("\n Result of  process %d is %f",rank,result);
    break;

    case 2:
    printf("process %d performing multiplication",rank);
    result=a*b;
    printf("\n Result of  process %d is %f",rank,result);
    break;

    case 3:
    printf("process %d performing division",rank);
    result=a/b;
    printf("\n Result of  process %d is %f",rank,result);
    break;

  }

  printf("Process %d terminated",rank);


MPI_Finalize();
return 0;
}