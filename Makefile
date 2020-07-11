PYTHON3 := $(shell command -v python3)

jhu.gif: data
	@#find data -name '*.png' -print0 | xargs -0 open
	@open "$@"

data:
	"$(PYTHON3)" -c 'import imageio, requests' \
		|| "$(PYTHON)" -m pip install --user imageio requests
	"$(PYTHON3)" jhu.py gif data jhu.gif
