from easytello import tello
import time

class DroneController:
    """
    Clase para controlar el dron utilizando comandos.
    """

    def __init__(self):
        self.drone = tello.Tello()

    def move(self, command):
        """
        Mueve el dron según el comando recibido.
        Args:
            command (str): El comando recibido.
        """
        command_map = {
            "a": self.drone.left,
            "d": self.drone.right,
            "w": self.drone.forward,
            "s": self.drone.back,
            "p": self.drone.down,
            "u": self.drone.up,
            "stop": self.drone.stop,
            "cw": lambda: self.drone.cw(90),
            "ccw": lambda: self.drone.ccw(90),
            "flip_f": self.drone.flip_forward,
            "flip_b": self.drone.flip_back,
            "flip_l": self.drone.flip_left,
            "flip_r": self.drone.flip_right
        }

        if command in command_map:
            command_map 
        else:
            print("Comando no reconocido")

    def start(self):
        """
        Inicia el control del dron.
        """
        self.drone.takeoff()
        print("Bienvenido al control del dron. Usa 'w', 'a', 's', 'd' para moverte.")
        print("Usa 'u' para subir, 'p' para bajar. Usa 'cw' para rotar en el sentido horario y 'ccw' para rotar en el sentido antihorario.")
        print("Usa 'flip_f', 'flip_b', 'flip_l', 'flip_r' para hacer flips.")
        print("Para detener el movimiento, presiona 'stop'.")
        print("Para aterrizar, presiona 'q'.")

        while True:
            command = input("Ingresa un comando: ").lower()
            if command == 'q':
                break
            self.move(command)
            time.sleep(0.1)  # Pausa de 0.1 segundos después de cada comando de movimiento

        self.drone.land()

if __name__ == "__main__":
    drone_controller = DroneController()
    drone_controller.start()
