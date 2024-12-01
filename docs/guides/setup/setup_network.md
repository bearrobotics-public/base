### Network Connectivity

Using the Bear Robot API Server does not require an internet connection. However, an internet connection is required to get the full experience with Universe (Bear's fleet management system) integration.

#### Local Connectivity (Ethernet)

The ethernet port on Bear's PC is configured with IP **10.10.127.2**. You need to set up network configuration to ensure packets can reach between your PC and Bear's PC.

**1. Check the interface name for the ethernet connection**  
In this example, the interface name is `enxf8e43bc77e2f`:
```bash
ip addr show
```
**Example Output:**
```bash
7: enxf8e43bc77e2f: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000                       
   link/ether f8:e4:3b:c7:7e:2f brd ff:ff:ff:ff:ff:ff                                               
   inet6 fe80::93ee:2155:af0c:a3e8/64 scope link noprefixroute                                      
      valid_lft forever preferred_lft forever                      
```


**2. Configure the network interface through a persistent configuration file**:

In this example, we are using IP **10.10.127.3**. The configuration file may be different based on your machine. The following instructions is for Ubuntu/Debian-based systems.

If you have a `/etc/network/interfaces` file (on older systems), append the following to the file:

```bash
auto enxf8e43bc77e2f
iface enxf8e43bc77e2f inet static
    address 10.10.127.3
    netmask 255.255.255.0
    gateway 10.10.127.1  # Optional, if you don't require internet access from this interface, omit this line.
```
Apply the changes
```bash
sudo systemctl restart networking
```

If you have a `/etc/netplan/01-*.yaml` file (on newer systems), append the following under `network`:
```bash
network:
   # ...
   # additional settings here
   # ...
   ethernets:
      enxf8e43bc77e2f:
         dhcp4: no
         addresses:
           - 10.10.127.3/24
```
Apply the changes
```bash
sudo netplan apply
```

**3. Run a ping test to ensure you can communicate with Bear's PC** (**10.10.127.2**):
```bash
ping 10.10.127.2
```

If the ping transmits successful packets, then you can now communicate with BRAS!

#### Connecting to WiFi

Internet connection is required to connect to Universe (Bear's fleet management system). You can use [ConnectWifi](../../../v0/robot/RobotApiService/#connectwifi) to set the network.

