import subprocess
import random

# bring down mac
config_down = "ifconfig eth0 down"

# change mac to a random one
random_mac = ("52:54:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        ))
change_mac = f"ifconfig eth0 hw ether {random_mac}"
# bring mac back up
mac_up = "ifconfig eth0 up"


subprocess.call(config_down, shell=True)
subprocess.call(change_mac, shell=True)
subprocess.call(mac_up, shell=True)



