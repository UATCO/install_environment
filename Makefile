ifeq ($(OS),Windows_NT)
    python = python
else
    python = python3
endif
command = $(python)
obj  = installer.py

clone:
	$(command) $(obj) -clone
create_venv:
	$(command) $(obj) -create_venv
install_requirements:
	$(command) $(obj) -reqs
pull:
	$(command) $(obj) -pull
