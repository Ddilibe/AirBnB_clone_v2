#!/bin/usr/python3
""" Module to the function that compress a folder """
import os
from fabric.api import local
import os

def do_pack():
    """ Fabric script that generates a tgx archive from the contents
        of the web_static folder of the airbub clone repo

        Args:
            No Arguments

        Return:
            The archive path if it is correctly generated or none
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        t = datatime.now()
        f = "%Y%m%d%H%M%S"
        path = "versions/web_static_{}.tgx".format(t.strftime(f))
        local("tar -cvzf {} web_static".format(path))
        return archive_path
    except:
        return None
