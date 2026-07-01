#!/bin/bash

# Captura el archivo o tag que le pases, si no, corre toda la suite
TARGET=${1:-""}

echo "🗑️  Limpiando reportes anteriores..."
rm -rf reports/allure-results/*

echo "🚀 Ejecutando Behave..."
behave -f allure -o reports/allure-results $TARGET

echo "📊 Abriendo Allure..."
allure serve reports/allure-results