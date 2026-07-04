# Distributed Docker Cluster
A distributed docker containers cluster for experimenting with distributed computing and parallel workloads using Docker Compose, Celery, and Redis.

## Problem statement
Given a Celery worker executing a computationally heavy task, where picking an integer $k$ from an array requires generating a sequence of the first $k$ perfect squares, with a simulated $2\text{-second}$ latency imposed on *each* individual square calculation, the workload per task scales dynamically based on the value of $k$ ($k \times 2\text{ seconds}$).

If the requirement is to process an array of size $n$ containing various integers $[k_1, k_2, ..., k_n]$, a sequential execution results in a total latency of $\left(\sum k\right) \times 2\text{ seconds}$. To optimize performance and prevent long-running tasks from blocking the pipeline, how can we distribute these dynamic workloads across a cluster of multiple, horizontally scaled Docker container nodes?

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
|            | 1. Dispatches 'n' asynchronous tasks               |
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
1. CLone the repo: `git clone https://github.com/himmat12/distributed-docker-cluster.git`
2. Open the cloned directory: `cd distributed-docker-cluster`
3. Run the compose: `docker compose up --build --scale worker=4` -> spawns all compose service containers and replicates 4 worker service containers for parallel computation for generating square numbers

## Compute Logs
You can see the debug logs for each setup:

#### Running single worker
> You can see the verbose logs [here](./logs/single_worker_compute_log.md).

Results:

```
worker-1    | [2026-07-04 00:23:39,319: INFO/MainProcess] Task tasks.generate_k_square_numbers [3559a316-0b93-4b2e-82ac-fd1226819dd2] received
worker-1    | [2026-07-04 00:23:39,322: INFO/MainProcess] Task tasks.generate_k_square_numbers[9956cbf7-08bc-46ed-a5dd-31c91ed6070d] received
worker-1    | [2026-07-04 00:23:39,324: WARNING/ForkPoolWorker-4] [Worker] Starting heavy 3 square numbers computation...
worker-1    | [2026-07-04 00:23:39,325: WARNING/ForkPoolWorker-2] [Worker] Starting heavy 5 square numbers computation...
worker-1    | [2026-07-04 00:23:39,330: INFO/MainProcess] Task tasks.generate_k_square_numbers[ae04ca6b-ee81-43d8-91fe-eea14923ebe3] received
worker-1    | [2026-07-04 00:23:39,333: WARNING/ForkPoolWorker-3] [Worker] Starting heavy 2 square numbers computation...
worker-1    | [2026-07-04 00:23:43,335: WARNING/ForkPoolWorker-3] [Worker] Finished computation!
worker-1    | Result: [1, 4]
worker-1    | [2026-07-04 00:23:43,369: INFO/ForkPoolWorker-3] Task tasks.generate_k_square_numbers[ae04ca6b-ee81-43d8-91fe-eea14923ebe3] succeeded in 4.036321217000022s: [1, 4]
worker-1    | [2026-07-04 00:23:45,326: WARNING/ForkPoolWorker-4] [Worker] Finished computation!
worker-1    | Result: [1, 4, 9]
worker-1    | [2026-07-04 00:23:45,367: INFO/ForkPoolWorker-4] Task tasks.generate_k_square_numbers[3559a316-0b93-4b2e-82ac-fd1226819dd2] succeeded in 6.0439506419998s: [1, 4, 9]
worker-1    | [2026-07-04 00:23:49,327: WARNING/ForkPoolWorker-2] [Worker] Finished computation!
worker-1    | Result: [1, 4, 9, 16, 25]
producer-1  |
worker-1    | [2026-07-04 00:23:49,403: INFO/ForkPoolWorker-2] Task tasks.generate_k_square_numbers[9956cbf7-08bc-46ed-a5dd-31c91ed6070d] succeeded in 10.079271358999904s: [1, 4, 9, 16, 25]
producer-1  |
producer-1  | [Producer] Infrastructure is verified healthy by Docker. Dispatching tasks...
producer-1  |
producer-1  |
producer-1  | [Producer] Triggering parallel tasks for array: [3, 5, 2]
producer-1  |
producer-1  |
producer-1  | [Producer] Tasks queued successfully. Gathering results...
producer-1  |
producer-1  |
producer-1  |
producer-1  | ================================================================================
producer-1  | Distributed Compute Completed!
producer-1  | Total Processing Time: 10.38 seconds
producer-1  | Final Output Matrix: [[1, 4, 9], [1, 4, 9, 16, 25], [1, 4]]
producer-1  | ================================================================================
```

#### Running 4 parallel workers
> You can see the verbose logs [here](./logs/parallel_workers_computelog.md).

Results:

```
worker-1    | [2026-07-04 00:24:47,180: INFO/MainProcess] Task tasks.generate_k_square_numbers[20381ee5-3695-4258-9a30-86c9bb1cfb80] received
worker-1    | [2026-07-04 00:24:47,192: WARNING/ForkPoolWorker-4] [Worker] Starting heavy 3 square numbers computation...
worker-3    | [2026-07-04 00:24:47,196: INFO/MainProcess] Task tasks.generate_k_square_numbers[9bfba095-5221-4f75-9692-fc76078798ca] received
worker-4    | [2026-07-04 00:24:47,196: INFO/MainProcess] Task tasks.generate_k_square_numbers[74b9fa3d-d3bb-46ce-884c-0baebbdbcdf7] received
worker-3    | [2026-07-04 00:24:47,203: WARNING/ForkPoolWorker-4] [Worker] Starting heavy 2 square numbers computation...
worker-4    | [2026-07-04 00:24:47,201: WARNING/ForkPoolWorker-4] [Worker] Starting heavy 5 square numbers computation...
worker-3    | [2026-07-04 00:24:51,205: WARNING/ForkPoolWorker-4] [Worker] Finished computation!
worker-3    | Result: [1, 4]
worker-3    | [2026-07-04 00:24:51,240: INFO/ForkPoolWorker-4] Task tasks.generate_k_square_numbers[9bfba095-5221-4f75-9692-fc76078798ca] succeeded in 4.038002817999768s: [1, 4]
worker-1    | [2026-07-04 00:24:53,193: WARNING/ForkPoolWorker-4] [Worker] Finished computation!
worker-1    | Result: [1, 4, 9]
worker-1    | [2026-07-04 00:24:53,235: INFO/ForkPoolWorker-4] Task tasks.generate_k_square_numbers[20381ee5-3695-4258-9a30-86c9bb1cfb80] succeeded in 6.043468405000112s: [1, 4, 9]
worker-4    | [2026-07-04 00:24:57,205: WARNING/ForkPoolWorker-4] [Worker] Finished computation!
worker-4    | Result: [1, 4, 9, 16, 25]
producer-1  |
worker-4    | [2026-07-04 00:24:57,223: INFO/ForkPoolWorker-4] Task tasks.generate_k_square_numbers[74b9fa3d-d3bb-46ce-884c-0baebbdbcdf7] succeeded in 10.023003527999663s: [1, 4, 9, 16, 25]
producer-1  |
producer-1  | [Producer] Infrastructure is verified healthy by Docker. Dispatching tasks...
producer-1  |
producer-1  |
producer-1  | [Producer] Triggering parallel tasks for array: [3, 5, 2]
producer-1  |
producer-1  |
producer-1  | [Producer] Tasks queued successfully. Gathering results...
producer-1  |
producer-1  |
producer-1  |
producer-1  | ================================================================================
producer-1  | Distributed Compute Completed!
producer-1  | Total Processing Time: 10.86 seconds
producer-1  | Final Output Matrix: [[1, 4, 9], [1, 4, 9, 16, 25], [1, 4]]
producer-1  | ================================================================================
```

