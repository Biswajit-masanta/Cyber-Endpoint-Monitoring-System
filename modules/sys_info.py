import socket
import platform

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version()
    }