# COVID-19 State Graph Scraper

Pulls current data summary (images) for all fifty states from Johns Hopkins.

Example output from 2020-10-10 run:

![Example Output](ymd/2020-10-10.gif)

If you want to image parse or slow it down, try: https://ezgif.com/speed

## Development

Uses `Makefile` to drive `PYTHON3 ?= $(shell command -v python3)`.

See `make` output, or read `.py` file(s) for more data.

Targets include:

* `make demo # for jhu.gif`
* `make json # esri/*.json`
* `make recalls # from FDA`

The `docs` folder is hosted on: https://hagemt.github.io/covid-19-data
