import psutil

def get_memoryuse():
    mem = psutil.virtual_memory() 
    mem = mem.percent
    return mem

def get_cpuuse():
    cpu = psutil.cpu_percent(interval=1)
    return cpu
