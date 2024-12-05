def ordenar_texto_por_item(texto):
    if not isinstance(texto, str):
        raise TypeError
    
    def custom_key(item):
        return int(item) if item.isdigit() else item.casefold()
    
    lista = sorted(texto.split('-'), key=custom_key)
    lista_ordenada = "-".join(str(palabra) for palabra in lista)
    return lista_ordenada