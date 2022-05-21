# Configuring Nginx with puppet

exec { 'Update Nginx':
  command  => 'if ! [ "$(command -v nginx)" ];
               then apt-get -y update;
               apt-get install nginx -y;
               fi;
               sudo mkdir -p /data/web_static/releases/test/;
               sudo mkdir -p /data/web_static/shared/;
               echo "Fake HTML File :)" | sudo tee /data/web_static/releases/test/index.html;
               sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
               sudo chown -R ubuntu:ubuntu /data/;
               sudo sed -i "55i \\t\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"\
            /etc/nginx/sites-available/default;
               sudo service nginx restart',
  provider => shell,
}
