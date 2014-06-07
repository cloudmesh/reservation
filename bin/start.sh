#! /bin/sh

mkdir -p ~/data
mongod --noauth --dbpath ~/data --port 27777
