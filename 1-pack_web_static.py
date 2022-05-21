#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
        contents of the web_static folder """
from os.path import exists
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function that generates tgz archive """
    if not exists("versions"):
        local("mkdir versions")
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        name_archive = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(name_archive))
        return name_archive
    except Exception as e:
        return None
