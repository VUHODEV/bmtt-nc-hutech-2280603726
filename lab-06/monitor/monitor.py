import psutil
import platform
import socket
import logging
import time

# Cấu hình logging
logging.basicConfig(level=logging.INFO, filename="system_monitor.log", format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def log_info(category, message):
    """ Ghi log và hiển thị thông tin """
    logger.info(f"{category} - {message}")
    print(f"{category} - {message}")
    
def monitor_cpu_memory():
    """ Giám sát CPU và RAM """
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    
    log_info("CPU", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")

def monitor_system_info():
    """ Giám sát thông tin hệ thống """
    os_info = platform.uname()
    hostname = socket.gethostname()
    
    log_info("System Info", f"Hostname: {hostname}")
    log_info("System Info", f"OS: {os_info.system} {os_info.release}")
    log_info("System Info", f"Python Version: {platform.python_version()}")

def monitor_network():
    """ Giám sát mạng """
    net_stats = psutil.net_io_counters()
    log_info("Network", f"Bytes Sent: {net_stats.bytes_sent}, Bytes Received: {net_stats.bytes_recv}")

def monitor_software():
    """ Giám sát phần mềm đang chạy """
    software_list = psutil.process_iter(attrs=['pid', 'name', 'username'])
    log_info("Software", "Running processes:")
    
    for software in software_list:
        try:
            software_name = software.info['name']
            software_pid = software.info['pid']
            software_username = software.info['username']
            log_info("Software", f"PID: {software_pid}, Name: {software_name}, User: {software_username}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Bỏ qua các process không thể truy cập

def monitor_system():
    """ Chạy chương trình giám sát hệ thống """
    log_info("System Monitor", "Starting system monitor...")

    while True:
        monitor_cpu_memory()
        monitor_system_info()
        monitor_network()
        monitor_software()
        
        log_info("System Monitor", "------------------------------------")
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()
