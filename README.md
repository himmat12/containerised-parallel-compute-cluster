# Containerised Parallel Compute Cluster
A distributed Docker container cluster for experimenting with distributed computing and parallel workloads using Docker Compose, Celery, and Redis.

## Problem statement
Given a large array of random integers, compute the prime factorization of every integer. Because each factorization task uses trial division and is therefore computationally expensive for large values, a sequential implementation can become slow. How can we distribute the work across multiple Docker containers using Celery and Redis to reduce end-to-end processing time?

## Solution
The system uses a producer/consumer architecture. The producer in [`trigger.py`](./trigger.py) splits the input array into batches and submits each batch as an asynchronous Celery task. Redis acts as the message broker, and multiple Celery worker containers consume and process the tasks in parallel. The producer collects the final results after all task complete.

## System Architecture (Producer/Consumer)

```
+-----------------------------------------------------------------+
|                       LAPTOP / HOST MACHINE                     |
|                                                                 |
|   +------------------+                                          |
|   | PRODUCER         | (Container: producer)                    |
|   | [Array of size n]|                                          |
|   +--------+---------+                                          |
|            |                                                    |
|            | 1. Dispatches chunked asynchronous tasks           |
|            v                                                    |
|   +------------------+                                          |
|   | MESSAGE BROKER   | (Container: redis)                       |
|   | [Task Queue]     |                                          |
|   +--------+---------+                                          |
|            |                                                    |
|            +-------------------+-------------------+            |
|            | 2. Pulls tasks    |                   |            |
|            v                   v                   v            |
|   +--------------+   +--------------+   +--------------+        |
|   | COMPUTATION  |   | COMPUTATION  |   | COMPUTATION  |        |
|   | NODE 1       |   | NODE 2       |   | NODE 'M'     |        |
|   | (worker_1)   |   | (worker_2)   |   | (worker_m)   |        |
|   +--------------+   +--------------+   +--------------+        |
|                                                                 |
+-----------------------------------------------------------------+
```

## Getting started

Steps:
1. Clone the repo: `git clone https://github.com/himmat12/containerised-parallel-compute-cluster.git`
2. Open the cloned directory: `cd containerised-parallel-compute-cluster`
3. Run the compose: 
    - `docker compose up --build` to run a single worker to compute the whole array numbers prime factors.
    - `docker compose up --build --scale worker=4` to run 4 parallel workers at once to distribute the computation.

## Benchmarks
When `CHUNK_SIZE = 1000` which is 10 batches given the [`input_array`](./input_array.py) contains `10000` random integers in the range `1 to 1000000`, the a single worker run took `101.75 seconds` to compute all numbers prime factors, while the 4 parallel workers run took `74.99 seconds` reducing total rutime by `25.1 seconds`, which shows that parallel execution improves throughput for sufficiently heavy workloads.

#### Running a single worker
> You can see the verbose logs [here](./logs/single_worker_compute_log.md).

Results:

```
producer-1  | ================================================================================
producer-1  | Distributed Compute Completed!
producer-1  | Total Processing Time: 101.75 seconds
producer-1  | ================================================================================
```

#### Running 4 parallel workers
> You can see the verbose logs [here](./logs/parallel_workers_computelog.md).

Results:

```
producer-1  | ================================================================================
producer-1  | Distributed Compute Completed!
producer-1  | Total Processing Time: 74.99 seconds
producer-1  | ================================================================================
```