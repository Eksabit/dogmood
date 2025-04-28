import subprocess
import win32evtlog
import win32evtlogutil
import win32security
import win32api
import win32con

def get_net_sessions():
    result = subprocess.run(['net', 'session'], capture_output=True, text=True)
    return result.stdout

def get_netstat():
    result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)
    return result.stdout

def get_security_events():
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

def main():
    print("Текущие сетевые сессии:")
    print(get_net_sessions())
    print("\nАктивные сетевые подключения:")
    print(get_netstat())
    print("\nСобытия безопасности (4624 и 4625):")
    events = get_security_events()
    for event in events:
        print(f"Event ID: {event.EventID}, Time Generated: {event.TimeGenerated}, String Inserts: {event.StringInserts}")

if __name__ == "__main__":
    main()
