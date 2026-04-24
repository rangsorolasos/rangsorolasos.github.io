
REMOTE_USER = mag
REMOTE_HOST = server
REMOTE_PATH = /var/www/reform

PANDOC = pandoc
PANDOC_FLAGS = -s --mathjax

MD_FILES = $(wildcard *.md)

HTML_FILES = $(MD_FILES:.md=.html)

deploy: compile
	git add --all && git commit && git push


test: compile
	rsync -avz \
			--exclude='Makefile' \
			--exclude='.*' \
			./docs/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH)/;

compile:
	npm run build

.PHONY: all clean
