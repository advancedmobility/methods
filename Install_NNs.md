
## Setup Laneline Detection Environment

**Building the docker image**

```bash
cd /path/to/NN_models/lane_detection
make build
```

Edit `Makefile` to specify the data directory to be mounted in the container

```bash
# Makefile
# Change /path/to/data
...

run:
	docker run -it --name clrnet_ra -d --gpus all --shm-size=8g -v /path/to/data:/shared_host clrnet_ra
...
```

Running the docker container based on the image just built
```bash
cd /path/to/NN_models/lane_detection
make run
```

This will create a container named `clrnet_ra`

To execute lane detection script
```bash
cd /path/to/NN_models/lane_detection
make exec
```

In case the container `clrnet_ra` is terminated for any reason, it needs to be started again as follows

```bash
docker start clrnet_ra
```

Then run
```bash
cd /path/to/NN_models/lane_detection
make exec
```


## Setup Sign Detection Environment

Building the docker image

```bash
cd /path/to/NN_models/sign_detection/code/docker
make build
```

Edit `source_env.sh` to specify the required arguments for the container

```bash
# source_env.sh
# Change AMSIGN_DATA and AMSIGN_CODE
export AMSIGN_DATA="/media/dev/TRC_X9/I-70/NN_models/sign_detection/data"
export AMSIGN_CODE="/media/dev/TRC_X9/I-70/NN_models/sign_detection/code"
export AMSIGN_ARGS="--workdir /project/amsign_model --imgdir /data/event_images"
```

Running the docker container based on the image just built
```bash
cd /path/to/NN_models/sign_detection/code/docker
source source_env.sh
make run
```

This will create a container named `amsign_ra`

To execute sign detection script
```bash
cd /path/to/NN_models/sign_detection/code/docker
source source_env.sh
make exec
```

In case the container `amsign_ra` is terminated for any reason, it needs to be started again as follows

```bash
docker start amsign_ra
```

Then run
```bash
cd /path/to/NN_models/sign_detection/code/docker
source source_env.sh
make exec
```
