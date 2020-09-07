import platform


sys_info = platform.uname()


print(sys_info.system)
print(sys_info.release)
print(sys_info.version)
print(sys_info.machine)
print(sys_info.processor)

