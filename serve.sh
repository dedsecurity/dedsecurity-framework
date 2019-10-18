#!/bin/bash

echo "port: "; read p
nc -lvp "$p"
