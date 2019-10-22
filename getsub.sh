#!/bin/bash
echo "Enter URL: "; read u
	wget $u
	grep href index.html | cut -d "/" -f3 | grep "\." | sort -u
