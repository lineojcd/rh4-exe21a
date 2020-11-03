# rh4-exe21a
Duckietown 2020 RH4 exe 21a

Instructions to reproduce results

### 1. Clone this repository and go to its directory
```bash
git clone https://github.com/lineojcd/rh4-exe21a.git
cd rh4-exe21a
```
### 2. Build docker image in Duckiebot
```bash
dts devel build -f --arch arm32v7 -H MY_ROBOT.local
```

### 3. Run docker image in Duckiebot with the following options
```bash
docker -H MY_ROBOT.local run -it --privileged --rm --net=host duckietown/rh4-exe21a:latest-arm32v7 /bin/bash
```

### 4. After going inside the docker shell, run the python script using the command below
```bash
python3 packages/my_package/src/my_node.py
```

Now, the image stream is publishing.
