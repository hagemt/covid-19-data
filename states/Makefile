.PHONY: clean sane stats raw run

stats: raw
	python3 -u stats.py .

raw: sane
	python3 -u stats.py &> "raw.jhu.data.$(shell date '+%Y-%m-%d').csv"

run:
	make "run.$(shell date '+%Y-%m-%d').jhu.data.js"

run.%.js: sane
	python3 scrape.py &> "./$@"

sane:
	python3 -c 'import bs4, matplotlib, pandas, requests' \
		|| pip3 install -U pip -r requirements.txt

clean:
	git clean -dix
