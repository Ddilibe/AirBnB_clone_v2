#!/usr/bin/python3
""" Module to function that deploys the static files """
from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['3.238.118.13','3.236.13.154']
env.user = "ubuntu"


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
