#!/usr/bin/python3
"""concepto simple de paginacion"""


def paginate(data, page_size, page_number):
    # indice de inicio para la pagina deseada
    start_index = (page_number - 1) * page_size
    # indice de finalizacion para la pagina deseada
    end_index = start_index + page_size
    # numero total de paginas en funcion de la longitud de los datos y el tamaño de la pagina
    total_pages = (len(data) + page_size - 1) // page_size
    # obtener los datos para la pagina deseada utilizando el indice de inicio y finalizacion
    page_data = data[start_index:end_index]

    # verifica si la pagina solicitada es valida (dentro del rango de paginas)
    if page_number > total_pages or page_number < 1:
        return [], total_pages
    else:
        return page_data, total_pages


# tamaño de pagina y numero de pagina deseado
page_number = 3
page_size = 10
# datos de ejemplo (una lista de números del 1 al 100)
data = list(range(1, 100))
# obtener los datos de la pagina deseada y el numero total de páginas
page_data, total_pages = paginate(data, page_size, page_number)

if page_data:
    print(f"Pagina {page_number} de {total_pages}:")
    for item in page_data:
        print(f"Articulo: {item}")
else:
    print(f"La pagina {page_number} no existe.")
