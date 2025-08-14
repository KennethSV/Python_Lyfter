
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Iterable, Optional
from datetime import datetime
import re

import persistencia

def _normalizar_nombre(nombre: str) -> str:
    return re.sub(r"\s+", " ", nombre.strip()).lower()

@dataclass(frozen=True)
class Categoria:
    nombre: str

    def __post_init__(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío.")

@dataclass
class Movimiento:
    tipo: str
    titulo: str
    monto: float
    categoria: str
    fecha: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))

    def __post_init__(self):
        t = self.tipo.lower()
        if t not in {"gasto", "ingreso"}:
            raise ValueError("El tipo de movimiento debe ser 'gasto' o 'ingreso'.")
        if not isinstance(self.titulo, str) or not self.titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        try:
            monto_val = float(self.monto)
        except Exception as e:
            raise ValueError("El monto debe ser un número.") from e
        if monto_val <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        # Normalizar
        self.tipo = t
        self.titulo = self.titulo.strip()
        self.monto = monto_val
        self.categoria = self.categoria.strip()

class GestorFinanzas:
    def __init__(self, directorio_datos: Optional[str] = None) -> None:
        if directorio_datos:
            persistencia.set_directorio_datos(directorio_datos)
        self._categorias: List[Categoria] = []
        self._movimientos: List[Movimiento] = []
        self.cargar()

    def guardar(self) -> None:
        persistencia.guardar_categorias([{"nombre": c.nombre} for c in self._categorias])
        persistencia.guardar_movimientos([m.__dict__ for m in self._movimientos])

    def cargar(self) -> None:
        self._categorias = [Categoria(c["nombre"]) for c in persistencia.cargar_categorias()]
        self._movimientos = [Movimiento(**m) for m in persistencia.cargar_movimientos()]

    def listar_categorias(self) -> List[str]:
        return [c.nombre for c in self._categorias]

    def existe_categoria(self, nombre: str) -> bool:
        key = _normalizar_nombre(nombre)
        return any(_normalizar_nombre(c.nombre) == key for c in self._categorias)

    def agregar_categoria(self, nombre: str) -> Categoria:
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("Ingrese un nombre de categoría.")
        if self.existe_categoria(nombre):
            raise ValueError("La categoría ya existe.")
        cat = Categoria(nombre)
        self._categorias.append(cat)
        self.guardar()
        return cat

    def agregar_movimiento(self, tipo: str, titulo: str, monto: float, categoria: str) -> Movimiento:
        if not self._categorias:
            raise RuntimeError("No hay categorías. Agregue una categoría antes de registrar movimientos.")
        if not self.existe_categoria(categoria):
            raise ValueError("La categoría seleccionada no existe.")
        mov = Movimiento(tipo=tipo, titulo=titulo, monto=monto, categoria=categoria)
        self._movimientos.append(mov)
        self.guardar()
        return mov

    def agregar_gasto(self, titulo: str, monto: float, categoria: str) -> Movimiento:
        return self.agregar_movimiento("gasto", titulo, monto, categoria)

    def agregar_ingreso(self, titulo: str, monto: float, categoria: str) -> Movimiento:
        return self.agregar_movimiento("ingreso", titulo, monto, categoria)

    def listar_movimientos(self) -> List[Dict[str, object]]:
        return [
            {
                "fecha": m.fecha,
                "tipo": m.tipo,
                "titulo": m.titulo,
                "monto": m.monto,
                "categoria": m.categoria,
            }
            for m in self._movimientos
        ]

    def balance(self) -> float:
        total = 0.0
        for m in self._movimientos:
            total += m.monto if m.tipo == "ingreso" else -m.monto
        return round(total, 2)
