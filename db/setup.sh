#!/bin/bash

# get script location
APP_ROOT=$(dirname $(basename $0))

# ensure sqlite3 is installed
#sudo apt update
#sudo apt install sqlite3

# setup database
SQLITE_DB_FILE="$APP_ROOT/db/db.db"
SQLITE_DB_INIT_SCRIPT="$APP_ROOT/db/init.sql"

# run the SQL init script to set up tables
sqlite3 "$SQLITE_DB_FILE" ".read $SQLITE_DB_INIT_SCRIPT"
