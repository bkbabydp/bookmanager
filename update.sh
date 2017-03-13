#!/usr/bin/env bash

declare basepath=$(cd `dirname "$0"`; pwd)
cd "$basepath"

git pull origin master
