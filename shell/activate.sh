#!/bin/bash

# Deactivate existing virtual environment if active
[[ -n "$VIRTUAL_ENV" ]] && deactivate

# Set project path and name
export PROJ_PATH=$(pwd)
export PROJ_NAME=$(basename "$PROJ_PATH")

# Source virtual environment if available
VENV="${PROJ_PATH}/venv/bin/activate"
[[ -f "$VENV" ]] && source "$VENV"

# Set Django settings module and Pylint config
export DJANGO_SETTINGS_MODULE="project.settings"
export PYLINTRC="${PROJ_PATH}/${PROJ_NAME}/.pylintrc"
