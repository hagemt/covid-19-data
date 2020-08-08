BROWSER := /Applications/Google Chrome.app
PYTHON3 := $(shell command -v python3)

JQ_PARAM := spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&resultOffset=0&resultRecordCount=250&cacheHint=true
JSON_URL := https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=1%3D1&$(JQ_PARAM)

default: help
.PHONY: default

help:
	# export PYTHON3=... # set python3 executable (default: from PATH)
	# try:
	# - make demo # for jhu.gif
	# - make json # esri/*.json
	# - make recalls # from FDA
.PHONY: help

demo: jhu.gif
	# run w/ BROWSER= path to application that opens GIFs
	open -a "$(BROWSER)" --args "file://$(shell pwd)/$<"
.PHONY: demo

json:
	# render per-country JSON data from JHU via PHP + Esri format:
	mkdir -p esri && curl -s "$(JSON_URL)" \
		| jq . > "esri/ncov-data-$(shell date +%s).json"
	cd esri; php -f index.php > ../docs/esri.html
	#cd esri; php -S localhost:9001
.PHONY: json

recalls: #sane
	[[ -x "$(PYTHON3)" ]] # run w/ PYTHON3= path to python v3.2+
	@"$(PYTHON3)" -c 'import pandas, matplotlib' \
		|| "$(PYTHON3)" -m pip install --user pandas matplotlib -U
	@"$(PYTHON3)" fda.py recalls
.PHONY: recalls

data: sane
	"$(PYTHON3)" jhu.py data
	#find data -name '*.png' -print0 | xargs -0 open

docs:
	npx @tilecloud/mdhtml README.md -t template.html -o docs/index.html
.PHONY: docs

sane:
	[[ -x "$(PYTHON3)" ]] # run w/ PYTHON3= path to python v3.2+
	"$(PYTHON3)" -c 'import imageio, requests' \
		|| "$(PYTHON3)" -m pip install --user imageio requests -U
.PHONY: sane

jhu.gif: data
	#find data -name '*.png' -print0 | xargs -0 open
	"$(PYTHON3)" jhu.py data "$@"
