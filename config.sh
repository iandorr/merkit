#!/bin/bash

# common paths for scripts

GIT_REPO=
DIR=
REPO_DIR=
REQUIREMENTS=
CONFIG=

# allowed_hosts (IP and domain names), use formal IP="['a','b']"
IP=

DATABASE_ENGINE=

# set these variables
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=

RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_PRIVATE_KEY=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

PYTHON_VERSION=

# end of set

if [ "$PYTHON_VERSION" == "3" ]; then
    PYTHON="python3"
    PIP="pip3"
else
    PYTHON="python"
    PIP="pip"
fi