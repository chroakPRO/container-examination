# What docker image that will be used
FROM python:3.10-slim

# Args
ARG SERVER_FILE="main.py"
ARG MAINTAINER="Christopher Ek"
ARG AUTHOR="Christopher Ek"
ARG PORT_LISTEN="8000"

ENV FILE=$SERVER_FILE


# Labels
LABEL author=$AUTHOR
LABEL maintainer=$MAINTAINER
LABEL version="0.1"
LABEL desc="Lorem ipsum"

# Create a new directory and make that the working directory
WORKDIR /app

# Copy all files from the current directory to the /app directory
COPY * .

# Update and install all packages
RUN pip install -r requirements.lock && rm -rf requirements.lock

# Expose the port
EXPOSE 8000

# Run the app
CMD ["/bin/sh", "-c", "python $FILE"]

