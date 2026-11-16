# Directrices de Estilo: Código Legible y Extendido

Para este repositorio se prohíbe estrictamente el uso de "code golf", código críptico y *one-liners* excesivos. El código debe priorizar la legibilidad humana por encima de la brevedad sintáctica.

## Reglas obligatorias:
1. **Evitar One-Liners complejos:** No encadenar múltiples comprensiones de listas, funciones de orden superior (`map`, `filter`, `lambda`) o condicionales ternarios anidados en una sola línea si esto oscurece la lógica.
2. **Estructuras de control explícitas:** Preferir bloques `if-else` tradicionales y ciclos `while` o `for` desglosados donde se pueda ver claramente cada paso de la iteración y el manejo de índices.
3. **Nombres descriptivos:** Las variables y funciones deben tener nombres claros en inglés (según las convenciones del curso) que indiquen su propósito y no una abreviatura críptica.
4. **Comentarios de precondición y lógica:** Cada bloque lógico importante debe ir acompañado de comentarios explicativos que detallen el razonamiento (especialmente en reintentos, programación dinámica y reducciones).