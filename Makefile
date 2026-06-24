
REMOTE_USER = mag
REMOTE_HOST = mailserver
REMOTE_PATH = /var/www/reform

PANDOC = pandoc
PANDOC_FLAGS = -s --mathjax

MD_FILES = $(wildcard *.md)

HTML_FILES = $(MD_FILES:.md=.html)


update:
	git fetch origin
	git merge origin/develop
	./update-data.py

deploy: update compile
	cp -r Downloads _site/
	git add --all && git commit ; git push


test: compile
	rsync -avz \
			--exclude='Makefile' \
			--exclude='.*' \
			./_site/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH)/;

megyatest: compile
	rsync -avz \
			--exclude='Makefile' \
			--exclude='.*' \
			./_site/ /var/www/megya

compile:
	npm run build

.PHONY: all clean
