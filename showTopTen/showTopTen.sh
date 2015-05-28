#!/bin/sh

python categorylinkToTile.py > zonmei.txt
python extraction.py < output.txt