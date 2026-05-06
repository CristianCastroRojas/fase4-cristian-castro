# Requisitos del Usuario

**Árbol Binario de Búsqueda - Aplicación Gráfica**  
Curso: 301305 - Estructura de Datos  
Fase 4 - Arquitectura de estructuras binarias  

---

## 1. Requisitos Funcionales

**RF1.** El sistema debe mostrar una interfaz gráfica inicial de acceso con el título "Acceso - Árbol Binario de Búsqueda".

**RF2.** El sistema debe mostrar en la interfaz inicial:
- Nombre de la aplicación  
- Nombre del estudiante  
- Fecha de realización  

**RF3.** El sistema debe solicitar una contraseña enmascarada con caracteres (* o -).

**RF4.** La contraseña de acceso será: "ARBOL".

**RF5.** El sistema debe contar con un botón "Ingresar" que permita acceder a la interfaz principal si la contraseña es correcta.

**RF6.** El sistema debe mostrar un mensaje de error si la contraseña es incorrecta.

**RF7.** El sistema debe redirigir a la interfaz principal del árbol binario al ingresar correctamente.

**RF8.** La interfaz principal debe contener un campo de entrada para ingresar valores enteros.

**RF9.** El sistema debe contar con un botón "Agregar Nodo" que permita insertar un valor en el árbol binario de búsqueda.

**RF10.** El sistema debe contar con un botón "Buscar Nodo" que permita verificar si un valor existe en el árbol.

**RF11.** El sistema debe contar con un botón "Limpiar" que elimine todos los nodos del árbol y sus recorridos.

**RF12.** El sistema debe contar con un botón "Salir" que cierre la aplicación.

**RF13.** El sistema debe mostrar gráficamente el árbol binario de búsqueda en un panel denominado "Árbol".

**RF14.** El sistema debe mostrar los recorridos del árbol en tres paneles adicionales:
- Preorden  
- Inorden  
- Posorden  

**RF15.** El sistema debe actualizar automáticamente el árbol y los recorridos cada vez que se agregue un nodo.

**RF16.** El sistema debe permitir ingresar únicamente valores enteros.

**RF17.** El sistema debe mostrar un mensaje de error si el usuario ingresa un valor no numérico.

**RF18.** El sistema debe mostrar un mensaje de error si se intenta buscar un nodo que no existe en el árbol.

**RF19.** El sistema debe limitar la profundidad del árbol a un máximo de 4 niveles.

**RF20.** El sistema debe mostrar un mensaje de error si se intenta insertar un nodo que supere el nivel máximo permitido.

---

## 2. Requisitos No Funcionales

**RNF1.** La aplicación debe desarrollarse en lenguaje Python.

**RNF2.** La aplicación debe utilizar programación orientada a objetos (POO).

**RNF3.** La aplicación debe implementar la estructura de datos Árbol Binario de Búsqueda (ABB).

**RNF4.** La aplicación debe utilizar una interfaz gráfica de usuario (GUI), preferiblemente con Tkinter u otra librería equivalente.

**RNF5.** La aplicación debe ejecutarse de forma local sin necesidad de conexión a internet.

**RNF6.** La aplicación no debe utilizar bases de datos; los datos se almacenan en memoria.

**RNF7.** La interfaz debe ser clara, organizada e intuitiva para el usuario.

**RNF8.** El sistema debe manejar correctamente las excepciones y mostrar mensajes adecuados al usuario.

**RNF9.** La representación gráfica del árbol debe ser legible y organizada hasta 4 niveles.

**RNF10.** El código debe estar estructurado en clases, incluyendo una clase principal para gestionar el árbol.

---

## 3. Reglas de Negocio

**RN1.** El acceso al sistema solo es permitido si la contraseña ingresada es exactamente "ARBOL".

**RN2.** El árbol binario de búsqueda debe cumplir la propiedad:
- Los valores menores se ubican a la izquierda.  
- Los valores mayores se ubican a la derecha.  

**RN3.** No se deben permitir valores duplicados en el árbol.

**RN4.** Los nodos deben insertarse siguiendo las reglas del Árbol Binario de Búsqueda (ABB).

**RN5.** Los recorridos del árbol deben generarse automáticamente:
- Preorden: Raíz → Izquierda → Derecha  
- Inorden: Izquierda → Raíz → Derecha  
- Posorden: Izquierda → Derecha → Raíz  

**RN6.** La búsqueda de nodos debe recorrer el árbol siguiendo la lógica del ABB.

**RN7.** El árbol debe reiniciarse completamente al presionar el botón "Limpiar".

**RN8.** El sistema debe impedir la inserción de nodos si se alcanza una profundidad mayor a 4 niveles.

**RN9.** Los valores ingresados deben ser validados antes de ser procesados.

---