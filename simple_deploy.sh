#!/bin/bash

RED='\033[1;31m' 
GREEN='\033[1;32m'
YELLOW='\033[1;33m'

NORMAL='\033[0m'

read -p "$(printf "${YELLOW}WARNING${NORMAL}: Are you sure you are in an environment [y/n]?") " yn

CORRECT = true

case $yn in
    [Yy]* ) ;;
    [Nn]* ) exit 1;;
    * ) exit 1;;
esac


if test -f config.sh && source config.sh;then
    printf "\n${GREEN}INFO${NORMAL}: Config sourced.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Error sourcing config, are you sure there is config.sh?\n"
    exit 1
fi


# bash for first time setup

# Clone repository

if ! test -d "$DIR"; then
    mkdir $DIR
    cd $DIR
fi

if git pull; then
    printf "\n${GREEN}INFO${NORMAL}: Git pulled.\n"
elif git clone $GIT_REPO .; then
    printf "\n${GREEN}INFO${NORMAL}: Git cloned.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Error pulling git, check if correct repository.\n"
    exit 1
fi

# working for git > 1.8.5
# if git -C $DIR pull || git clone $GIT_REPO $DIR; then
#     printf "\n${GREEN}INFO${NORMAL}: Git pulled.\n"
# else
#     printf "\n${RED}ERROR${NORMAL}: Error pulling git, check if correct repository.\n"
#     exit 1
# fi

#cd $DIR

if ! test -z "$REPO_DIR";then
    cd $REPO_DIR
fi

# Install dependencies

if test -f "$REQUIREMENTS"; then
    if $PIP install -r $REQUIREMENTS; then
        printf "\n${GREEN}INFO${NORMAL}: Dependencies installed.\n"
    else
        printf "\n${RED}ERROR${NORMAL}: At least one dependency installed incorrectly.\n"
        CORRECT = false
    fi
else 
    printf "\n${RED}ERROR${NORMAL}: Dependecies list missing.\n"
    CORRECT = false
fi

# Set up secret key, database, ... (.env file)

if test -f "$CONFIG"; then
    printf "\n${YELLOW}WARNING${NORMAL}: Env already created --> skipping\n"
    # TODO: maybe check if smt not missing
else
    touch $CONFIG
    # generating debug
    echo -e "DEBUG = 'False'" >> $CONFIG
    printf "\n${GREEN}INFO${NORMAL}: DEBUG set.\n"
    # generating secret key
    DJANGO_SECRET_KEY_VALUE=`openssl rand -base64 48`
    DJANGO_SECRET_KEY="SECRET_KEY='"$DJANGO_SECRET_KEY_VALUE"'"
    echo -e $DJANGO_SECRET_KEY >> $CONFIG
    printf "\n${GREEN}INFO${NORMAL}: Django secret key generated.\n"
    # Allow Hosts
    if ! test -z $IP;then
        echo -e "ALLOWED_HOSTS = $IP" >> $CONFIG
    else
        IP=$(hostname -I | head -n1 | cut -d " " -f1)
	    printf "\n${YELLOW}WARNING${NORMAL}: IP not set, reversing to $IP.\n"
	    echo -e "ALLOWED_HOSTS = ['$IP']" >> $CONFIG
    fi
    printf "\n${GREEN}INFO${NORMAL}: Allowed hosts set up.\n"

    # generating recaptcha data
    if ! test -z "$RECAPTCHA_PUBLIC_KEY" && ! test -z "$RECAPTCHA_PRIVATE_KEY";then
        echo -e "RECAPTCHA_PUBLIC_KEY='"$RECAPTCHA_PUBLIC_KEY"'" >> $CONFIG
        echo -e "RECAPTCHA_PRIVATE_KEY='"$RECAPTCHA_PRIVATE_KEY"'" >> $CONFIG
        printf "\n${GREEN}INFO${NORMAL}: Recaptcha set.\n"
    else
        printf "\n${RED}ERROR${NORMAL}: Recaptcha not set --> skipping\n"
        CORRECT = false
    fi
    # generating database
    if ! test -z "$DATABASE_NAME" && ! test -z "$DATABASE_USER" && ! test -z "$DATABASE_PASSWORD" && ! test -z "$DATABASE_HOST" && ! test -z "$DATABASE_ENGINE"; then
        echo -e "DATABASE_ENGINE='"$DATABASE_ENGINE"'" >> $CONFIG
        echo -e "DATABASE_NAME='"$DATABASE_NAME"'" >> $CONFIG
        echo -e "DATABASE_USER='"$DATABASE_USER"'" >> $CONFIG
        echo -e "DATABASE_PASSWORD='"$DATABASE_PASSWORD"'" >> $CONFIG
        echo -e "DATABASE_HOST='"$DATABASE_HOST"'" >> $CONFIG
        printf "\n${GREEN}INFO${NORMAL}: Database set.\n"
    else
        printf "\n${RED}ERROR${NORMAL}: Database not set --> skipping\n"
        CORRECT = false
    fi
    # generating email info

    if ! test -z "$EMAIL_HOST_USER" && ! test -z "$EMAIL_HOST_PASSWORD";then
        echo -e "EMAIL_HOST_USER='"$EMAIL_HOST_USER"'" >> $CONFIG
        echo -e "EMAIL_HOST_PASSWORD='"$EMAIL_HOST_PASSWORD"'" >> $CONFIG
    else
        printf "\n${RED}ERROR${NORMAL}: Email not set --> skipping\n"
        CORRECT = false
    fi
fi

# django manage

$PYTHON manage.py makemigrations
if $PYTHON manage.py migrate; then
    printf "\n${GREEN}INFO${NORMAL}: Database migration done.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Some problems in database migration.\n"
    CORRECT = false
fi
if $PYTHON manage.py collectstatic;then
    printf "\n${GREEN}INFO${NORMAL}: Static collected.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Some problems in static collection.\n"
    CORRECT = false
fi
if $PYTHON manage.py compilemessages;then
    printf "\n${GREEN}INFO${NORMAL}: Translations compiled.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Some problems in translations compilation.\n"
    CORRECT = false
fi

read -p "$(printf "${YELLOW}WARNING${NORMAL}: Do you want to create a superuser? [y/n]?") " suyn

case $suyn in
    [Yy]* )
        if $PYTHON manage.py createsuperuser;then
            printf "\n${GREEN}INFO${NORMAL}: Superuser created.\n"
        else
            printf "\n${RED}ERROR${NORMAL}: There was a problem in superuser creation.\n"
        fi
    ;;
    * ) ;;
esac

# TODO: do Misa stuff (nginx,wsgi,...)

if $CORRECT; then
    printf "\n${GREEN}INFO${NORMAL}: All done.\n"
else
    printf "\n${RED}ERROR${NORMAL}: Some problems along the way, check the log.\n"
fi
