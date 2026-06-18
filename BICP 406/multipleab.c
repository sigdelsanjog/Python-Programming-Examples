#include <stdio.h>
#include <cuda_runtime.h>

// CUDA Kernel: Multiply a * b on GPU
__global__ void multiply(float a, float b, float *result) {
    *result = a * b;
}

int main() {
    float a = 555555555555.0f;
    float b = 333333333333.0f;

    printf("Multiplying a = %.1f and b = %.1f using GPU\n\n", a, b);

    // Step 1: Allocate memory on GPU for result
    float *d_result;
    cudaMalloc((void **)&d_result, sizeof(float));
    printf("Step 1: GPU memory allocated\n");

    // Step 2: Launch kernel on GPU
    multiply<<<1, 1>>>(a, b, d_result);
    printf("Step 2: Kernel launched on GPU\n");

    // Step 3: Wait for GPU to finish
    cudaDeviceSynchronize();
    printf("Step 3: GPU computation completed\n");

    // Step 4: Copy result back to CPU
    float h_result = 0.0f;
    cudaMemcpy(&h_result, d_result, sizeof(float), cudaMemcpyDeviceToHost);
    printf("Step 4: Result copied back to CPU\n");

    // Step 5: Print result
    printf("\nResult: %.1f * %.1f = %.1f\n", a, b, h_result);

    // Step 6: Free GPU memory
    cudaFree(d_result);
    printf("Step 6: GPU memory freed\n");

    return 0;
}
