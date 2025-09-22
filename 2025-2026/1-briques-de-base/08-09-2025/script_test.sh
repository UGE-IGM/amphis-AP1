#!/bin/bash

pandoc "$1" -o "$2" --from markdown --template eisvogel --listings  --pdf-engine=xelatex
