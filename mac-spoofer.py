import optparse
import random
import subprocess

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address.")

# specify the interface you wish to change the mac of
interface = input("Specify the interface: ")


try:
  if interface == 'eth0' or 'wlan0':
    user_interface = interface
except:
  ("Error. Invalid interface specified.")



# change mac to a random one
random_mac = ("52:54:00:%02x:%02x:%02x" % (
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  ))



# subprocess.call(f"ifconfig {interface} down", shell=True)
# subprocess.call(f"ifconfig {interface} hw ether {random_mac}", shell=True)
# subprocess.call(f"ifconfig {interface} up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", random_mac])
subprocess.call(["ifconfig", interface, "up"])








