from easytello import tello
import time

# Crear instancia del dron
drone = tello.Tello()

def move_drone(command):
    """
    Función para mover el dron según el comando recibido.
    Args:
        command (str): El comando recibido.
    """
    if command == "a":
        drone.left(50)
    elif command == "d":
        drone.right(50)
    elif command == "w":
        drone.forward(50)
    elif command == "s":
        drone.back(50)
    elif command == "p":
        drone.down(50)
    elif command == "u":
        drone.up(50)
    elif command == "stop":
        drone.stop()

def main():
    """
    Función principal.
    """
    drone.takeoff()
    print("Bienvenido al control del dron. Usa 'w', 'a', 's', 'd' para moverte.")
    print("Para detener el movimiento, presiona 'stop'.")
    print("Para aterrizar, presiona 'q'.")

    while True:
        command = input("Ingresa un comando: ").lower()
        if command == 'q':
            break
        move_drone(command)
        time.sleep(0)  # Pausa de 0 segundos después de cada comando de movimiento

    drone.land()

if __name__ == "__main__":
    main()