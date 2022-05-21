# Configuring Nginx with puppet

exec { 'executing in nginx':
  command  => 'if ! dpkg -s nginx > /dev/null;
               then apt-get -y update;
               apt-get -y upgrade;
               apt-get -y install nginx;
               fi;
               sudo mkdir -p /data/web_static/releases/test/;
               sudo mkdir -p /data/web_static/shared/;
               echo Holberton School | sudo tee /data/web_static/releases/test/index.html;
               sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
               sudo chown -R ubuntu:ubuntu /data/;
               sudo sed -i /:80 default_server;/ a \\\n\tlocation\
            /hbnb_static {\n\talias /data/web_static/current/;\n\t}/\
            /etc/nginx/sites-available/default;
               sudo service nginx restart',
  provider => shell,
}
