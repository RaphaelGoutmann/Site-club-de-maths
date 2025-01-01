#!/bin/bash

OUTPUT="book.pdf"

cp -r ../img .
files=`ls | grep .md`

pandoc --pdf-engine=xelatex -f markdown -t pdf -s $files -o ${OUTPUT}
rm -rf img/
