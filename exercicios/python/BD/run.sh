#!/bin/bash
# Script para executar o programa PostgreSQL
# Ativa o ambiente virtual e executa o programa

cd "$(dirname "$0")"
source venv/bin/activate
python3 postgresql_bd.py
