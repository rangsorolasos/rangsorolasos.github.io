
REMOTE_USER = mag
REMOTE_HOST = server
REMOTE_PATH = /var/www/reform/aranyos-rangsorolasos

PANDOC = pandoc
PANDOC_FLAGS = -s --mathjax

MD_FILES = $(wildcard *.md)

HTML_FILES = $(MD_FILES:.md=.html)

all: $(HTML_FILES)


deploy: all
	rsync -avz --delete \
			--exclude='Makefile' \
			--exclude='.*' \
			./ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH)/;

%.html: %.md
	$(PANDOC) $(PANDOC_FLAGS) -o $@ $<

clean:
	rm -f $(HTML_FILES)

.PHONY: all clean
