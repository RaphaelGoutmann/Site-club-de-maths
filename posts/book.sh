#!/bin/bash

files=`ls | grep .md`

pandoc --pdf-engine=xelatex -f markdown -t pdf -s $files -o o.pdf
