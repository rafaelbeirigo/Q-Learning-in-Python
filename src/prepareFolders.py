#!/usr/bin/env python2

from subprocess import call

def prepareFolders(commandPath, filePath):
    if commandPath != '' and filePath != '':
        command   = commandPath + "/prepareFolders.sh"
        arguments = filePath

        print command + " " + arguments

        call([command, arguments])
