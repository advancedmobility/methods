target: exec

build: 
	docker build . -t clrnet_ra --no-cache

run:
	docker run -it --name clrnet_ra -d --gpus all --shm-size=8g -v /path/to/data:/shared_host clrnet_ra
	
start:
	docker container start clrnet_ra

exec:
	docker exec -it clrnet_ra "./call_clrnet.sh"
