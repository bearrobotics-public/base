

### Message Types

##### Authentication

| Name | Type | Description |
|------|------|-------------|
| `username` | string<br>*optional* | User provided input for enterprise networks requiring username.<br>For personal and unsecure networks, username may be omitted. |
| `password` | string | User provided input for password input for secure networks. |

##### ConnectionOptions

| Name | Type | Description |
|------|------|-------------|
| `cidr_ip` | string | Classless inter-domain routing IP used to configure a static IP.<br>This should be a static IPv4 address followed by a ‘/’ and suffix.<br>e.g. `"192.168.1.123/24"` |
| `gateway_ip` | string | Network gateway that local traffic is routed to. e.g. `"192.168.1.1"` |
| `dns_ips` | string<br>*repeated* | A list of DNS servers to override the DNS resolution provided by the host<br>network. e.g. `["8.8.8.8", "8.8.4.4"]` |

##### NetworkState

| Name | Type | Description |
|------|------|-------------|
| `connected_wifi` | [Wifi](#wifi)<br>*repeated* | State related to the currently connected Wi-Fi.<br>No connected_wifi indicates that no Wi-Fi network is connected. |

##### Wifi

| Name | Type | Description |
|------|------|-------------|
| `ssid` | string | SSID of Wi-Fi network. |
| `signal_strength` | int32 | Signal strength of the connected Wi-Fi connection in intervals of 5,<br>within a range of 0 to 100. |
| `security` | [Security](#wifisecurity) | Security requirements for the network. |
| `connected_state` | [Connection](#wificonnection) | Currently connected Wi-Fi state. |

###### Wifi.Connection

| Name | Number | Description |
|------|--------|-------------|
| `CONNECTION_UNKNOWN` | 0 | |
| `CONNECTION_BEAR_CONNECTED` | 1 | Universe > Bear services and network connection are both working. |
| `CONNECTION_INTERNET_ONLY` | 2 | Internet is connected but universe connection cannot be established. |
|  `CONNECTION_NO_INTERNET` | 3 | Network is connected but it does not have an internet connection. |

###### Wifi.Security

| Name | Number | Description |
|------|--------|-------------|
| `SECURITY_UNKNOWN` | 0 | |
| `SECURITY_UNSECURED` | 1 | Unsecured network that do not require any authentication. |
| `SECURITY_PASSWORD_SECURED` | 2 | Password secured network. e.g. WPA2, WPA3 and WEP networks |
| `SECURITY_USERNAME_PASSWORD_SECURED` | 3 | Login required network. i.e. Enterprise networks |

##### WifiConnections

| Name | Type | Description |
|------|------|-------------|
| `saved_networks` | [Wifi](#wifi)<br>*repeated* | List of remembered Wi-Fi networks. (not necessarily available) |
| `available_networks` | [Wifi](#wifi)<br>*repeated* | List of other available networks. |

##### WifiInfo

| Name | Type | Description |
|------|------|-------------|
| `current_ssid` | string | Currently connected Wi-Fi network’s SSID.<br>This will be empty if the robot is not connected to a network. |
| `cidr_ip` | string | Classless inter-domain routing IPv4 address followed by a suffix<br>representing the number of bits for the subnet mask.<br>e.g. `“192.168.1.123/24”` |
| `gateway_ip` | string | Gateway IP to direct local network traffic.<br>This typically mirrors the first 3 octets in the network IP with<br>the last octet ending in 1. e.g. “192.168.1.1” |
| `mac_address` | string | Unique MAC address for the Wi-Fi interface. e.g. `“aa:1a:a1:a1:1a:11”` |
| `dns_ips` | string<br>*repeated* | A list of DNS servers to override the DNS resolution provided by the host<br>network. e.g. `["8.8.8.8", "8.8.4.4"]` |
