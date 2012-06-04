#!/usr/bin/env python

from subprocess import call

def prepareFolders(commandPath, filePath):
    if commandPath != '' and filePath != '':
        command   = commandPath + "/prepareFolders.sh"
        arguments = filePath

        print command + " " + arguments

        call([command, arguments])
