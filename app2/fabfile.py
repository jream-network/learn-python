from fabric.api import *

def listme():
    local('ls -lta')

def commit():
    branch = 'master'
    local('git add -u')
    local('git add .')
    msg = prompt('Commit Message: ')
    local('git commit -m {0}'.format(msg))
    local('git push origin {0}'.format(branch))
