#!/usr/bin/python3
""" Function that deploys """
from datetime import datetime
from fabric.api import *
import os
import shlex


env.hosts = ['3.238.118.13' '3.236.13.154']
env.user = "ubuntu"


def deploy():
    """ Fabric script that creates and distributes an archive to your web
        server

        Args:
            No Arguments

        Return:
            Return True if archve have been created else False
    """
    try:
        archive_path = do_pack()
    except:
        return False

    return do_deploy(archive_path)

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


def do_deploy(path):
    """ Fabric script that distribute an archive to a web server 
        
        Args:
            path: Path to the archive folder

        Return:
            True if all operations have been done correctly, otherwise
            return False
    """
    if not os.path.exists(path):
        return False
    try:
        a = path.replace('/', ' ')
        a = shlex.split(a)
        a = a[-1]

        am = a.replace('.', ' ')
        am = shlex.split(am)
        am = am[0]

        releases = "/data/web_static/releases/{}/".format(am)
        tmp = "/tmp/{}".format(a)

        put(path, "/tmp/")
        run("mkdir -p {}".format(releases))
        run("tar -xzf {} -C {}".format(tmp, releases))
        run("rm {}".format(tmp))
        run("mv {}web_static/* {}".format(releases, releases))
        run("rm -rf {}web_static".format(releases))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases))
        print("New version deployed!")
        return True
    except:
        return False
