import socket
from zeroconf import ServiceInfo, Zeroconf
import threading

def start_broadcast():
    local_ip = socket.gethostbyname(socket.gethostname())
    info = ServiceInfo(
        "_airplay._tcp.local.",
        "Dell-Mac-Mirror._airplay._tcp.local.",
        addresses=[socket.inet_aton(local_ip)],
        port=7000,
        properties={'deviceid': '00:11:22:33:44:55', 'model': 'AppleTV3,1', 'features': '0x7'}
    )
    zeroconf = Zeroconf()
    print(f"iPhone Mirroring is ACTIVE. Connect to 'Dell-Mac-Mirror'.")
    zeroconf.register_service(info)
    
    # This part waits for the iPhone to send video data
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((local_ip, 7000))
    server_socket.listen(1)
    
    try:
        while True:
            client, addr = server_socket.accept()
            print(f"iPhone Connected from {addr}! Receiving stream...")
            # In a full build, we'd pass 'client' data to a video player here.
    except KeyboardInterrupt:
        zeroconf.unregister_service(info)
        zeroconf.close()

if __name__ == "__main__":
    start_broadcast()