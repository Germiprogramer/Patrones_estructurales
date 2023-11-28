# Patrones_estructurales

Germán Llorente

El link al repositorio es el siguiente: https://github.com/Germiprogramer/Patrones_estructurales.git

### Pizzeria

En el ejercicio de la entrega pasada, se decidió emplear el patrón builder para la elaboración de las pizzas, debido a que este patrón habilita declarar subpartes de un elemento e ir indicándolas. Esto era perfecto para una pizza con distintos ingredientes. 

En este caso, debíamos expandir el patrón con la implementación de menús. Para ello se ha requerido del patrón composite, justificado por la necesidad de representar tanto elementos individuales (como entradas, bebidas, pizzas y postres), como menús compuestos que pueden contener otros elementos y/o menús. Las razones de uso de este patrón de diseño son varias:

**Estructura Jerárquica:**

Los menús pueden tener una estructura jerárquica, donde un menú compuesto puede contener otros menús o elementos individuales. En el ejercicio, se han metido menús dobles, que son menús compuestos de otros menús. El patrón Composite permite representar esta estructura de manera eficiente.

**Operaciones Recursivas:**

Al utilizar Composite, se pueden realizar operaciones recursivas en toda la estructura de menús y elementos. Por ejemplo, calcular el precio total de un menú compuesto que contiene otros menús y elementos.

**Facilita la Creación y Modificación:**

La implementación del patrón Composite facilita la creación y modificación de menús. Se pueden agregar, quitar o modificar elementos de manera transparente, ya que todos los elementos comparten la misma interfaz.

**Cálculo Eficiente del Precio:**

El cálculo del precio de un menú compuesto se puede realizar de manera eficiente al aprovechar las operaciones recursivas.  Cada elemento individual contribuye a la suma total del precio, y los menús compuestos propagan la llamada para calcular el precio de sus componentes.

**Persistencia y Reconstrucción:**

Al utilizar Composite, se facilita la persistencia en archivos CSV y la reconstrucción de la estructura de menús a partir de la información almacenada. La recursividad inherente al patrón simplifica la reconstrucción de menús compuestos a partir de sus componentes almacenados.

Además, cabe destacar también que el patron builder y el patrón composite pueden acoplarse el uno al otro y ser usados como una estructura única. Esto permite realizar perfectamente la simulación de la pizzeria.

_____________________________________________________________________________________________________________________________________________________________________

Además de la justificación del uso del patrón, me gustaría resaltar el uso de las interfaces gráficas que se han elegido, dado que lo que creo que le da un toque extra a mi resolución del ejercicio es la conexión de interfaces en función de las conexiones del usuario. Para próximos ejercicios se intentará realizar en frameworks como Django o Flask, pero en este he preferido optar por readaptar la versión anterior-

### SAMUR





