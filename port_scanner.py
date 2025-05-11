import socket
from datetime import datetime

def scan_ports(target, start_port, end_port, timeout=0.5):
    open_ports = []
    print(f"Taranıyor: {target} ({start_port}-{end_port})")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)

    end_time = datetime.now()
    duration = end_time - start_time
    return open_ports, duration

target = "127.0.0.1"
start_port = 75
end_port = 85

open_ports, duration = scan_ports(target, start_port, end_port)
print("Açık portlar:", open_ports)
print("Tarama süresi:", duration)
