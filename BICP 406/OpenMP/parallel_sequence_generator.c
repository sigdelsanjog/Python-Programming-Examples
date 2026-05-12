#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#define LENGTH 1000000UL

int main() {
    char *dna = (char*) malloc((LENGTH + 1) * sizeof(char));
    if (dna == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    char bases[] = {'A', 'T', 'G', 'C'};
    double start = omp_get_wtime();
    #pragma omp parallel
    {
        unsigned int seed = time(NULL) ^ omp_get_thread_num();
        #pragma omp for
        for (unsigned long i = 0; i < LENGTH; i++) {
            dna[i] = bases[rand_r(&seed) % 4];
        }
    }

    dna[LENGTH] = '\0';
    double end = omp_get_wtime();
    printf("Parallel generation completed\n");
    printf("Threads used: %d\n", omp_get_max_threads());
    printf("Time taken: %f seconds\n", end - start);
    printf("First 100 bases:\n");
    for (int i = 0; i < 100; i++) {
        printf("%c", dna[i]);
    }
    printf("\n");
    free(dna);
    return 0;
}