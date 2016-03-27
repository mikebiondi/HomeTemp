#!/bin/bash

HOME=/home/pi
TEMP=$HOME/temp
date=$(date +%F)
FILE=/home/pi/temp/alertTemp


if [ -f $FILE ]; then
  $HOME/Dropbox-Uploader/dropbox_uploader.sh upload $FILE Alert/GCTemp.ALERT.${date}.csv  && rm $FILE
fi

