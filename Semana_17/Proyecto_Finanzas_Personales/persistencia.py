
from __future__ import annotations
import os
from pathlib import Path
from typing import List, Dict, Iterable, Optional, Tuple
from manejo_archivo_csv import escribir_archivo_csv, importar_archivo_csv

_DATA_DIR = Path(".").resolve()

def set_directorio_datos(path: os.PathLike | str) -> None:
    global _DATA_DIR
    _DATA_DIR = Path(path).resolve()
    _DATA_DIR.mkdir(parents=True, exist_ok=True)

def _ruta(nombre: str) -> Path:
    return _DATA_DIR / nombre

def guardar_categorias(categorias: Iterable[Dict[str, str]]) -> Path:

    categorias = list(categorias)
    ruta = _ruta("categorias.csv")
    headers = ["nombre"]
    escribir_archivo_csv(str(ruta), categorias, headers)
    return ruta

def cargar_categorias() -> List[Dict[str, str]]:
    ruta = _ruta("categorias.csv")
    return importar_archivo_csv(str(ruta)) if ruta.exists() else []

def guardar_movimientos(movimientos: Iterable[Dict[str, object]]) -> Path:
    movimientos = list(movimientos)
    ruta = _ruta("movimientos.csv")
    headers = ["tipo", "titulo", "monto", "categoria", "fecha"]
    
    norm = []
    for m in movimientos:
        fila = dict(m)
        fila["monto"] = float(fila["monto"])
        norm.append(fila)
    escribir_archivo_csv(str(ruta), norm, headers)
    return ruta

def cargar_movimientos() -> List[Dict[str, object]]:
    ruta = _ruta("movimientos.csv")
    return importar_archivo_csv(str(ruta)) if ruta.exists() else []
