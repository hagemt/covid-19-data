BROWSER := /Applications/Google Chrome.app
PYTHON3 := $(shell command -v python3)

default: help
.PHONY: default

help:
	# export PYTHON3=... # set python3 executable (default: from PATH)
	# try:
	# - make demo # for jhu.gif
	# - make recalls # from FDA
.PHONY: help

demo: jhu.gif
	# run w/ BROWSER= path to application that opens GIFs
	open -a "$(BROWSER)" --args "file://$(shell pwd)/$<"
.PHONY: demo

recalls: #sane
	[[ -x "$(PYTHON3)" ]] # run w/ PYTHON3= path to python v3.2+
	@"$(PYTHON3)" -c 'import pandas, matplotlib' \
		|| "$(PYTHON3)" -m pip install --user pandas matplotlib -U
	@"$(PYTHON3)" fda.py recalls
.PHONY: recalls

data: sane
	"$(PYTHON3)" jhu.py data
	#find data -name '*.png' -print0 | xargs -0 open

sane:
	[[ -x "$(PYTHON3)" ]] # run w/ PYTHON3= path to python v3.2+
	"$(PYTHON3)" -c 'import imageio, requests' \
		|| "$(PYTHON3)" -m pip install --user imageio requests -U
.PHONY: sane

jhu.gif: data
	#find data -name '*.png' -print0 | xargs -0 open
	"$(PYTHON3)" jhu.py data "$@"
