# EEG Drones Documentation

Este repositorio tiene como objetivo documentar el funcionamiento de drones controlados mediante señales EEG utilizando la diadema Muse 2 y la biblioteca BrainFlow.

## Introducción

Los drones controlados por señales EEG representan una interesante intersección entre neurociencia y robótica. A través del uso de dispositivos de electroencefalografía (EEG) como la Muse 2, es posible captar y procesar señales cerebrales para controlar drones de manera innovadora.

## Muse 2: La Diadema de Percepción Cerebral

La Muse 2 es una diadema EEG que proporciona una forma sencilla y accesible de monitorear la actividad cerebral. Equipada con sensores para EEG, acelerómetro, giroscopio y pulsómetro, la Muse 2 permite a los usuarios obtener datos en tiempo real sobre su actividad cerebral y otros parámetros fisiológicos. Es ampliamente utilizada tanto en investigación como en aplicaciones comerciales.

## Requisitos del Sistema

Este proyecto está desarrollado en una Raspberry Pi con sistema operativo Ubuntu. Utilizamos el manejador de paquetes `apt` para instalar las dependencias necesarias, aunque los usuarios son libres de utilizar el manejador de paquetes que prefieran.

## Instalación

1. **Actualizar el sistema y los paquetes:**
    ```bash
    sudo apt update && sudo apt upgrade
    ```

2. **Instalar Python y pip:**
    ```bash
    sudo apt install python3 python3-pip
    ```

3. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/EEG-Drones.git
    cd EEG-Drones
    ```

4. **Instalar las dependencias del proyecto:**
    ```bash
    pip3 install -r requirements.txt
    ```

## BrainFlow

BrainFlow es una biblioteca diseñada para simplificar el acceso a datos de dispositivos EEG y otros sensores biométricos. Proporciona una API unificada que facilita la adquisición, procesamiento y análisis de datos.

### Instalación de BrainFlow

1. **Instalar las dependencias de BrainFlow:**
    ```bash
    sudo apt install libboost-all-dev libeigen3-dev
    ```

2. **Instalar BrainFlow mediante pip:**
    ```bash
    pip3 install brainflow
    ```

### Uso Básico de BrainFlow

Aquí tienes un ejemplo de cómo iniciar la adquisición de datos desde la Muse 2 utilizando BrainFlow:

```python
import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams

params = BrainFlowInputParams()
params.serial_port = '/dev/ttyUSB0'  # Ajustar según tu configuración
board = BoardShim(BoardShim.MUSE_2_BOARD, params)
board.prepare_session()
board.start_stream()

data = board.get_board_data()
print(data)

board.stop_stream()
board.release_session()

```
Para más información, consulta la [documentación completa de BrainFlow](https://brainflow.readthedocs.io/en/stable/) y su [repositorio en GitHub](https://github.com/brainflow-dev/brainflow).

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Enlaces Útiles

- [Muse 2: Sitio Oficial](https://choosemuse.com/muse-2/)
- [BrainFlow: Repositorio en GitHub](https://github.com/brainflow-dev/brainflow)
