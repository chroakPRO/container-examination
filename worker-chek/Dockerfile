# What docker image that will be used
FROM jenkins/jenkins:lts:jdk11

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


EXPOSE 8080
EXPOSE 50000


docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts-jdk11
'''