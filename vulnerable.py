import subprocess
import sys


def ping_host(host):
    # Vulnérabilité volontaire : injection de commande via shell=True
    cmd = "ping -c 1 " + host
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vulnerable.py <host>")
        sys.exit(1)
    ping_host(sys.argv[1])
