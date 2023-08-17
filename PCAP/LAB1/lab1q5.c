#include"mpi.h"
#include<math.h>
#include<stdio.h>
#include<string.h>

int factorial(int x)
{
  if(x==1 || x==0)
  return 1;
  else{
    return x * factorial(x-1);
  }

}

int fibonacci(int n) {
    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }

    int prev = 0;
    int current = 1;
    int next;

    for (int i = 2; i <= n; i++) {
        next = prev + current;
        prev = current;
        current = next;
    }

    return current;
}
int main(int argc,char *argv[])
{

  int rank,size;int result;


  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);

  if(rank%2==0)
  {
    result=factorial(rank);
    printf("Process %d printing factorial of %d = %d",rank,rank,result);
  }
  else{

    result=fibonacci(rank);
    printf("Process %d printing fibonacci result = %d",rank,result);

  }
MPI_Finalize();
return 0;
}