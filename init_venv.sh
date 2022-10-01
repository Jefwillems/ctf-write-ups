#!/bin/zsh

if [ ! -f venv/bin/activate ]; then
    echo "Venv not found! creating..." >&2
    python -m venv venv
fi
