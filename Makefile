PYTHON3 := $(shell command -v python3)

jhu: data
	find data -name '*.png' -print0 | xargs -0 open
.PHONY: jhu

data:
	"$(PYTHON3)" -c 'import requests' \
		|| "$(PYTHON)" -m pip install --user requests
	"$(PYTHON3)" jhu.py
