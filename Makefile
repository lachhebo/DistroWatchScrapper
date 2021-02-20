.PHONY: update the datasets on kaggle  
update:
	poetry run /Users/ismail.lachheb/Projects/personal/DistroWatchScrapper/gather.py
	poetry run kaggle datasets version -p datasets -m "update data"
	

