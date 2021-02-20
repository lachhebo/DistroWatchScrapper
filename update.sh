# /bin/bash
cd /Users/ismail.lachheb/Projects/personal/DistroWatchScrapper
poetry run python gather.py
poetry run kaggle datasets version -p datasets -m "update data"