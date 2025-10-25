#!/bin/bash
# Script para executar o programa PostgreSQL
# Executa o programa diretamente (sem venv)

cd "$(dirname "$0")"
python3 postgresql_bd.py
