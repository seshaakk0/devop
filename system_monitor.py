import shutil
import subprocess

print("===== LINUX SYSTEM HEALTH MONITOR =====")

print("\n1. MEMORY USAGE")
subprocess.run(["free", "-h"])
memory = subprocess.run(
    ["free"],
    capture_output=True,
    text=True
)

values = memory.stdout.splitlines()[1].split()

total_ram = int(values[1])
used_ram = int(values[2])

ram_usage = (used_ram / total_ram) * 100

print("RAM Usage:", round(ram_usage, 2), "%")

if ram_usage > 80:
    print("WARNING: RAM usage is high!")
else:
    print("RAM usage is healthy!")
print("\n2. CPU USAGE")
result = subprocess.run(
    ["mpstat", "1", "1"],
    capture_output=True,
    text=True
)

print(result.stdout)

idle = float(result.stdout.strip().splitlines()[-1].split()[-1])
cpu_usage = 100 - idle

print("CPU Usage:", round(cpu_usage, 2), "%")

if cpu_usage > 80:
    print("WARNING: CPU usage is high!")
else:
    print("CPU usage is healthy!")

print("\n3. DISK USAGE")

total, used, free = shutil.disk_usage("/")

usage = (used / total) * 100

print("Disk Usage:", round(usage, 2), "%")

if usage > 80:
    print("WARNING: Disk space is low!")
else:
    print("Disk space is healthy!")

print("\n4. SYSTEM UPTIME")
subprocess.run(["uptime"])

print("\n===== MONITORING COMPLETED =====")
