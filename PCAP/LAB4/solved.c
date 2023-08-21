#include"mpi.h"
#include<stdio.h>
int main(int argc, char *argv[]) {
    int rank, size,i;int fact=1;int fact_sum=0;
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

for(i=1;i<=rank+1;i++)
{
	fact=fact*i;
}
    int error;
    MPI_Errhandler_set(MPI_COMM_WORLD, MPI_ERRORS_RETURN);
    error = MPI_Scan(&fact,&fact_sum, MPI_INT, MPI_SUM, i);

    if (error != MPI_SUCCESS) {
        char s[100];
        int len, class1;
        MPI_Error_string(error, s, &len);
        MPI_Error_class(error, &class1);
        fprintf(stderr, "Error description is %s\n", s);
        fflush(stderr);
        fprintf(stderr, "Error class is %d\n", class1);
        fflush(stderr);
    }

MPI_Scan(&fact,&fact_sum,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
if(rank==size-1)
{
	printf("Sum = %d\n",fact_sum);

}
MPI_Finalize();
return 0;
}
