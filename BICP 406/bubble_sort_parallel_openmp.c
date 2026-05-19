#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void bubble_sort_parallel(int arr[], int n) {
    for (int phase = 0; phase < n; phase++) {
        if (phase % 2 == 0) {
            #pragma omp parallel for
            for (int i = 0; i < n - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                }
            }
        } else {
            #pragma omp parallel for
            for (int i = 1; i < n - 1; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                }
            }
        }
    }
}

int main() {
    FILE *fp = fopen("random.txt", "r");
    if (fp == NULL) {
        printf("Could not open random.txt\n");
        return 1;
    }

    int capacity = 1024;
    int n = 0;
    int *arr = (int *)malloc(capacity * sizeof(int));
    if (arr == NULL) {
        fclose(fp);
        return 1;
    }

    while (1) {
        int value;
        int result = fscanf(fp, "%d", &value);
        if (result != 1) {
            break;
        }

        if (n == capacity) {
            capacity *= 2;
            int *new_arr = (int *)realloc(arr, capacity * sizeof(int));
            if (new_arr == NULL) {
                free(arr);
                fclose(fp);
                return 1;
            }
            arr = new_arr;
        }
        arr[n++] = value;

        int c = fgetc(fp);
        if (c == EOF) {
            break;
        }
    }
    fclose(fp);

    double start = omp_get_wtime();
    bubble_sort_parallel(arr, n);
    double elapsed = omp_get_wtime() - start;

    for (int i = 0; i < 20 && i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf("Time taken: %.6f seconds\n", elapsed);

    free(arr);
    return 0;
}
