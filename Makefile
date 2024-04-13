
ifeq ($(shell which python),)
  PYTHON = python3
else
  PYTHON = python
endif

REPO_PTH = $(shell pwd)
VENV_NAME=env
VENV_BIN=$(REPO_PTH)/${VENV_NAME}
PYTHON_PTH = $(VENV_BIN)/$(DIR)/python

OS := $(shell uname)
ifeq ($(OS), Darwin)
	DIR := bin
	REQS := requirements.txt
	PYTHON_NM = python.exe
else
	DIR := Scripts
	REQS := requirements.txt
	PYTHON_NM = python
	REPO_PTH := $(subst /c/,C:/,$(REPO_PTH))
endif
	
create_venv:
	$(PYTHON) -m venv $(VENV_NAME) && . $(VENV_BIN)/$(DIR)/activate

pip: create_venv
	$(PYTHON_PTH) -m pip install --upgrade pip setuptools wheel

install: pip
	. $(VENV_NAME)/$(DIR)/activate && \
	$(PYTHON_PTH) -m pip install --no-cache-dir -r $(REQS)

clean:
	if test -d $(VENV_NAME); then rm -r $(VENV_NAME); fi
