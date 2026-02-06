from config import SENSITIVE_PATHS, USB_PREFIXES, NETWORK_PREFIX

def is_sensitive(path):
    return any(path.startswith(p) for p in SENSITIVE_PATHS)

def is_usb(path):
    return any(path.startswith(p) for p in USB_PREFIXES)

def is_network(path):
    return path.startswith(NETWORK_PREFIX)
