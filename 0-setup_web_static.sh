#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

if ! [ "$(command -v nginx)" ]
then
        sudo apt-get -y update && apt-get install -y nginx
        sudo service nginx start
fi

if ! [ -d "/data" ]; then sudo mkdir -p /data/; fi
if ! [ -d "/data/web_static/" ]; then sudo mkdir -p /data/web_static/; fi
if ! [ -d "/data/web_static/releases/" ]; then sudo mkdir -p /data/web_static/releases/; fi
if ! [ -d "/data/web_static/shared/" ]; then sudo mkdir -p /data/web_static/shared/; fi
if ! [ -d "/data/web_static/releases/test/" ]; then sudo mkdir -p /data/web_static/releases/test/; fi
sudo touch /data/web_static/releases/test/index.html
echo " Fake HTML file :) " > /data/web_static/>
if [ -d "data/web_static/current" ]; then sudo rm -rf /data/web_static/current; fi
# Create a linked symbolic link, if it exists, it must be removed and recreated
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/ # Give ownership of the /data/ folder to the ubuntu user AND group
sudo sed -i '55 i \\t\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/>sudo service nginx restart
sudo service nginx restart
