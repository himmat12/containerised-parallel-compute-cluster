# Single worker computation logs

```
(.venv) PS C:\Users\himmat\Desktop\2026\coding\distributed-docker-cluster> docker compose up --build --watch
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 7.2s (19/19) FINISHED                                                                                                                 docker:desktop-linux
 => [worker internal] load build definition from Dockerfile                                                                                                        0.1s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load metadata for docker.io/library/python:3.11-slim                                                                                       0.9s
 => [worker internal] load .dockerignore                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer 1/5] FROM docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                 0.8s
 => => resolve docker.io/library/python:3.11-slim@sha256:b27df5841f3355e9473f9a516d38a6783b6c8dfeacaf2d14a240f443b368ddb6                                          0.5s
 => [worker internal] load build context                                                                                                                           0.9s
 => => transferring context: 423.08kB                                                                                                                              0.9s
 => CACHED [producer 2/5] WORKDIR /app                                                                                                                             0.0s
 => CACHED [worker 3/5] COPY ./requirements.txt .                                                                                                                  0.0s
 => CACHED [worker 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                         0.0s
 => CACHED [worker 5/5] COPY . .                                                                                                                                   0.0s
 => [worker] exporting to image                                                                                                                                    0.2s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:557a35685f894b4c051e3c7ed872f21e342c50472ac897e5170cef3992cd92b4                                                                  0.0s
 => => exporting config sha256:3e697f3852eb038236f58c42fe5ad0614e0ffd4f197720a0724a5c677035537f                                                                    0.0s
 => => exporting attestation manifest sha256:5ae1e36864d6f01c16247274a1f5ee37ca64df00e0f42e917c342a6931ecf843                                                      0.0s
 => => exporting manifest list sha256:c98c0b4f75eca4a6593092f3d340568f64edb628c48609ce0367340fdf737ba6                                                             0.0s
 => => naming to docker.io/library/distributed-docker-cluster-worker:latest                                                                                        0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-worker:latest                                                                                     0.0s
 => [worker] resolving provenance for metadata file                                                                                                                0.0s
 => [producer internal] load build definition from Dockerfile                                                                                                      0.1s
 => => transferring dockerfile: 233B                                                                                                                               0.0s
 => [producer internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [producer internal] load build context                                                                                                                         1.2s
 => => transferring context: 423.08kB                                                                                                                              1.1s
 => CACHED [producer 3/5] COPY ./requirements.txt .                                                                                                                0.0s
 => CACHED [producer 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                       0.0s
 => CACHED [producer 5/5] COPY . .                                                                                                                                 0.0s
 => [producer] exporting to image                                                                                                                                  0.3s
 => => exporting layers                                                                                                                                            0.0s
 => => exporting manifest sha256:2fd6330269f0da879d3148f39351a1a2fb4f0119e57c90317f1106b02b89ab81                                                                  0.0s
 => => exporting config sha256:a3fb3be8ca9057b0cafab6956a3a3d4d024a205d22a1b36cc89d6d0dc6e065d3                                                                    0.0s
 => => exporting attestation manifest sha256:7a9d65b03177351cf4fc5322dd154c9bb72646c4e981bc353c853292c53dbeba                                                      0.0s
 => => exporting manifest list sha256:b1875509710338e1813a4e79b2c5a41b0e9d8974a18157179886bbc08aaf7693                                                             0.0s
 => => naming to docker.io/library/distributed-docker-cluster-producer:latest                                                                                      0.0s
 => => unpacking to docker.io/library/distributed-docker-cluster-producer:latest                                                                                   0.0s
 => [producer] resolving provenance for metadata file                                                                                                              0.1s
[+] Running 8/8
 ✔ producer                                         Built                                                                                                          0.0s
 ✔ worker                                           Built                                                                                                          0.0s
 ✔ Container distributed-docker-cluster-redis-1     Created                                                                                                        0.0s
 ✔ Container distributed-docker-cluster-producer-1  Recreated                                                                                                      3.2s
 ✔ Container distributed-docker-cluster-worker-14   Removed                                                                                                        0.4s
 ✔ Container distributed-docker-cluster-worker-21   Recreated                                                                                                      2.2s
 ✔ Container distributed-docker-cluster-worker-18   Removed                                                                                                        1.5s
 ✔ Container distributed-docker-cluster-worker-22   Removed                                                                                                        0.7s
Attaching to producer-1, redis-1, worker-21
redis-1     | 1:C 05 Jul 2026 20:12:40.027 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis-1     | 1:C 05 Jul 2026 20:12:40.027 * Redis version=7.4.8, bits=64, commit=00000000, modified=0, pid=1, just started
redis-1     | 1:C 05 Jul 2026 20:12:40.027 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis-1     | 1:M 05 Jul 2026 20:12:40.027 * monotonic clock: POSIX clock_gettime
redis-1     | 1:M 05 Jul 2026 20:12:40.043 * Running mode=standalone, port=6379.
redis-1     | 1:M 05 Jul 2026 20:12:40.047 * Server initialized
redis-1     | 1:M 05 Jul 2026 20:12:40.048 * Loading RDB produced by version 7.4.8
redis-1     | 1:M 05 Jul 2026 20:12:40.048 * RDB age 21 seconds
redis-1     | 1:M 05 Jul 2026 20:12:40.048 * RDB memory usage when created 4.74 Mb
redis-1     | 1:M 05 Jul 2026 20:12:40.083 * Done loading RDB, keys loaded: 155, keys expired: 0.
redis-1     | 1:M 05 Jul 2026 20:12:40.084 * DB loaded from disk: 0.036 seconds
redis-1     | 1:M 05 Jul 2026 20:12:40.084 * Ready to accept connections tcp
worker-21   | /usr/local/lib/python3.11/site-packages/celery/platforms.py:841: SecurityWarning: You're running the worker with superuser privileges: this is
worker-21   | absolutely not recommended!
worker-21   |
worker-21   | Please specify a different user using the --uid option.
worker-21   |
worker-21   | User information: uid=0 euid=0 gid=0 egid=0
worker-21   |
worker-21   |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-21   |
worker-21   |  -------------- celery@3e50ab6635b3 v5.6.3 (recovery)
worker-21   | --- ***** -----
worker-21   | -- ******* ---- Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.41 2026-07-05 20:12:44
worker-21   | - *** --- * ---
worker-21   | - ** ---------- [config]
worker-21   | - ** ---------- .> app:         tasks:0x7f34a78b8d50
worker-21   | - ** ---------- .> transport:   redis://redis:6379/0
worker-21   | - ** ---------- .> results:     redis://redis:6379/0
worker-21   | - *** --- * --- .> concurrency: 1 (prefork)
worker-21   | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-21   | --- ***** -----
worker-21   |  -------------- [queues]
worker-21   |                 .> celery           exchange=celery(direct) key=celery
worker-21   |
worker-21   |
worker-21   | [tasks]
worker-21   |   . tasks.get_prime_factors_chunk
worker-21   |
worker-21   | [2026-07-05 20:12:44,918: INFO/MainProcess] Connected to redis://redis:6379/0
worker-21   | [2026-07-05 20:12:44,936: INFO/MainProcess] mingle: searching for neighbors
worker-21   | [2026-07-05 20:12:45,989: INFO/MainProcess] mingle: all alone
worker-21   | [2026-07-05 20:12:46,078: INFO/MainProcess] celery@3e50ab6635b3 ready.
worker-21   | [2026-07-05 20:12:48,326: INFO/MainProcess] Task tasks.get_prime_factors_chunk[081dc40f-7c9c-46d5-b1fc-189d466ed764] received
worker-21   | [2026-07-05 20:12:48,331: INFO/MainProcess] Task tasks.get_prime_factors_chunk[bc4070ed-85af-447a-94e3-8e71339e9600] received
worker-21   | [2026-07-05 20:12:48,344: INFO/MainProcess] Task tasks.get_prime_factors_chunk[b99c50eb-3832-40d7-a132-11a0f87e850e] received
worker-21   | [2026-07-05 20:12:48,351: INFO/MainProcess] Task tasks.get_prime_factors_chunk[2424ffb7-7a2d-47b9-bd82-f8bdd54ac76c] received
worker-21   | [2026-07-05 20:12:48,379: INFO/MainProcess] Task tasks.get_prime_factors_chunk[840596ef-4c02-42c2-aa93-76c029389c40] received
worker-21   | [2026-07-05 20:13:00,241: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[081dc40f-7c9c-46d5-b1fc-189d466ed764] succeeded in 11.897515505006595s: [{'n': 6060, 'factors': [2, 2, 3, 5, 101]}, {'n': 571708, 'factors': [2, 2, 47, 3041]}, {'n': 151564, 'factors': [2, 2, 7, 5413]}, {'n': 117011, 'factors': [17, 6883]}, {'n': 982989, 'factors': [3, 3, 3, 7, 7, 743]}, {'n': 856881, 'factors': [3, 3, 19, 5011]}, {'n': 832911, 'factors': [3, 277637]}, {'n': 709929, 'factors': [3, 3, 11, 71, 101]}, {'n': 219826, 'factors': [2, 109913]}, {'n': 327483, 'factors': [3, 3, 3, 3, 13, 311]}, {'n': 234750, 'factors': [2, 3, 5, 5, 5, 313]}, {'n': 404076, 'factors': [2, 2, 3, 151, 223]}, {'n': 474038, 'factors': [2, 237019]}, {'n': 421908, 'factors': [2, 2, 3, 35159]}, {'n': 153039, 'factors': [3, 139, 367]}, {'n': 832830, 'factors': [2, 3, 5, 17, 23, 71]}, {'n': 580226, 'factors': [2, 290113]}, {'n': 577000, 'factors': [2, 2, 2, 5, 5, 5, 577]}, {'n': 361868, 'factors': [2, 2, 13, 6959]}, {'n': 957432, 'factors': [2, 2, 2, 3, 7, 41, 139]}, {'n': 446577, 'factors': [3, 148859]}, {'n': 727163, 'factors': [83, 8761]}, {'n': 881103, 'factors': [3, 293701]}, {'n': 14317, 'factor...', ...}]
worker-21   | [2026-07-05 20:13:00,248: INFO/MainProcess] Task tasks.get_prime_factors_chunk[c571f157-ee6e-49b7-ad06-a52a32756210] received
worker-21   | [2026-07-05 20:13:10,361: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[bc4070ed-85af-447a-94e3-8e71339e9600] succeeded in 10.117482919995382s: [{'n': 416447, 'factors': [61, 6827]}, {'n': 573874, 'factors': [2, 7, 179, 229]}, {'n': 947010, 'factors': [2, 3, 5, 31567]}, {'n': 207557, 'factors': [7, 149, 199]}, {'n': 306973, 'factors': [251, 1223]}, {'n': 413415, 'factors': [3, 3, 5, 9187]}, {'n': 254145, 'factors': [3, 5, 16943]}, {'n': 584168, 'factors': [2, 2, 2, 13, 41, 137]}, {'n': 310003, 'factors': [151, 2053]}, {'n': 774707, 'factors': [17, 199, 229]}, {'n': 857282, 'factors': [2, 499, 859]}, {'n': 329846, 'factors': [2, 11, 11, 29, 47]}, {'n': 17161, 'factors': [131, 131]}, {'n': 990023, 'factors': [990023]}, {'n': 131828, 'factors': [2, 2, 32957]}, {'n': 148486, 'factors': [2, 13, 5711]}, {'n': 365894, 'factors': [2, 113, 1619]}, {'n': 513770, 'factors': [2, 5, 83, 619]}, {'n': 118148, 'factors': [2, 2, 29537]}, {'n': 37980, 'factors': [2, 2, 3, 3, 5, 211]}, {'n': 496633, 'factors': [41, 12113]}, {'n': 782467, 'factors': [7, 111781]}, {'n': 269096, 'factors': [2, 2, 2, 33637]}, {'n': 511880, 'factors': [2, 2, 2, 5, 67, 191]}, {'n': 223916, 'f...', ...}]
worker-21   | [2026-07-05 20:13:10,371: INFO/MainProcess] Task tasks.get_prime_factors_chunk[a123d258-5990-478d-8ca3-b1d10c905dc7] received
worker-21   | [2026-07-05 20:13:19,570: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[b99c50eb-3832-40d7-a132-11a0f87e850e] succeeded in 9.205908158000966s: [{'n': 756812, 'factors': [2, 2, 7, 151, 179]}, {'n': 577681, 'factors': [13, 37, 1201]}, {'n': 916296, 'factors': [2, 2, 2, 3, 73, 523]}, {'n': 148564, 'factors': [2, 2, 13, 2857]}, {'n': 970056, 'factors': [2, 2, 2, 3, 3, 3, 3, 3, 499]}, {'n': 72871, 'factors': [72871]}, {'n': 670604, 'factors': [2, 2, 11, 15241]}, {'n': 452355, 'factors': [3, 5, 53, 569]}, {'n': 986049, 'factors': [3, 3, 331, 331]}, {'n': 929204, 'factors': [2, 2, 233, 997]}, {'n': 701955, 'factors': [3, 3, 5, 19, 821]}, {'n': 621923, 'factors': [621923]}, {'n': 835662, 'factors': [2, 3, 41, 43, 79]}, {'n': 554788, 'factors': [2, 2, 13, 47, 227]}, {'n': 724059, 'factors': [3, 3, 3, 3, 7, 1277]}, {'n': 694974, 'factors': [2, 3, 7, 16547]}, {'n': 426598, 'factors': [2, 17, 12547]}, {'n': 46896, 'factors': [2, 2, 2, 2, 3, 977]}, {'n': 459862, 'factors': [2, 13, 23, 769]}, {'n': 866586, 'factors': [2, 3, 7, 47, 439]}, {'n': 148547, 'factors': [7, 21221]}, {'n': 451741, 'factors': [17, 26573]}, {'n': 665012, 'factors': [2, 2, 31, 31, 173]}, {'n', ...}]
worker-21   | [2026-07-05 20:13:19,580: INFO/MainProcess] Task tasks.get_prime_factors_chunk[05d71af9-d5ea-44ae-88d9-b163edb10e11] received
worker-21   | [2026-07-05 20:13:28,879: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[2424ffb7-7a2d-47b9-bd82-f8bdd54ac76c] succeeded in 9.304892989006476s: [{'n': 90350, 'factors': [2, 5, 5, 13, 139]}, {'n': 888391, 'factors': [7, 126913]}, {'n': 358382, 'factors': [2, 29, 37, 167]}, {'n': 262460, 'factors': [2, 2, 5, 11, 1193]}, {'n': 135078, 'factors': [2, 3, 47, 479]}, {'n': 778891, 'factors': [127, 6133]}, {'n': 703605, 'factors': [3, 5, 7, 6701]}, {'n': 925549, 'factors': [199, 4651]}, {'n': 117481, 'factors': [7, 13, 1291]}, {'n': 481186, 'factors': [2, 47, 5119]}, {'n': 970975, 'factors': [5, 5, 38839]}, {'n': 759243, 'factors': [3, 253081]}, {'n': 414288, 'factors': [2, 2, 2, 2, 3, 3, 3, 7, 137]}, {'n': 65851, 'factors': [65851]}, {'n': 939826, 'factors': [2, 23, 20431]}, {'n': 812171, 'factors': [367, 2213]}, {'n': 600332, 'factors': [2, 2, 150083]}, {'n': 60999, 'factors': [3, 20333]}, {'n': 976023, 'factors': [3, 3, 3, 37, 977]}, {'n': 926978, 'factors': [2, 13, 101, 353]}, {'n': 73533, 'factors': [3, 127, 193]}, {'n': 36164, 'factors': [2, 2, 9041]}, {'n': 277115, 'factors': [5, 19, 2917]}, {'n': 754078, 'factors': [2, 13, 13, 23, 97]}, {'n': 18517, , ...}]
worker-21   | [2026-07-05 20:13:28,886: INFO/MainProcess] Task tasks.get_prime_factors_chunk[ccf224f7-fbc5-4015-94c3-af18a50a18bc] received
worker-21   | [2026-07-05 20:13:39,528: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[840596ef-4c02-42c2-aa93-76c029389c40] succeeded in 10.643651867998415s: [{'n': 621617, 'factors': [621617]}, {'n': 936415, 'factors': [5, 19, 9857]}, {'n': 146547, 'factors': [3, 3, 19, 857]}, {'n': 740124, 'factors': [2, 2, 3, 3, 3, 7, 11, 89]}, {'n': 309276, 'factors': [2, 2, 3, 3, 11, 11, 71]}, {'n': 485817, 'factors': [3, 67, 2417]}, {'n': 621469, 'factors': [17, 139, 263]}, {'n': 190227, 'factors': [3, 63409]}, {'n': 468138, 'factors': [2, 3, 11, 41, 173]}, {'n': 64333, 'factors': [64333]}, {'n': 343913, 'factors': [343913]}, {'n': 238701, 'factors': [3, 251, 317]}, {'n': 906865, 'factors': [5, 17, 47, 227]}, {'n': 220152, 'factors': [2, 2, 2, 3, 9173]}, {'n': 452919, 'factors': [3, 43, 3511]}, {'n': 660310, 'factors': [2, 5, 7, 9433]}, {'n': 376163, 'factors': [389, 967]}, {'n': 91854, 'factors': [2, 3, 3, 3, 3, 3, 3, 3, 3, 7]}, {'n': 185295, 'factors': [3, 5, 11, 1123]}, {'n': 844214, 'factors': [2, 7, 47, 1283]}, {'n': 156890, 'factors': [2, 5, 29, 541]}, {'n': 464182, 'factors': [2, 232091]}, {'n': 520093, 'factors': [7, 191, 389]}, {'n': 888918, 'factors': [2, 3, 148153..., ...}]
worker-21   | [2026-07-05 20:13:39,535: INFO/MainProcess] Task tasks.get_prime_factors_chunk[41650263-736c-403d-8712-6608b323f6f3] received
worker-21   | [2026-07-05 20:13:50,125: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[c571f157-ee6e-49b7-ad06-a52a32756210] succeeded in 10.594064495002385s: [{'n': 517638, 'factors': [2, 3, 11, 11, 23, 31]}, {'n': 998334, 'factors': [2, 3, 3, 37, 1499]}, {'n': 238876, 'factors': [2, 2, 11, 61, 89]}, {'n': 35760, 'factors': [2, 2, 2, 2, 3, 5, 149]}, {'n': 996820, 'factors': [2, 2, 5, 11, 23, 197]}, {'n': 459725, 'factors': [5, 5, 7, 37, 71]}, {'n': 73908, 'factors': [2, 2, 3, 3, 2053]}, {'n': 526572, 'factors': [2, 2, 3, 3, 14627]}, {'n': 550695, 'factors': [3, 5, 36713]}, {'n': 450557, 'factors': [450557]}, {'n': 931683, 'factors': [3, 29, 10709]}, {'n': 700002, 'factors': [2, 3, 3, 3, 3, 29, 149]}, {'n': 14319, 'factors': [3, 3, 37, 43]}, {'n': 617914, 'factors': [2, 11, 28087]}, {'n': 38470, 'factors': [2, 5, 3847]}, {'n': 107437, 'factors': [11, 9767]}, {'n': 119900, 'factors': [2, 2, 5, 5, 11, 109]}, {'n': 205064, 'factors': [2, 2, 2, 25633]}, {'n': 699815, 'factors': [5, 67, 2089]}, {'n': 449443, 'factors': [23, 19541]}, {'n': 43500, 'factors': [2, 2, 3, 5, 5, 5, 29]}, {'n': 151446, 'factors': [2, 3, 43, 587]}, {'n': 576716, 'factors': [2, 2, 7, 43, 479]}, {, ...}]
worker-21   | [2026-07-05 20:14:00,615: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[a123d258-5990-478d-8ca3-b1d10c905dc7] succeeded in 10.488595016002364s: [{'n': 66730, 'factors': [2, 5, 6673]}, {'n': 85881, 'factors': [3, 28627]}, {'n': 879423, 'factors': [3, 433, 677]}, {'n': 273553, 'factors': [7, 39079]}, {'n': 992294, 'factors': [2, 19, 26113]}, {'n': 819055, 'factors': [5, 163811]}, {'n': 865196, 'factors': [2, 2, 73, 2963]}, {'n': 622355, 'factors': [5, 124471]}, {'n': 380100, 'factors': [2, 2, 3, 5, 5, 7, 181]}, {'n': 497135, 'factors': [5, 19, 5233]}, {'n': 83500, 'factors': [2, 2, 5, 5, 5, 167]}, {'n': 670634, 'factors': [2, 23, 61, 239]}, {'n': 431525, 'factors': [5, 5, 41, 421]}, {'n': 885469, 'factors': [13, 68113]}, {'n': 314665, 'factors': [5, 13, 47, 103]}, {'n': 27299, 'factors': [27299]}, {'n': 370551, 'factors': [3, 123517]}, {'n': 150811, 'factors': [23, 79, 83]}, {'n': 440435, 'factors': [5, 59, 1493]}, {'n': 692171, 'factors': [43, 16097]}, {'n': 695673, 'factors': [3, 3, 11, 7027]}, {'n': 909748, 'factors': [2, 2, 7, 32491]}, {'n': 86472, 'factors': [2, 2, 2, 3, 3, 1201]}, {'n': 100610, 'factors': [2, 5, 10061]}, {'n': 125333, 'factors': , ...]}]
worker-21   | [2026-07-05 20:14:11,377: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[05d71af9-d5ea-44ae-88d9-b163edb10e11] succeeded in 10.759250745999452s: [{'n': 616274, 'factors': [2, 308137]}, {'n': 971779, 'factors': [79, 12301]}, {'n': 452887, 'factors': [457, 991]}, {'n': 850061, 'factors': [850061]}, {'n': 606877, 'factors': [149, 4073]}, {'n': 331043, 'factors': [331043]}, {'n': 844144, 'factors': [2, 2, 2, 2, 7, 7537]}, {'n': 249482, 'factors': [2, 79, 1579]}, {'n': 265635, 'factors': [3, 3, 5, 5903]}, {'n': 13711, 'factors': [13711]}, {'n': 73474, 'factors': [2, 17, 2161]}, {'n': 954933, 'factors': [3, 7, 37, 1229]}, {'n': 272300, 'factors': [2, 2, 5, 5, 7, 389]}, {'n': 965467, 'factors': [965467]}, {'n': 330183, 'factors': [3, 3, 3, 7, 1747]}, {'n': 763250, 'factors': [2, 5, 5, 5, 43, 71]}, {'n': 9347, 'factors': [13, 719]}, {'n': 296226, 'factors': [2, 3, 3, 7, 2351]}, {'n': 554500, 'factors': [2, 2, 5, 5, 5, 1109]}, {'n': 818106, 'factors': [2, 3, 136351]}, {'n': 738204, 'factors': [2, 2, 3, 227, 271]}, {'n': 533731, 'factors': [11, 11, 11, 401]}, {'n': 248164, 'factors': [2, 2, 7, 8863]}, {'n': 500567, 'factors': [500567]}, {'n': 61432, 'factors': , ...]}]
worker-21   | [2026-07-05 20:14:20,659: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[ccf224f7-fbc5-4015-94c3-af18a50a18bc] succeeded in 9.279048483003862s: [{'n': 73755, 'factors': [3, 3, 5, 11, 149]}, {'n': 672687, 'factors': [3, 3, 41, 1823]}, {'n': 339604, 'factors': [2, 2, 59, 1439]}, {'n': 269181, 'factors': [3, 3, 11, 2719]}, {'n': 550643, 'factors': [23, 89, 269]}, {'n': 448330, 'factors': [2, 5, 107, 419]}, {'n': 977105, 'factors': [5, 73, 2677]}, {'n': 486794, 'factors': [2, 7, 11, 29, 109]}, {'n': 71872, 'factors': [2, 2, 2, 2, 2, 2, 1123]}, {'n': 468728, 'factors': [2, 2, 2, 13, 4507]}, {'n': 992993, 'factors': [487, 2039]}, {'n': 489805, 'factors': [5, 97961]}, {'n': 988639, 'factors': [29, 73, 467]}, {'n': 123345, 'factors': [3, 3, 5, 2741]}, {'n': 522547, 'factors': [181, 2887]}, {'n': 688912, 'factors': [2, 2, 2, 2, 7, 6151]}, {'n': 528221, 'factors': [167, 3163]}, {'n': 112420, 'factors': [2, 2, 5, 7, 11, 73]}, {'n': 428793, 'factors': [3, 37, 3863]}, {'n': 683175, 'factors': [3, 5, 5, 9109]}, {'n': 354631, 'factors': [67, 67, 79]}, {'n': 73443, 'factors': [3, 24481]}, {'n': 758123, 'factors': [211, 3593]}, {'n': 732998, 'factors': [2, 7, 41, 127..., ...}]
worker-21   | [2026-07-05 20:14:29,826: INFO/ForkPoolWorker-1] Task tasks.get_prime_factors_chunk[41650263-736c-403d-8712-6608b323f6f3] succeeded in 9.166990180005087s: [{'n': 100357, 'factors': [100357]}, {'n': 748244, 'factors': [2, 2, 7, 26723]}, {'n': 845091, 'factors': [3, 3, 13, 31, 233]}, {'n': 949227, 'factors': [3, 397, 797]}, {'n': 501222, 'factors': [2, 3, 83537]}, {'n': 578384, 'factors': [2, 2, 2, 2, 37, 977]}, {'n': 699052, 'factors': [2, 2, 174763]}, {'n': 486158, 'factors': [2, 43, 5653]}, {'n': 838181, 'factors': [263, 3187]}, {'n': 235939, 'factors': [11, 89, 241]}, {'n': 167287, 'factors': [131, 1277]}, {'n': 52233, 'factors': [3, 23, 757]}, {'n': 518306, 'factors': [2, 337, 769]}, {'n': 290655, 'factors': [3, 3, 3, 5, 2153]}, {'n': 170229, 'factors': [3, 179, 317]}, {'n': 737518, 'factors': [2, 23, 16033]}, {'n': 777729, 'factors': [3, 41, 6323]}, {'n': 378817, 'factors': [378817]}, {'n': 623169, 'factors': [3, 3, 17, 4073]}, {'n': 241087, 'factors': [7, 11, 31, 101]}, {'n': 471621, 'factors': [3, 157207]}, {'n': 531664, 'factors': [2, 2, 2, 2, 7, 47, 101]}, {'n': 855103, 'factors': [199, 4297]}, {'n': 513104, 'factors': [2, 2, 2, 2, 32069]}, {'n': 903532..., ...}]
producer-1  |
producer-1  |
producer-1  | [Producer] Dispatching tasks...
producer-1  |
producer-1  |
producer-1  | [Producer] Tasks queued successfully. Gathering results...
producer-1  |
producer-1  |
producer-1  |
producer-1  | ================================================================================
producer-1  | Distributed Compute Completed!
producer-1  | Total Processing Time: 101.75 seconds
producer-1  | ================================================================================
producer-1 exited with code 0
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 3/3 Desktop   o View Config   w Enable Watch
 ✔ Container distributed-docker-cluster-producer-1  Stopped                                                                                                        0.0s
 ✔ Container distributed-docker-cluster-worker-21   Stopped                                                                                                        3.3s
 ✔ Container distributed-docker-cluster-redis-1     Stopped                                                                                                        0.9s

(.venv) PS C:\Users\himmat\Desktop\2026\coding\distributed-docker-cluster>

```