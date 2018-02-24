# Logs Analysis

This is the "logs analysis" project for the Udacity Full Stack Nanodegree Program.

# Project setup
Copy `config.ini.dist` to `config.ini` and insert appropriate content.

Run the `logs-analysis.py` script to get the statistics.

# Docker environment setup
Rename all *.deploy files inside the docker-env folder and insert appropriate content.

Now run `docker-compose up` from the project root directory.
This starts a PostgreSQL and a web server running Adminer.

## Ports
By default the PostgreSQL server listens for connections on `63322`
and the web server on `63323`.

Both ports can be changed by setting the environment variables `PRJ_DB_PORT`
and `PRJ_WEB_PORT` to another port when using `docker-compose`.

## Available environment variables
* `PRJ_DB_NAME` (Default: `logs_analysis`)  
Specify the PostgreSQL database name
* `PRJ_DB_USER` (Default: `logs_analysis`)  
Specify the PostgreSQL database name
* `PRJ_DB_PASS`  
**NOT AN ENVIRONMENT VARIABLE** - The password has to be stored inside `docker-env/db-password.txt`
* `PRJ_DB_PORT` (Default: `63322`)
The port on which the PostgreSQL server listens for external connections
* `PRJ_WEB_PORT` (Default: `63323`)
The port on which the web server (running Adminer) listens for external connections