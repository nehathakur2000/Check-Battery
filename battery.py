import psutil

b=psutil.sensors_battery()
print(b.percent)
print(b.power_plugged)

a= psutil.net_io_counters
print(a)

print(psutil.cpu_freq())