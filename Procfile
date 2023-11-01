primary: bin/litefs mount -config etc/primary.yml
secondary_1: bin/litefs mount -config etc/secondary_1.yml
secondary_2: bin/litefs mount -config etc/secondary_2.yml
enrollment_1: uvicorn --port 5300 main:app --reload
enrollment_2: uvicorn --port 5400 main:app --reload
enrollment_3: uvicorn --port 5500 main:app --reload
krakend:  echo krakend.json | entr -nrz krakend run --config krakend.json --port 8080
