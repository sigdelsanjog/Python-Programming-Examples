#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LENGTH 1000000UL

int main() {
    char *dna = (char*) malloc((LENGTH + 1) * sizeof(char));
    if (dna == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    char bases[] = {'A', 'T', 'G', 'C'};
    srand(time(NULL));
    clock_t start = clock();
    for (unsigned long i = 0; i < LENGTH; i++) {
        dna[i] = bases[rand() % 4];
    }
    dna[LENGTH] = '\0';
    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Sequential generation completed\n");
    printf("Time taken: %f seconds\n", time_taken);
    printf("First 100 bases:\n");
    for (int i = 0; i < 100; i++) {
        printf("%c", dna[i]);
    }
    printf("\n");
    free(dna);
    return 0;
}