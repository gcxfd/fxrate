#!/usr/bin/env bash

set -e

_DIR=$(dirname $(realpath "$0"))

cd $_DIR

. /root/.py3/bin/activate

timeout 1h ./main.py

cp CNY.csv /mnt/sf/Shared\ with\ groups/const/

timeout 1h sync

