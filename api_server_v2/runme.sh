docker build \
--tag christopherek/skola-api:latest \
--build-arg PORT_LISTEN="8000" \
--build-arg SERVER_FILE="main.py" . \
&& docker push christopherek/skola-api:latestdocker \
&& docker run -it --rm -P -e PORT_LISTEN=8000 -e SERVER_FILE=main.py christopherek/skola-api:latest
