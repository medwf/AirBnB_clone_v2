#!/usr/bin/python3
"""
import modules
this file is fabfile
"""
from fabric.api import local, task, env, put, run
from datetime import datetime
import os

env.hosts = ['100.25.110.123', '54.208.156.46']

@task
def do_pack():
    """
    this function execute script that generates a .tgz
        archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f'versions/web_static_{date}.tgz'
    print(f'Packing web_static to {file_path}')
    try:
        local(f"tar -czvf {file_path} web_static")
        size = os.path.getsize(file_path)
        print(f'web_static packed: {file_path} -> {size}Bytes')
        return file_path
    except Exception:
        return None
@task
def do_deploy(archive_path):
    """this function distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        File = os.path.basename(archive_path)
        Dir, ext = os.path.splitext(File)
        pt = "/data/web_static/releases/{}".format(Dir)
        run("mkdir -p {}".format(pt))
        run("tar -xzf /tmp/{} -C {}/".format(File, pt))
        run("rm /tmp/{}".format(File))
        run("mv {}/web_static/* {}/".format(pt))
        run("rm -rf {}/web_static".format(pt))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(pt))
        print("New version deployed!")
        return True
    except Exception:
        return False
