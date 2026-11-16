# Criterios de Evaluación y Estándares de Corrección

Al generar o revisar código de algoritmos, se evalúan los siguientes componentes formales:

1. **Especificación Precisa:** 
   - Separación clara entre Entrada y Salida (Regla de la mano derecha).
   - Ausencia de detalles de implementación o fuentes de datos externas en la especificación.
2. **Demostración y Correctitud:**
   - Invariantes de ciclo documentados formalmente cuando aplique.
   - Demostración de terminación basada en relaciones bien fundadas.
   - En algoritmos de reintento, cumplimiento estricto del invariante de restauración (`Post_1`: deshacer los cambios en el estado auxiliar exactamente como se aplicaron).
3. **Análisis de Complejidad:**
   - Definición clara de la medida del tamaño de la entrada.
   - Identificación de la operación barómetro y planteamiento correcto de sumas o recurrencias (Teorema Maestro).