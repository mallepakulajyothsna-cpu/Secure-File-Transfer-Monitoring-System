import time
import os
import psutil
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler

from integrity import calculate_hash
from detector import is_sensitive, is_usb, is_network
from logger import log_event, alert

# -------------------------------------------------
# Ignore system / temp paths
# -------------------------------------------------

IGNORE_KEYWORDS = [
    "\\appdata\\",
    "\\windows\\",
    "\\program files\\",
    "\\program files (x86)\\",
    ".tmp",
    ".log",
    ".cache"
]

def should_ignore(path):
    path = path.lower()
    return any(keyword in path for keyword in IGNORE_KEYWORDS)

# -------------------------------------------------
# Helper: get user & process name
# -------------------------------------------------

def get_user_and_process():
    try:
        proc = psutil.Process()
        return proc.username(), proc.name()
    except Exception:
        return "UNKNOWN", "UNKNOWN"

# -------------------------------------------------
# File Monitoring Handler
# -------------------------------------------------

class WindowsFileMonitor(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            self.process_event("CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process_event("MODIFIED", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.process_move(event.src_path, event.dest_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.process_delete(event.src_path)

    # ---------- CREATE / MODIFY ----------
    def process_event(self, action, path):
        if should_ignore(path):
            return

        file_hash = calculate_hash(path)
        user, process = get_user_and_process()

        log_event(
            f"{action} | Source: {path} | User: {user} | "
            f"Process: {process} | Hash: {file_hash}"
        )

    # ---------- MOVE / TRANSFER ----------
    def process_move(self, src, dest):
        if should_ignore(src) or should_ignore(dest):
            return

        user, process = get_user_and_process()
        src_hash = calculate_hash(src)
        sensitive = is_sensitive(src)

        log_event(
            f"MOVED | Source: {src} | Destination: {dest} | "
            f"User: {user} | Process: {process}"
        )

        # Unauthorized movement detection
        if sensitive and (is_usb(dest) or is_network(dest)):
            alert(
                f"Unauthorized transfer detected | "
                f"Sensitive file moved to {dest}"
            )

        # Integrity check
        if src_hash:
            dest_hash = calculate_hash(dest)
            if src_hash != dest_hash:
                alert(
                    f"Integrity violation | Hash mismatch after transfer | "
                    f"File: {dest}"
                )

    # ---------- DELETE ----------
    def process_delete(self, path):
        if should_ignore(path):
            return

        user, process = get_user_and_process()
        log_event(
            f"DELETED | Path: {path} | User: {user} | Process: {process}"
        )

# -------------------------------------------------
# Main Execution
# -------------------------------------------------

if __name__ == "__main__":

    WATCH_PATH = r"C:\Users\malle\OneDrive\Documents\SensitiveData"

    if not os.path.exists(WATCH_PATH):
        print(f"❌ Watch path does not exist: {WATCH_PATH}")
        print("Create it first and run again.")
        exit(1)

    observer = PollingObserver(timeout=1)
    observer.schedule(
        WindowsFileMonitor(),
        WATCH_PATH,
        recursive=True
    )
    observer.start()

    print("🛡️ Secure File Transfer Monitoring System Started")
    print(f"📂 Monitoring sensitive directory: {WATCH_PATH}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
        observer.stop()

    observer.join()
