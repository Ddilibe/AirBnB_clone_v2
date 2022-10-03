#!/usr/bin/env bash
# Bash script that sets up a we server for the deployment of web static

# Update the server
sudo apt-get update

# Install web server Nginx
sudo apt-get install nginx

# Create folder data
sudo mkdir -p /data/

# Create folder web static if it doesn't exists
sudo mkdir -p /data/web_static

# Creating folder release if it doesn't exists
sudo mkdir -p data/web_static/releases

# Creating folder shared if it doesn't already exists
sudo mkdir -p data/web_static/shared/

# Creating folder test if it doesn't already exists
sudo mkdir -p data/web_static/releases/test/

# Creating a fake html file if it doesn't exist
jame="<html>\n\t<head></head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo $jame >> data/web_static/releases/test/index.html

# Creating a symbolic link to a folder
ln -s data/web_static/releases/test data/web_static/current

# Grant permission to a user and a group
chown -hR ubuntu: data/

# Command to change a configure the content to be served
sed -i "s/}/}\n\tlocation \/hbnb_static\/ {\n\t\t alias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}\n/" /etc/nginx/sites-enabled/default

# Restarting nginx
sudo service nginx restart
