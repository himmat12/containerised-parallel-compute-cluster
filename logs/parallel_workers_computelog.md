# 4 workers computation logs

```txt
(.venv) PS C:\Users\himmat\Desktop\2026\coding\distributed-docker-cluster> docker compose up --build --scale worker=4
[+] Building 4.3s (19/19) FINISHED                                                                                                                 docker:desktop-linux
 => [worker internal] load build definition from Dockerfile                                                                                                        0.0s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load metadata for docker.io/library/python:3.11-slim                                                                                       1.0s
 => [worker internal] load .dockerignore                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer 1/5] FROM docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                 0.6s
 => => resolve docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                          0.5s
 => [worker internal] load build context                                                                                                                           0.4s
 => => transferring context: 293.59kB                                                                                                                              0.4s
 => CACHED [producer 2/5] WORKDIR /app                                                                                                                             0.0s
 => CACHED [worker 3/5] COPY ./requirements.txt .                                                                                                                  0.0s
 => CACHED [worker 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                         0.0s
 => CACHED [worker 5/5] COPY . .                                                                                                                                   0.0s
 => [worker] exporting to image                                                                                                                                    0.2s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:a28f46e82a155fe103ac02015547b42ed27bac77baf7cfe0e1956f4812c49303                                                                  0.0s
 => => exporting config sha256:acacb560c7b0c8e51f13006c6cfe387b8c59b675ee8bed776a2347f320218d9c                                                                    0.0s
 => => exporting attestation manifest sha256:56bd1bd6c0684b9f939e18c8aff9fe00caa59282b5b20bb72ce1631ab7aeadce                                                      0.0s
 => => exporting manifest list sha256:98ef4162bf76b4b496598389185e0d30091b0f6da1f3083da3015ae19a4176c2                                                             0.0s
 => => naming to docker.io/library/distributed-docker-cluster-worker:latest                                                                                        0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-worker:latest                                                                                     0.0s
 => [worker] resolving provenance for metadata file                                                                                                                0.0s
 => [producer internal] load build definition from Dockerfile                                                                                                      0.0s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer internal] load build context                                                                                                                         0.5s
 => => transferring context: 293.59kB                                                                                                                              0.5s
 => CACHED [producer 3/5] COPY ./requirements.txt .                                                                                                                0.0s
 => CACHED [producer 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                       0.0s
 => CACHED [producer 5/5] COPY . .                                                                                                                                 0.0s
 => [producer] exporting to image                                                                                                                                  0.6s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:4bed9018e2f01041613e7dcd00357d9bdaec44f0864557812f71a25435ddac4e                                                                  0.0s
 => => exporting config sha256:dd4ce79052bf259b4b7f277967555b9cd2b5e9e4590a39a1dff9480320a3447b                                                                    0.0s
 => => exporting attestation manifest sha256:74fc90fa78f2d1c06df5126a0321a9c54401f77a9d98d93d7d9d49989eb1915c                                                      0.3s
 => => exporting manifest list sha256:82fb5312bdd3ca91bf40c131aadfd1e43bde775c1b0db99f8a8922001b4aa59b                                                             0.1s
 => => naming to docker.io/library/distributed-docker-cluster-producer:latest                                                                                      0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-producer:latest                                                                                   0.0s
 => [producer] resolving provenance for metadata file                                                                                                              0.0s
[+] Running 8/8
 ✔ producer                                         Built                                                                                                          0.0s
 ✔ worker                                           Built                                                                                                          0.0s
 ✔ Container distributed-docker-cluster-redis-1     Created                                                                                                        0.0s
 ✔ Container distributed-docker-cluster-producer-1  Recreated                                                                                                      2.3s
 ✔ Container distributed-docker-cluster-worker-4    Created                                                                                                        0.7s
 ✔ Container distributed-docker-cluster-worker-2    Created                                                                                                        0.8s
 ✔ Container distributed-docker-cluster-worker-1    Recreated                                                                                                      1.2s
 ✔ Container distributed-docker-cluster-worker-3    Created                                                                                                        0.8s
Attaching to producer-1, redis-1, worker-1, worker-2, worker-3, worker-4
redis-1     | 1:C 04 Jul 2026 00:24:33.583 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis-1     | 1:C 04 Jul 2026 00:24:33.583 * Redis version=7.4.8, bits=64, commit=00000000, modified=0, pid=1, just started
redis-1     | 1:C 04 Jul 2026 00:24:33.583 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis-1     | 1:M 04 Jul 2026 00:24:33.584 * monotonic clock: POSIX clock_gettime
redis-1     | 1:M 04 Jul 2026 00:24:33.585 * Running mode=standalone, port=6379.
redis-1     | 1:M 04 Jul 2026 00:24:33.606 * Server initialized
redis-1     | 1:M 04 Jul 2026 00:24:33.611 * Loading RDB produced by version 7.4.8
redis-1     | 1:M 04 Jul 2026 00:24:33.611 * RDB age 29 seconds
redis-1     | 1:M 04 Jul 2026 00:24:33.611 * RDB memory usage when created 1.50 Mb
redis-1     | 1:M 04 Jul 2026 00:24:33.612 * Done loading RDB, keys loaded: 4, keys expired: 0.
redis-1     | 1:M 04 Jul 2026 00:24:33.612 * DB loaded from disk: 0.005 seconds
redis-1     | 1:M 04 Jul 2026 00:24:33.612 * Ready to accept connections tcp
worker-3    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-3    | absolutely not recommended!
worker-3    |
worker-3    | Please specify a different user using the --uid option.
worker-3    |
worker-3    | User information: uid=0 euid=0 gid=0 egid=0
worker-3    |
worker-3    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-3    |
worker-3    |  -------------- celery@67e25906c35c v5.6.3 (recovery)
worker-3    | --- ***** -----
worker-3    | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-04 00:24:38
worker-3    | - *** --- * ---
worker-3    | - ** ---------- [config]
worker-3    | - ** ---------- .> app:         tasks:0x7f5405e82390
worker-3    | - ** ---------- .> transport:   redis://redis:6379/0
worker-3    | - ** ---------- .> results:     redis://redis:6379/0
worker-3    | - *** --- * --- .> concurrency: 4 (prefork)
worker-3    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-3    | --- ***** -----
worker-3    |  -------------- [queues]
worker-3    |                 .> celery           exchange=celery(direct) key=celery
worker-3    |
worker-3    |
worker-3    | [tasks]
worker-3    |   . tasks.generate_k_square_numbers
worker-3    |
worker-3    | [2026-07-04 00:24:38,925: INFO/MainProcess] Connected to redis://redis:6379/0
worker-3    | [2026-07-04 00:24:38,941: INFO/MainProcess] mingle: searching for neighbors
worker-2    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-2    | absolutely not recommended!
worker-2    |
worker-2    | Please specify a different user using the --uid option.
worker-2    |
worker-2    | User information: uid=0 euid=0 gid=0 egid=0
worker-2    |
worker-2    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-2    |
worker-2    |  -------------- celery@76456756d4a6 v5.6.3 (recovery)
worker-2    | --- ***** -----
worker-2    | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-04 00:24:39
worker-2    | - *** --- * ---
worker-2    | - ** ---------- [config]
worker-2    | - ** ---------- .> app:         tasks:0x7f0cf9ed2190
worker-2    | - ** ---------- .> transport:   redis://redis:6379/0
worker-2    | - ** ---------- .> results:     redis://redis:6379/0
worker-2    | - *** --- * --- .> concurrency: 4 (prefork)
worker-2    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-2    | --- ***** -----
worker-2    |  -------------- [queues]
worker-2    |                 .> celery           exchange=celery(direct) key=celery
worker-2    |
worker-2    |
worker-2    | [tasks]
worker-2    |   . tasks.generate_k_square_numbers
worker-2    |
worker-3    | [2026-07-04 00:24:39,993: INFO/MainProcess] mingle: all alone
worker-4    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-4    | absolutely not recommended!
worker-4    |
worker-3    | [2026-07-04 00:24:40,259: INFO/MainProcess] celery@67e25906c35c ready.
worker-2    | [2026-07-04 00:24:40,260: INFO/MainProcess] Connected to redis://redis:6379/0
worker-4    | Please specify a different user using the --uid option.
worker-2    | [2026-07-04 00:24:40,339: INFO/MainProcess] mingle: searching for neighbors
worker-3    | [2026-07-04 00:24:40,599: INFO/MainProcess] sync with celery@76456756d4a6
worker-4    |
worker-4    | User information: uid=0 euid=0 gid=0 egid=0
worker-4    |
worker-4    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-4    |
worker-4    |  -------------- celery@0c9cee587253 v5.6.3 (recovery)
worker-4    | --- ***** -----
worker-4    | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-04 00:24:40
worker-4    | - *** --- * ---
worker-4    | - ** ---------- [config]
worker-4    | - ** ---------- .> app:         tasks:0x7f79dabe0a90
worker-4    | - ** ---------- .> transport:   redis://redis:6379/0
worker-4    | - ** ---------- .> results:     redis://redis:6379/0
worker-4    | - *** --- * --- .> concurrency: 4 (prefork)
worker-4    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-4    | --- ***** -----
worker-4    |  -------------- [queues]
worker-4    |                 .> celery           exchange=celery(direct) key=celery
worker-4    |
worker-4    |
worker-4    | [tasks]
worker-4    |   . tasks.generate_k_square_numbers
worker-4    |
worker-1    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-1    | absolutely not recommended!
worker-1    |
worker-1    | Please specify a different user using the --uid option.
worker-2    | [2026-07-04 00:24:41,651: INFO/MainProcess] mingle: sync with 1 nodes
worker-1    |
worker-2    | [2026-07-04 00:24:41,652: INFO/MainProcess] mingle: sync complete
worker-1    | User information: uid=0 euid=0 gid=0 egid=0
worker-1    |
worker-1    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-2    | [2026-07-04 00:24:41,820: INFO/MainProcess] celery@76456756d4a6 ready.
worker-4    | [2026-07-04 00:24:42,011: INFO/MainProcess] Connected to redis://redis:6379/0
worker-4    | [2026-07-04 00:24:42,042: INFO/MainProcess] mingle: searching for neighbors
worker-3    | [2026-07-04 00:24:42,090: INFO/MainProcess] sync with celery@0c9cee587253
worker-2    | [2026-07-04 00:24:42,089: INFO/MainProcess] sync with celery@0c9cee587253
worker-1    |
worker-1    |  -------------- celery@4610781694d2 v5.6.3 (recovery)
worker-1    | --- ***** -----
worker-1    | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-04 00:24:42
worker-1    | - *** --- * ---
worker-1    | - ** ---------- [config]
worker-1    | - ** ---------- .> app:         tasks:0x7f1bda9aa0d0
worker-1    | - ** ---------- .> transport:   redis://redis:6379/0
worker-1    | - ** ---------- .> results:     redis://redis:6379/0
worker-1    | - *** --- * --- .> concurrency: 4 (prefork)
worker-1    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-1    | --- ***** -----
worker-1    |  -------------- [queues]
worker-1    |                 .> celery           exchange=celery(direct) key=celery
worker-1    |
worker-1    |
worker-4    | [2026-07-04 00:24:43,129: INFO/MainProcess] mingle: sync with 2 nodes
worker-1    | [tasks]
worker-2    | [2026-07-04 00:24:43,172: INFO/MainProcess] sync with celery@4610781694d2
worker-3    | [2026-07-04 00:24:43,170: INFO/MainProcess] sync with celery@4610781694d2
worker-4    | [2026-07-04 00:24:43,131: INFO/MainProcess] mingle: sync complete
worker-1    |   . tasks.generate_k_square_numbers
worker-4    | [2026-07-04 00:24:43,322: INFO/MainProcess] celery@0c9cee587253 ready.
worker-1    |
worker-1    | [2026-07-04 00:24:43,075: INFO/MainProcess] Connected to redis://redis:6379/0
worker-1    | [2026-07-04 00:24:43,111: INFO/MainProcess] mingle: searching for neighbors
worker-1    | [2026-07-04 00:24:44,195: INFO/MainProcess] mingle: sync with 2 nodes
worker-1    | [2026-07-04 00:24:44,195: INFO/MainProcess] mingle: sync complete
worker-1    | [2026-07-04 00:24:44,284: INFO/MainProcess] celery@4610781694d2 ready.
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
producer-1 exited with code 0
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 6/6 Desktop   o View Config   w Enable Watch
 ✔ Container distributed-docker-cluster-producer-1  Stopped                                                                                                        0.0s
 ✔ Container distributed-docker-cluster-worker-1    Stopped                                                                                                        3.5s
 ✔ Container distributed-docker-cluster-worker-3    Stopped                                                                                                        6.0s
 ✔ Container distributed-docker-cluster-worker-4    Stopped                                                                                                        3.2s
 ✔ Container distributed-docker-cluster-worker-2    Stopped                                                                                                        6.0s
 ✔ Container distributed-docker-cluster-redis-1     Stopped                                                                                                        1.1s

(.venv) PS C:\Users\himmat\Desktop\2026\coding\distributed-docker-cluster>
```