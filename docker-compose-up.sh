#!/bin/bash

if [ $1 != "prod" ] && [ $1 != "dev" ] && [ $1 != "seed" ]
then
    echo -e "ERROR Invalid entry\nAllowed values: [prod, dev, seed]"
    exit 1
fi

if [ $1 == "seed" ]
then
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --rm web sh -c "cd /app && python -c 'from modules import db; db.init_db()'"
else
    docker-compose -f docker-compose.yml -f docker-compose.$1.yml up --build --force-recreate
fi
