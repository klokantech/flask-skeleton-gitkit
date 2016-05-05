SCRIPTS = hello

TARGET ?= .

all: build

serve:
	java -jar $(PLOVR) serve ./*/debug.json

build: $(addprefix $(TARGET)/,$(addsuffix .js,$(SCRIPTS)))

$(TARGET)/%.js: %/release.json
	java -jar $(PLOVR) build $< > $@
