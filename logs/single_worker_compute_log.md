# Single worker computation logs
```
(.venv) PS C:\Users\himmat\Desktop\2026\coding\distributed-docker-cluster> docker compose up --build
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 15.5s (19/19) FINISHED                                                                                                                docker:desktop-linux
 => [worker internal] load build definition from Dockerfile                                                                                                        0.1s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load metadata for docker.io/library/python:3.11-slim                                                                                       1.3s
 => [worker internal] load .dockerignore                                                                                                                           0.4s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer 1/5] FROM docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                 0.6s
 => => resolve docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                          0.2s
 => [worker internal] load build context                                                                                                                           0.7s
 => => transferring context: 304.95kB                                                                                                                              0.6s
 => CACHED [producer 2/5] WORKDIR /app                                                                                                                             0.0s
 => CACHED [worker 3/5] COPY ./requirements.txt .                                                                                                                  0.0s
 => CACHED [worker 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                         0.0s
 => [worker 5/5] COPY . .                                                                                                                                          3.9s
 => [worker] exporting to image                                                                                                                                    5.8s
 => => exporting layers                                                                                                                                            3.7s
 => => exporting manifest sha256:a28f46e82a155fe103ac02015547b42ed27bac77baf7cfe0e1956f4812c49303                                                                  0.1s
 => => exporting config sha256:acacb560c7b0c8e51f13006c6cfe387b8c59b675ee8bed776a2347f320218d9c                                                                    0.0s
 => => exporting attestation manifest sha256:5fa7fd9c05e16ea71281cef5bd0b4c8fd221455f59d027fbecda394ced8e5e03                                                      0.1s
 => => exporting manifest list sha256:3466ae9155c54dc0c52201168d29ac11edaaf58795cac621dac74532160633e8                                                             0.0s
 => => naming to docker.io/library/distributed-docker-cluster-worker:latest                                                                                        0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-worker:latest                                                                                     1.8s
 => [worker] resolving provenance for metadata file                                                                                                                0.0s
 => [producer internal] load build definition from Dockerfile                                                                                                      0.0s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer internal] load build context                                                                                                                         0.6s
 => => transferring context: 293.59kB                                                                                                                              0.5s
 => CACHED [producer 3/5] COPY ./requirements.txt .                                                                                                                0.0s
 => CACHED [producer 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                       0.0s
 => CACHED [producer 5/5] COPY . .                                                                                                                                 0.0s
 => [producer] exporting to image                                                                                                                                  0.4s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:4bed9018e2f01041613e7dcd00357d9bdaec44f0864557812f71a25435ddac4e                                                                  0.0s
 => => exporting config sha256:dd4ce79052bf259b4b7f277967555b9cd2b5e9e4590a39a1dff9480320a3447b                                                                    0.1s
 => => exporting attestation manifest sha256:e3e6c81198c6232396fc6e7dbeff51e190d76497623ffe3000a78512125845ca                                                      0.1s
 => => exporting manifest list sha256:97e327f471d3cd4723d1751f9203f3e3fe3806e29d4a778dcfb37782342fdaa6                                                             0.0s
 => => naming to docker.io/library/distributed-docker-cluster-producer:latest                                                                                      0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-producer:latest                                                                                   0.0s
 => [producer] resolving provenance for metadata file                                                                                                              0.0s
[+] Running 6/6
 ✔ producer                                         Built                                                                                                          0.0s
 ✔ worker                                           Built                                                                                                          0.0s
 ✔ Network distributed-docker-cluster_default       Created                                                                                                        0.1s
 ✔ Container distributed-docker-cluster-redis-1     Created                                                                                                        3.8s
 ✔ Container distributed-docker-cluster-worker-1    Created                                                                                                        0.6s
 ✔ Container distributed-docker-cluster-producer-1  Created                                                                                                        0.4s
Attaching to producer-1, redis-1, worker-1
redis-1     | 1:C 04 Jul 2026 00:23:27.627 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis-1     | 1:C 04 Jul 2026 00:23:27.627 * Redis version=7.4.8, bits=64, commit=00000000, modified=0, pid=1, just started
redis-1     | 1:C 04 Jul 2026 00:23:27.627 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis-1     | 1:M 04 Jul 2026 00:23:27.635 * monotonic clock: POSIX clock_gettime
redis-1     | 1:M 04 Jul 2026 00:23:27.638 * Running mode=standalone, port=6379.
redis-1     | 1:M 04 Jul 2026 00:23:27.640 * Server initialized
redis-1     | 1:M 04 Jul 2026 00:23:27.640 * Ready to accept connections tcp
worker-1    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-1    | absolutely not recommended!
worker-1    |
worker-1    | Please specify a different user using the --uid option.
worker-1    |
worker-1    | User information: uid=0 euid=0 gid=0 egid=0
worker-1    |
worker-1    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-1    |
worker-1    |  -------------- celery@9c287b7d4620 v5.6.3 (recovery)
worker-1    | --- ***** -----
worker-1    | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-04 00:23:33
worker-1    | - *** --- * ---
worker-1    | - ** ---------- [config]
worker-1    | - ** ---------- .> app:         tasks:0x7fef2df0dad0
worker-1    | - ** ---------- .> transport:   redis://redis:6379/0
worker-1    | - ** ---------- .> results:     redis://redis:6379/0
worker-1    | - *** --- * --- .> concurrency: 4 (prefork)
worker-1    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-1    | --- ***** -----
worker-1    |  -------------- [queues]
worker-1    |                 .> celery           exchange=celery(direct) key=celery
worker-1    |
worker-1    |
worker-1    | [tasks]
worker-1    |   . tasks.generate_k_square_numbers
worker-1    |
worker-1    | [2026-07-04 00:23:33,497: INFO/MainProcess] Connected to redis://redis:6379/0
worker-1    | [2026-07-04 00:23:33,508: INFO/MainProcess] mingle: searching for neighbors
worker-1    | [2026-07-04 00:23:34,536: INFO/MainProcess] mingle: all alone
worker-1    | [2026-07-04 00:23:34,591: INFO/MainProcess] celery@9c287b7d4620 ready.
worker-1    | [2026-07-04 00:23:39,319: INFO/MainProcess] Task tasks.generate_k_square_numbers[3559a316-0b93-4b2e-82ac-fd1226819dd2] received
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
producer-1 exited with code 0
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 3/3 Desktop   o View Config   w Enable Watch
 ✔ Container distributed-docker-cluster-producer-1  Stopped                                                                                                        0.0s
 ✔ Container distributed-docker-cluster-worker-1    Stopped                                                                                                        3.3s
 ✔ Container distributed-docker-cluster-redis-1     Stopped                                                                                                        0.8s
```