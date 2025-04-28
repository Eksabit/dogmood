import subprocess
import win32evtlog
import win32evtlogutil
import win32security
import win32api
import win32con
import ctypes
import sys
import os
from colorama import Fore, Style, init
from prettytable import PrettyTable

# Инициализация colorama
init(autoreset=True)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_console_encoding():
    """Устанавливает кодировку консоли для корректного отображения кириллицы."""
    if os.name == 'nt':
        # Устанавливаем кодировку консоли на cp866
        os.system('chcp 1251 >nul')
    else:
        # Для других операционных систем (например, Linux)
        sys.stdout.reconfigure(encoding='utf-8')

def get_net_sessions():
    """Получает текущие сетевые сессии."""
    result = subprocess.run(['net', 'session'], capture_output=True, text=True)
    return result.stdout

def get_netstat():
    """Получает активные сетевые подключения."""
    result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)
    return result.stdout

def get_security_events():
    """Получает события безопасности с ID 4624 и 4625."""
    server = 'localhost'
    log_type = 'Security'
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    hand = win32evtlog.OpenEventLog(server, log_type)
    total = win32evtlog.ReadEventLog(hand, flags, 0)
    events = []

    for event in total:
        if event.EventID == 4624 or event.EventID == 4625:
            events.append(event)

    win32evtlog.CloseEventLog(hand)
    return events

def print_section_header(header):
    """Печатает заголовок секции."""
    print(Fore.CYAN + "=" * 80)
    print(Fore.CYAN + header)
    print(Fore.CYAN + "=" * 80)

def print_net_sessions(sessions):
    """Печатает текущие сетевые сессии."""
    print_section_header("Текущие сетевые сессии")
    print(sessions)

def print_netstat(netstat):
    """Печатает активные сетевые подключения."""
    print_section_header("Активные сетевые подключения")
    print(netstat)

def print_security_events(events):
    """Печатает события безопасности в виде таблицы."""
    print_section_header("События безопасности (4624 и 4625)")
    
    table = PrettyTable()
    table.field_names = ["Event ID", "Time Generated", "Message"]
    
    # Установка максимальной ширины для каждого столбца
    table.max_width["Event ID"] = 10
    table.max_width["Time Generated"] = 25
    table.max_width["Message"] = 50
    
    # Установка выравнивания
    table.align["Event ID"] = "l"  # Выравнивание по левому краю
    table.align["Time Generated"] = "l"  # Выравнивание по левому краю
    table.align["Message"] = "l"  # Выравнивание по левому краю

    for event in events:
        try:
            event_data = win32evtlogutil.SafeFormatMessage(event)
            table.add_row([event.EventID, event.TimeGenerated, event_data])
        except Exception as e:
            print(f"{Fore.RED}Ошибка форматирования события: {e}")

    print(table)

def display_menu():
    """Отображает меню выбора."""
    print(Fore.CYAN + "=" * 80)
    print(Fore.CYAN + "DOGMOOD")
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + "1. Показать текущие сетевые сессии")
    print(Fore.YELLOW + "2. Показать активные сетевые подключения")
    print(Fore.YELLOW + "3. Показать события безопасности (4624 и 4625)")
    print(Fore.YELLOW + "0. Выход")
    print(Fore.CYAN + "=" * 80)

def main():
    """Основная функция для выполнения всех задач."""
    if not is_admin():
        print(Fore.RED + "Скрипт должен быть запущен с правами администратора.")
        return

    set_console_encoding()

    while True:
        display_menu()
        choice = input(Fore.YELLOW + "Выберите пункт меню: ")

       
        if choice == '1':
            sessions = get_net_sessions()
            print_net_sessions(sessions)
        elif choice == '2':
            netstat = get_netstat()
            print_netstat(netstat)
        elif choice == '3':
            events = get_security_events()
            print_security_events(events)
        elif choice == '0':
            print(Fore.GREEN + "Выход из программы...")
            break
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
