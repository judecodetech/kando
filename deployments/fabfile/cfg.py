"""
Define generic constants for reusabililty
"""

from os.path import join, sep

from fabric.api import env

env.BASE_DIR = join(sep, 'usr', 'local', 'src', 'kando')
env.GIT_REPO_URL = 'git@gitlab.lambda.codes:lambda/kando.git'

env.GIT_REPO_DIR = join(env.BASE_DIR, 'deploy')
env.PROJECT_DIR = join(env.GIT_REPO_DIR, 'web')

env.DEPLOY_DIR = join(env.GIT_REPO_DIR, 'deployments')
env.ETC_DIR = join(env.DEPLOY_DIR, 'ubuntu', 'etc')

env.VENV_DIR = '/var/venv/'
