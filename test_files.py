#!/usr/bin/env python3
"""
Gera arquivos de teste em ./test_files/
Uso: python create_test_files.py
"""
import os

OUT = "test_files"
os.makedirs(OUT, exist_ok=True)

for i in range(1, 6):
    fname = os.path.join(OUT, f"document_{i}.txt")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(f"Arquivo de teste #{i}\nConteúdo de amostra para simulação.\n")
print(f"Arquivos criados em ./{OUT}/")
