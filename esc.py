try:
    import msvcrt  # Для Windows
except ImportError:
    import sys, tty, termios  # Для Unix-подобных систем

def get_char():
    """ Функция для чтения одного символа с клавиатуры, без ожидания нажатия Enter. """
    try:
        return msvcrt.getch().decode('utf-8')
    except NameError:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.decode('utf-8')

def main():
    sum_of_codes = 0
    
    print("Введите символы, нажмите ESC для завершения:")
    
    while True:
        char = get_char()
        if ord(char) == 27:  # Код клавиши ESC
            break
        sum_of_codes += ord(char)
        print(char,":", ord(char))
    
    
    print(f"Сумма кодов символов: {sum_of_codes}")
    
if __name__ == "__main__":
    main()
