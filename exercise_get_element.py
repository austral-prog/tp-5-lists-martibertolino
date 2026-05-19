def get_element(lista, indice):
    if indice >= 0 and indice < len(lista):
        return lista[indice]
    elif indice < 0 and indice > -len(lista):
        return lista[indice]
    else:
        return None
