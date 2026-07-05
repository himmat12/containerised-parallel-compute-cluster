import time
import numpy as np
from tasks import get_prime_factors_chunk
from input_array import input_array

CHUNK_SIZE = 500

if __name__ == "__main__":
    print("\n\n[Producer] Dispatching tasks...")

    # input_array = np.random.randint(low=1, high=10000, size=10000).tolist()

    start_time = time.time()

    chunks = [
        input_array[i : i + CHUNK_SIZE] for i in range(0, len(input_array), CHUNK_SIZE)
    ]

    async_results = [get_prime_factors_chunk.delay(chunk) for chunk in chunks]

    print("\n\n[Producer] Tasks queued successfully. Gathering results...")
    results = [r.get() for r in async_results]

    end_time = time.time()

    print("\n\n\n" + "=" * 80)
    print(f"Distributed Compute Completed!")
    print(f"Total Processing Time: {end_time - start_time:.2f} seconds")
    print("=" * 80)
