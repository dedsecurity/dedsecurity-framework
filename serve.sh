#!/bin/bash

echo "Informe a porta que quer deixar na escuta: "; read p
nc -lvp "$p"
