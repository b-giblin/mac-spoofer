import subprocess

# bring down mac
config_down = "ifconfig eth0 down"
# change mac
change_mac = "ifconfig eth0 hw ether 00:11:22:33:44:66"
# bring mac back up
mac_up = "ifconfig eth0 up"


subprocess.call(config_down, shell=True)
subprocess.call(change_mac, shell=True)
subprocess.call(mac_up, shell=True)



