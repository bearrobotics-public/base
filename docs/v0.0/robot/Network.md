### Message Types
#### Authentication
  - **Fields:**
    - `username` (string): User provided input for enterprise networks requiring username.
For personal and unsecure networks, username may be omitted.
    - `password` (string): User provided input for password input for secure networks.
#### ConnectionOptions
  - **Fields:**
    - `cidr_ip` (string): Classless inter-domain routing IP used to configure a static IP.
This should be a static IPv4 address followed by a '/' and suffix.
e.g. '192.168.1.123/24'
    - `gateway_ip` (string): Network gateway that local traffic is routed to. e.g. '192.168.1.1'
    - `dns_ips` (string): A list of DNS servers to override the DNS resolution provided by the
host network. e.g. ['8.8.8.8', '8.8.4.4']
#### NetworkState
  - **Fields:**
    - `connected_wifi` [(Wifi)](#wifi): State related to the currently connected Wi-Fi.
No connected_wifi indicates that no Wi-Fi network is connected.
#### Wifi
  - **Fields:**
    - `ssid` (string): SSID of Wi-Fi network
    - `signal_strength` (int32): Signal strength of the connected Wi-Fi connection
in intervals of 5, within a range of 0 to 100.
    - `security` [(Security)](#security): Security requirements for the network
    - `connected_state` [(Connection)](#connection): Currently connected Wi-Fi state
  - **Enums:**

      | <a id="security">Security</a> | Numeric Value | Description                     |
      |:------------------------------|--------------:|:--------------------------------|
      | SECURITY_UNKNOWN              |             0 | Network security is unknown.    |
      | SECURITY_UNSECURED            |             1 | Unsecured network that do not require any authentication. |
      | SECURITY_PASSWORD_SECURED     |             2 | Password secured network. <br>e.g. WPA2, WPA3 and WEP networks |
      | SECURITY_USERNAME_PASSWORD_SECURED  |       3 | Login required network. <br>i.e. Enterprise networks |


      | <a id="connection">Connection</a>              | Numeric Value | Description                     |
      |:--------------------------|--------------:|:--------------------------------|
      | CONNECTION_UNKNOWN        |             0 | The family is unknown.          |
      | CONNECTION_BEAR_CONNECTED |             1 | Universe > Bear services and network connection are both working. |
      | CONNECTION_INTERNET_ONLY  |             2 | Internet is connected but universe connection cannot be established. |
      | CONNECTION_NO_INTERNET    |             3 | Network is connected but it does not have an internet connection. |

#### WifiConnections
  - **Fields:**
    - `saved_networks` [(Wifi)](#wifi): List of remembered Wi-Fi networks (not necessarily available)
    - `available_networks` [(Wifi)](#wifi): List of other available networks
#### WifiInfo
  - **Fields:**
    - `current_ssid` (string): Currently connected Wi-Fi network's SSID.
This will be empty if the robot is not connected to a network.
    - `cidr_ip` (string): Classless inter-domain routing IPv4 address followed by a suffix
representing the number of bits for the subnet mask.
e.g. "192.168.1.123/24"
    - `gateway_ip` (string): Gateway IP to direct local network traffic.
This typically mirrors the first 3 octets in the network IP with
the last octet ending in 1. e.g. "192.168.1.1"
    - `mac_address` (string): Unique MAC address for the Wi-Fi interface e.g. "aa:1a:a1:a1:1a:11"
    - `dns_ips` (string): A list of DNS servers to override the DNS resolution provided by the
host network. e.g. ['8.8.8.8', '8.8.4.4']

