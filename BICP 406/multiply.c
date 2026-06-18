#include <stdio.h>
#include <cuda_runtime.h>
#include <math.h>

// CUDA kernel: Vector multiplication on GPU
// Each thread multiplies one element from vector A with one element from vector B
__global__ void vectorMultiply(float *d_a, float *d_b, float *d_c, int n) {
    // Calculate thread index (which element this thread processes)
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    
    // Make sure we don't exceed array bounds
    if (idx < n) {
        d_c[idx] = d_a[idx] * d_b[idx];
    }
}

int main() {
    // ========== STEP 1: Initialize parameters ==========
    int n = 1024;  // Vector size
    size_t bytes = n * sizeof(float);
    
    printf("=== CUDA Vector Multiplication ===\n");
    printf("Vector size: %d elements\n", n);
    printf("Memory per vector: %.2f KB\n\n", bytes / 1024.0f);
    
    // ========== STEP 2: Allocate memory on HOST ==========
    float *h_a = (float*)malloc(bytes);  // Host vector A
    float *h_b = (float*)malloc(bytes);  // Host vector B
    float *h_c = (float*)malloc(bytes);  // Host result vector C
    
    if (!h_a || !h_b || !h_c) {
        printf("ERROR: Failed to allocate host memory\n");
        return 1;
    }
    printf("Step 1: Host memory allocated\n");
    
    // ========== STEP 3: Initialize host data ==========
    for (int i = 0; i < n; i++) {
        h_a[i] = (float)(i + 1);
        h_b[i] = (float)(i + 1);
        h_c[i] = 0.0f;
    }
    printf("Step 2: Host vectors initialized with test data\n");
    printf("  Example: h_a[0]=%.1f, h_a[1]=%.1f, ...\n\n", h_a[0], h_a[1]);
    
    // ========== STEP 4: Allocate memory on DEVICE (GPU) ==========
    float *d_a, *d_b, *d_c;
    
    cudaMalloc((void**)&d_a, bytes);
    if (cudaGetLastError() != cudaSuccess) {
        printf("ERROR: Failed to allocate GPU memory for d_a\n");
        return 1;
    }
    
    cudaMalloc((void**)&d_b, bytes);
    if (cudaGetLastError() != cudaSuccess) {
        printf("ERROR: Failed to allocate GPU memory for d_b\n");
        return 1;
    }
    
    cudaMalloc((void**)&d_c, bytes);
    if (cudaGetLastError() != cudaSuccess) {
        printf("ERROR: Failed to allocate GPU memory for d_c\n");
        return 1;
    }
    printf("Step 3: GPU memory allocated\n");
    
    // ========== STEP 5: Copy data from HOST to DEVICE ==========
    cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);
    
    printf("Step 4: Data copied from CPU to GPU\n\n");
    
    // ========== STEP 6: Configure CUDA grid and blocks ==========
    int threadsPerBlock = 256;  // Number of threads per block
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;  // Calculate blocks needed
    
    printf("Step 5: CUDA Grid Configuration\n");
    printf("  Threads per block: %d\n", threadsPerBlock);
    printf("  Blocks per grid: %d\n", blocksPerGrid);
    printf("  Total threads: %d\n\n", blocksPerGrid * threadsPerBlock);
    
    // ========== STEP 7: Launch CUDA kernel ==========
    printf("Step 6: Launching CUDA kernel on GPU...\n");
    vectorMultiply<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);
    
    // Check for kernel launch errors
    if (cudaGetLastError() != cudaSuccess) {
        printf("ERROR: Kernel launch failed: %s\n", cudaGetErrorString(cudaGetLastError()));
        return 1;
    }
    printf("  Kernel launched successfully\n\n");
    
    // ========== STEP 8: Synchronize GPU ==========
    cudaDeviceSynchronize();  // Wait for kernel to complete
    printf("Step 7: GPU computation completed and synchronized\n\n");
    
    // ========== STEP 9: Copy result from DEVICE back to HOST ==========
    cudaMemcpy(h_c, d_c, bytes, cudaMemcpyDeviceToHost);
    printf("Step 8: Results copied from GPU back to CPU\n\n");
    
    // ========== STEP 10: Verify results ==========
    printf("Step 9: Verification of results\n");
    int errors = 0;
    for (int i = 0; i < n; i++) {
        float expected = h_a[i] * h_b[i];
        if (fabs(h_c[i] - expected) > 1e-5) {
            errors++;
            if (errors <= 5) {  // Print first 5 errors
                printf("  ERROR at index %d: got %.1f, expected %.1f\n", i, h_c[i], expected);
            }
        }
    }
    
    if (errors == 0) {
        printf("  ✓ All results correct!\n\n");
        printf("First 10 results:\n");
        for (int i = 0; i < 10; i++) {
            printf("  h_a[%d] * h_b[%d] = %.1f * %.1f = %.1f\n", 
                   i, i, h_a[i], h_b[i], h_c[i]);
        }
    } else {
        printf("  ✗ Found %d errors!\n\n", errors);
    }
    
    // ========== STEP 11: Free GPU memory ==========
    printf("\nStep 10: Cleaning up GPU memory...\n");
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    printf("  GPU memory freed\n");
    
    // ========== STEP 12: Free HOST memory ==========
    free(h_a);
    free(h_b);
    free(h_c);
    printf("  CPU memory freed\n\n");
    
    printf("=== Program completed successfully ===\n");
    return 0;
}
