.PHONY: clean run

run:
	make "run.$(shell date '+%Y-%m-%d').jhu.data.js"

run.%.js:
	python3 -c 'import bs4, requests' || pip3 install -U pip -r requirements.txt
	python3 scrape.py &> "./$@"

clean:
	git clean -dix
