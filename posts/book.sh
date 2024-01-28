#!/bin/bash

files=`ls | grep .md`

pandoc -f markdown -t pdf -s $files -o o.pdf