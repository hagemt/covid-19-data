BROWSER := /Applications/Google Chrome.app
PYTHON3 := $(shell command -v python3)

default: jhu.gif
	# run w/ BROWSER= path to application that opens GIFs
	@open -a "$(BROWSER)" --args "file://$(shell pwd)/$<"
.PHONY: default

data: sane
	"$(PYTHON3)" jhu.py data
	#find data -name '*.png' -print0 | xargs -0 open

sane:
	[[ -x "$(PYTHON3)" ]] # run w/ PYTHON3= path to python v3.2+
	"$(PYTHON3)" -c 'import imageio, requests' \
		|| "$(PYTHON3)" -m pip install --user imageio requests
.PHONY: sane

jhu.gif: data
	#find data -name '*.png' -print0 | xargs -0 open
	"$(PYTHON3)" jhu.py data "$@"
