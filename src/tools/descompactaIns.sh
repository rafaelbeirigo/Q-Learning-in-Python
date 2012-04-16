#!/bin/bash
find ./ -name '*.in.gz' -exec gzip -d '{}' \; -print