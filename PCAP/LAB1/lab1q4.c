#include"mpi.h"
#include<math.h>
#include<stdio.h>
#include<string.h>
int main(int argc,char *argv[])
{

  int rank,size;int i=0,len;char name[10]="karthik";
  len=strlen(name);
  


  MPI_Init(&argc,&argv);
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);
for(i=0;i<size;i++)
{
  if(i==rank){
if (name[i]>=97 && name[i]<=122)
{
  printf("\n Process %d toggling the character %c \n",rank,name[i]);
  name[i]=name[i]-32;
}
else{
  printf("\n Process %d toggling the character %c \n",rank,name[i]);
  name[i]=name[i]+32;
}
}}

printf("The toggled string is %s",name);

MPI_Finalize();
return 0;
}