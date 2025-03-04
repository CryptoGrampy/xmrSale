import subprocess
import time

import config
from pay import monerod


def open_tunnel(host, port):
    # If tunnel is required (might make things easier)
    try:
        if host is not None:
            command = [
                "ssh",
                config.tunnel_host,
                "-q",
                "-N",
                "-L",
                "{}:localhost:{}".format(port, port),
            ]
            print("Opening tunnel to {}.".format(" ".join(command)))
            tunnel_proc = subprocess.Popen(command)
            return tunnel_proc

        else:
            tunnel_proc = None
    except Exception as e:
        print("FAILED TO OPEN TUNNEL. Exception: {}".format(e))
        tunnel_proc = None
        pass
    return


def close_tunnel():
    if tunnel_proc is not None:
        tunnel_proc.kill()
        print("Tunnel closed.")
    return


# Open tunnel
if config.tunnel_host is not None:
    tunnel_proc = open_tunnel(config.tunnel_host, config.monerod_rpcport)
    tunnel_proc2 = open_tunnel(config.tunnel_host, config.monerowallet_rpcport)
    time.sleep(3)
else:
    print("Connecting to local node..")
    tunnel_proc = None
