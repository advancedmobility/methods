target: exec

build:
	docker build . -t amsign_ocr

run:
	docker run -it -d --gpus all --shm-size=8g -v $(AMSIGN_CODE):/project -v $(AMSIGN_DATA):/data --name amsign_ra amsign_ocr:latest
	
run_new:
	docker run -it -d --gpus all --shm-size=8g -v $(AMSIGN_CODE):/project -v $(AMSIGN_DATA):/data --name amsign_ra trc-am/amsign_ra:202506exported bash

start:
	docker container start amsign_ra

exec:
	docker exec -it amsign_ra python /project/am_sign_inference_ocr.py $(AMSIGN_ARGS)
	
