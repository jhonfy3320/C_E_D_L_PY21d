# Insertar al principio de la lista

Crea un nuevo nodo con el dato deseado.
Establece el enlace nextdel nuevo nodo para que apunte al nodo actual de la cabeza.
Actualiza la cabeza de la lista para que apunte al nuevo nodo.
Insertar al final de la lista:

Crea un nuevo nodo con el dato deseado.
Recorre la lista hasta llegar al último nodo.
Establece el enlace nextdel último nodo para que apunte al nuevo nodo.
Insertar en una posición específica:

Crea un nuevo nodo con el dato deseado.
Recorre la lista hasta llegar a la posición deseada.
Establece el enlace nextdel nuevo nodo para que apunte al siguiente nodo.
Actualiza el enlace nextdel nodo anterior para que apunte al nuevo nodo.
****
Eliminar un nodo:

Recorre la lista hasta encontrar el nodo a eliminar.
Actualiza el enlace nextdel nodo anterior para que apunte al siguiente nodo, omitiendo el nodo a eliminar.
Libera la memoria del nudo eliminado.
Buscar un elemento:

Recorre la lista comparando el
Si el elemento se encuentra, devuelve el nodo correspondiente.
Si se llega al final de la lista sin encontrar el elemento, devuelve un valor indicando que no se encontró.
Obtener la longitud de la lista:

Recorre la lista contando la cantidad de nodos encontrados.
Devuelve el número de nodos contados.
Es importante tener en cuenta que estas operaciones están basadas en una lista enlazada simple, donde solo se tiene acceso a la cabeza de la lista y cada nodo solo contiene una referencia al siguiente nodo. Si se requieren operaciones lógicas más complejas, como inserción o eliminación en posiciones específicas, puede ser necesario implementar adicional para buscar y manipular

**Recuerda que al trabajar con una lista enlazada simple, debes actualizar correctamente los enlaces nextpara mantener la coherencia de la lista.**
