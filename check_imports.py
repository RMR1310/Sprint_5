# -*- coding: utf-8 -*-
import importlib, sys
modules = ["streamlit","pandas","plotly.express"]
for m in modules:
    try:
        importlib.import_module(m)
        print(f"{m} OK")
    except Exception as e:
        print(f"{m} ERRO: {e}")
        sys.exit(1)
print("todos os imports carregam")
