#!/bin/bash
echo "Informe a url: "; read u
	wget $u
	grep href index.html | cut -d "/" -f3 | grep "\." | sort -u
