#include <stdio.h>
#include <mpi.h>

double f(double x) {
    return 4.0 / (1.0 + x * x);
}

int main(int argc, char* argv[]) {
    int num_steps = 1000000;  // Total number of rectangles
    double step_size = 1.0 / (double)num_steps;
    double pi_partial = 0.0;
    double local_sum = 0.0;
    double x;

    int rank, num_procs;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    // Calculate the local sum for each process
    for (int i = rank; i < num_steps; i += num_procs) {
        x = (i + 0.5) * step_size;
        local_sum += f(x);
    }

    // Reduce local sums to get the partial sum on each process
    MPI_Reduce(&local_sum, &pi_partial, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        double pi = pi_partial * step_size;
        printf("Approximate value of π: %.15f\n", pi);
    }

    MPI_Finalize();

    return 0;
}
