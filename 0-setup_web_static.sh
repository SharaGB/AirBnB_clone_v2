#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

if [ -x "$(command -v nginx)" ];
then
        sudo apt update && apt install nginx -y
        sudo service nginx start
fi
# Create the folder /data/, /data/web_static/ and /data/web_static/releases/ with a single command
if ! [ -d "/data/web_static/releases/test/" ]; then sudo mkdir -p /data/web_static/releases/test; fi
if ! [ -d "/data/web_static/shared/" ]; then sudo mkdir -p /data/web_static/shared/; fi
echo 'Fake HTML file :)' > /data/web_static/releases/test/index.html
# Create a linked symbolic link, if it exists, it must be removed and recreated
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/ # Give ownership of the /data/ folder to the ubuntu user AND group
sudo sed -i '55i \\t\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
