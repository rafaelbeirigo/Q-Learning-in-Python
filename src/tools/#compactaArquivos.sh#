#!/bin/bash
find ./ -name '*.*' -exec gzip '{}' \; -print \
    -or -name "log.txt" -exec gzip '{}' \; -print \
    -or -name "shell.out" -exec gzip '{}' \; -print \
    -or -name "shell.output" -exec gzip '{}' \; -print