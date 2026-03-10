import psutil

print("Open Ports on Your Laptop:\n")

connections = psutil.net_connections()

open_ports = set()

for conn in connections:
    if conn.laddr and conn.status == 'LISTEN':
        open_ports.add(conn.laddr.port)

for port in sorted(open_ports):
    print("Port:", port)

print("\nTotal Open Ports:", len(open_ports))