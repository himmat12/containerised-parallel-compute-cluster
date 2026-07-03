import time
from tasks import generate_k_square_numbers

if __name__ == "__main__":
    print("--- [Producer] Infrastructure is verified healthy by Docker. Dispatching tasks... ---")
    
    input_array = [3, 5, 2]
    print(f"--- [Producer] Triggering parallel tasks for array: {input_array} ---")
    
    start_time = time.time()
    
    # dispatch tasks asynchronously
    async_results = [generate_k_square_numbers.delay(k) for k in input_array]
    
    print("--- [Producer] Tasks queued successfully. Gathering results... ---")
    results = [r.get() for r in async_results]
    
    end_time = time.time()
    
    print("\n" + "="*40)
    print(f"Distributed Compute Completed!")
    print(f"Total Processing Time: {end_time - start_time:.2f} seconds")
    print(f"Final Output Matrix: {results}")
    print("="*40)