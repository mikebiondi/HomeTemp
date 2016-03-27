#!/bin/bash

HOME=/home/pi
TEMP=$HOME/temp
date=$(date +%F)


if [ -f /home/pi/temp/temp.csv ]; then
  $HOME/Dropbox-Uploader/dropbox_uploader.sh upload $TEMP/temp.csv GCTemp.${date}.csv && rm $TEMP/temp.csv
else
	print "Erorr, file /home/pi/tmp/temp.csv not found"
fi

