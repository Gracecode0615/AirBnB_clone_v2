#!/usr/bin/python3
""" module deployment updates"""
from os.path import isfile
from fabric.api import *
from fabric.operations import run, local, put, sudo
from datetime import datetime
import time

env.user = 'ubuntu'
env.hosts = ['3.94.99.35', '3.239.94.218']


def do_pack():
    """compress a file for deployment
    Returns:
    type]: [description]
    """
    clocktime = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        localtar = local(
            'tar -czvf versions/web_static_{}.tgz web_static/'.format(
                clocktime), capture=True)
        return (localtar)
    except:
        return None


def do_deploy(archive_path):
    """deploy and transfers files
    """
    if isfile(archive_path):
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # divide the path and get the name of the file
        archive_file = archive_path.split("/")[-1]
        # Remove the extension to the archive
        folder_file = "/data/web_static/releases/" + archive_file.split(".")[0]
        # create the folder for the archive
        sudo("mkdir -p {:s}".format(folder_file))
        # Uncompress the archive to the folder
        sudo("tar -xzf /tmp/{:s} -C {:s}".format(archive_file, folder_file))
        # delete the archive from the web server in tmp
        sudo("rm /tmp/{:s}".format(archive_file))
        # move all files
        sudo("mv {:s}/web_static/* {:s}/".format(folder_file, folder_file))
        # delete
        sudo("rm -rf {:s}/web_static/".format(folder_file))
        # delete simbolic link
        sudo("rm -rf /data/web_static/current")
        # create simbolic link
        sudo("ln -s {:s} /data/web_static/current".format(folder_file))
        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """deploy final deployment
    Returns:
    [type]: [description]
    """
    path_of_archive = do_pack()
    if path_of_archive is None:
        return False
    else:
        final_deploy = path_of_archive.__dict__["command"].split(" ")[2]
        return do_deploy(final_deploy)
