import os, time, GPUtil, psutil, socket

class SystemMonitor:
    def kb_to_gb(self, kb):
        return round(kb / 1024**3, 1)

    def bytes_to_kb(self, value):
        return round(value/1024./1024.*8, 2)

    def get_mem(self):
        mem_info = psutil.virtual_memory()
        mem_total, mem_used, men_free = self.kb_to_gb(mem_info.total), self.kb_to_gb(mem_info.used), self.kb_to_gb(mem_info.free)
        data = [
            {"name": "总内存", "value": mem_total, "color": "#42d392"},
            {"name": "已使用", "value": mem_used, "color": "#ff9900"},
            {"name": "剩余", "value": men_free, "color": "#5f8bee"},
        ]

        return data

    def get_disk(self):
        disk_info = psutil.disk_partitions()
        disk_dict = {}
        for disk in disk_info:
            if disk.fstype:
                device = disk.device.split(":")[0] if ":" in disk.device else disk.device
                disk_dict[device] = [
                    {"name": "总容量", "value": round(self.kb_to_gb(psutil.disk_usage(disk.mountpoint).total), 2), "color": "#42d392"},
                    {"name": "已使用", "value": round(self.kb_to_gb(psutil.disk_usage(disk.mountpoint).used), 2), "color": "#ff9900"},
                    {"name": "剩余", "value": round(self.kb_to_gb(psutil.disk_usage(disk.mountpoint).free), 2), "color": "#5f8bee"},
                ]

        return disk_dict

    def get_net(self):
        old_upload_value, old_download_val = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv
        time.sleep(1)
        new_upload_value, new_download_val = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv
        upload_speed, download_speed = self.bytes_to_kb(new_upload_value - old_upload_value), self.bytes_to_kb(new_download_val - old_download_val)

        return [upload_speed, download_speed]

    def get_cpu(self):
        cpu_count_logical = psutil.cpu_count(logical=True)
        cpu_count = psutil.cpu_count(logical=False)
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_used = cpu_percent / cpu_count_logical * 100

        return [cpu_count_logical, cpu_count, cpu_used]


    def get_gpu(self):
        gpu_dict = {}
        gpus = GPUtil.getGPUs()

        for gpu in gpus:
            gpu_dict[gpu.id] = {
                'name': gpu.name,
                'load': gpu.load * 100,
                'free': gpu.memoryFree,
                'used': gpu.memoryUsed,
                'total': gpu.memoryTotal,
                'temp': gpu.temperature
            }

        return gpu_dict

    def get_user_info(self):
        hostname = socket.gethostname()
        user_login = os.getlogin()
        ip_address = socket.gethostbyname(hostname)

        return [user_login, hostname, ip_address]