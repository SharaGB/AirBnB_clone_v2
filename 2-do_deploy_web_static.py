#!/usr/bin/python3
""" Distributes an archive to your web servers """
from os.path import exists
from fabric.api import env, put, run

env.hosts = ['34.148.132.49', '3.95.23.58']


def do_deploy(archive_path):
    """ Distributes"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1].split('.')[0]
        path = '/data/web_static/releases/{}'.format(filename)
        put(archive_path, '/tmp/')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, path))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}/web_static/* {0}/'.format(path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(path))
        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False
