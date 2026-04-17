import socket
from zeroconf import ServiceInfo, Zeroconf

def start_airplay_broadcast():
    # This makes your Dell look like a Mac/Apple TV to your iPhone
    local_ip = socket.gethostbyname(socket.gethostname())
    info = ServiceInfo(
        "_airplay._tcp.local.",
        "Dell-Mac-Mirror._airplay._tcp.local.",
        addresses=[socket.inet_aton(local_ip)],
        port=7000,
        properties={'deviceid': '00:11:22:33:44:55', 'model': 'AppleTV3,1', 'features': '0x7'}
    )
    zeroconf = Zeroconf()
    print(f"Service started! Look for 'Dell-Mac-Mirror' in your iPhone Screen Mirroring.")
    zeroconf.register_service(info)
    try:
        input("Press Enter to stop...\n")
    finally:
        zeroconf.unregister_service(info)
        zeroconf.close()

if __name__ == "__main__":
    start_airplay_broadcast()