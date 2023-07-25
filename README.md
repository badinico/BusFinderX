<p align="center">
  <img src="insertar_aqui_logo_del_proyecto.png" alt="Logo del Proyecto">
</p>

# 🚍 BusCazador - Rastreo de Buses en Tiempo Real 🕐

BusCazador es un script en Python que te permite rastrear los buses en tiempo real cercanos a un paradero específico 🚌🚏. Utiliza la API de transporte público para obtener información actualizada sobre los buses y su tiempo estimado de llegada al paradero. ¡Mantente informado sobre los horarios de llegada de los buses en tu parada favorita! 🚍🕒

## Características 🔍

- 📡 Consulta la API de transporte público para obtener información actualizada de los buses cercanos al paradero.
- 🚏 Visualiza los buses cercanos al paradero y su tiempo estimado de llegada.
- 💾 Genera un archivo CSV con los datos de los buses para su posterior análisis.
- 🔄 Actualización en tiempo real: refresca la información cada vez que ejecutas el script para obtener los datos más recientes.

## Instrucciones de Uso 📝

1. 📥 Clona o descarga este repositorio en tu máquina local.
2. 🖥️ Asegúrate de tener Python instalado en tu sistema.
3. 📦 Instala las dependencias necesarias ejecutando: `pip install pandas requests`.
4. 🟢 Ejecuta el script `buscazador.py`.
5. 🛤️ Ingresa el código del paradero que deseas rastrear cuando se solicite.
6. 🚌 Espera a que el script obtenga la información de la API y muestre los datos de los buses cercanos.
7. 💾 Los resultados se guardarán automáticamente en un archivo CSV llamado "buses.csv".

## Ejemplo de Resultados 📊

Recorrido | Estado | Patente | Distancia | Min. Mínimos | Min. Máximos | Promedio Min
--- | --- | --- | --- | --- | --- | ---
Ruta 123 | En Ruta | AB123CD | 150 metros | 3 minutos | 5 minutos | 4 minutos
Ruta 456 | Próximo | EF456GH | 300 metros | 2 minutos | 4 minutos | 3 minutos

## Contribución 🤝

¡Las contribuciones son bienvenidas! Si tienes alguna idea de mejora, encuentras un error o quieres agregar nuevas características, no dudes en abrir un pull request.

## Notas Importantes 📢

- Este script utiliza la API de transporte público, por lo que asegúrate de respetar los términos y condiciones de uso de la API.
- Los tiempos estimados de llegada pueden variar según el tráfico y otras condiciones. Se proporciona información en tiempo real, pero ten en cuenta posibles retrasos.
- Este proyecto es solo con fines educativos y de aprendizaje.

## Licencia 📜

[MIT License](LICENSE)

¡Esperamos que BusCazador sea útil y te ayude a mantenerte informado sobre los horarios de llegada de los buses en tu parada favorita! 🚍🕒

<p align="center">
  ¡Gracias por usar BusCazador! 🙌
</p>
