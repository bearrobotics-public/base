### RobotAPIService

#### ConnectWifi
  - **Request Type:** [ConnectWifiRequest](#connectwifirequest)
  - **Response Type:** [ConnectWifiResponse](#connectwifiresponse)
  - **Description:**
  Clients can connect the base to an existing Wi-Fi network. <br> To connect to secure networks, `Authentication` can be set. <br>`ConnectionOptions` can be used if further configuration is needed for the Wi-Fi network.<br>
  `ssid` should be provided and nearby broadcasted networks may be scanned with ListWifiConnections.

**Example: Connecting to Wi-Fi Networks in ASCII Proto Format **
<br>
To connect to an open public Wi-Fi network `bear_public_wifi`:
```plaintext
// Sample Request
ssid: 'bear_public_wifi'
```
```plaintext
// Sample Response
{}
```
---
To connect to a private Wi-Fi network `bear_private_wifi` that requires a password:
```plaintext
// Sample Request
ssid: 'bear_private_wifi'
authentication {
  password: 'password_for_private'
}
```
```plaintext
// Sample Response
{}
```

---

**Example: To connect to a private Wi-Fi network `bear_private_wifi2` that requires a username and password:**
```plaintext
// Sample Request
ssid: 'bear_private_wifi2'
authentication {
  username: 'bear_user'
  password: 'password_for_private2'
}
```
```plaintext
// Sample Response
{}
```

---

**Example: To connect to an open public Wi-Fi network `bear_public_wifi2` that has a gateway and needs to specify DNS:**
```plaintext
// Sample Request
ssid: 'bear_public_wifi2'
connection_options {
  gateway_ip: '192.168.1.1'
  dns_ips: [ '1.1.1.1', '1.0.0.1', '8.8.8.8', '8.8.4.4' ]
}
```
```plaintext
// Sample Response
{}
```

---

#### GetSystemInfo
  - **Request Type:** [GetSystemInfoRequest](#getsysteminforequest)
  - **Response Type:** [GetSystemInfoResponse](#getsysteminforesponse)
  - **Description:**
  Get the overall robot system information.<br><br>When called, the server returns robot system information.<br>The system info tends to be static and does not change often.

**Example in ASCII proto format**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
system_Info {
  software_version: ‘base-slim-24.11.875;
  firmware_version: '3.6.0.2'
  robot_family: ROBOT_FAMILY_SERVI_PLUS
  robot_id: 'pennybot-xxxxxx'
  locale_language: 'en'
  wifi_info {
    current_ssid: 'bear_demo'
    cidr_ip: '10.1.30.104/24'
    gateway_ip: '10.1.30.1'
    macAddress: 'E4:C7:67:EE:FF:AA'
    dns_ips: [ '1.1.1.1', '1.0.0.1' ]
  }
}
```

---

#### ListWifiConnections
  - **Request Type:** [ListWifiConnectionsRequest](#listwificonnectionsrequest)
  - **Response Type:** [ListWifiConnectionsResponse](#listwificonnectionsresponse)
  - **Description:**
  List all available Wi-Fi networks as well as known Wi-Fi networks.

**Example in ASCII proto format**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
wifi_connections {
  saved_networks {
    ssid: 'bear_test'
    signal_strength: 90
    security: SECURITY_PASSWORD_SECURED
  }
  saved_networks {
    ssid: 'bear_public'
    signal_strength: 87
    security: SECURITY_UNSECURED
  }
  available_networks {
    ssid: 'bear_demo'
    signal_strength: 90
    security: SECURITY_PASSWORD_SECURED
  }
  available_networks {
    ssid: 'public_neighbor'
    signal_strength: 69
    security: SECURITY_UNSECURED
  }
  available_networks {
    ssid: 'bear_private'
    signal_strength: 90
    security: SECURITY_PASSWORD_SECURED
  }
}
```

---

#### SubscribeBatteryStatus
  - **Request Type:** [SubscribeBatteryStatusRequest](#subscribebatterystatusrequest)
  - **Response Type:** [SubscribeBatteryStatusResponse](#subscribebatterystatusresponse)
  - **Description:**
  Subscribe to the robot battery status.<br><br>Upon subscription, the latest known battery status is sent,<br>followed by updates whenever the battery status changes.

**Example in ASCII proto format where base is charging followed by disconnecting the charger**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
{
  metadata {
    timestamp {
      seconds: 1714313000
      nanos: 0
    }
    sequence_number: 50
  }
  battery_state {
    charge_percent: 99
    state: STATE_CHARGING
  }
}
{
  metadata {
    timestamp {
      seconds: 1714315000
      nanos: 0
    }
    sequence_number: 51
  }
  battery_state {
    charge_percent: 100
    state: STATE_CHARGING
  }
}
{
  metadata {
    timestamp {
      seconds: 1714316000
      nanos: 0
    }
    sequence_number: 52
  }
  battery_state {
    charge_percent: 100
    state: STATE_DISCHARGING
  }
}
{
  metadata {
    timestamp {
      seconds: 1714326000
      nanos: 0
    }
    sequence_number: 53
  }
  battery_state {
    charge_percent: 99
    state: STATE_DISCHARGING
  }
}
```

---

#### SubscribeNetworkStatus
  - **Request Type:** [SubscribeNetworkStatusRequest](#subscribenetworkstatusrequest)
  - **Response Type:** [SubscribeNetworkStatusResponse](#subscribenetworkstatusresponse)
  - **Description:**
  Subscribe to the robot's network status.<br><br>Upon subscription, the server immediately sends the latest known<br>network status, followed by updates whenever the network status<br>changes.

**Example in ASCII proto format where initially there is no Wi-Fi connection, then a Wi-Fi is connected, and disconnected again**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
{
  metadata {
    timestamp {
      seconds: 1732161076001
      nanos: 740591178
    }
    sequence_number: 15
  }
  network_state {}
}
{
  metadata {
    timestamp {
      seconds: 1732161076101
      nanos: 1654
    }
    sequence_number: 16
  }
  network_state {
    connected_wifi {
      ssid: 'bear_test'
      signal_strength: 90
      security: SECURITY_PASSWORD_SECURED
    }
  }
}
{
  metadata {
    timestamp {
      seconds: 1732161076540
      nanos: 905178
    }
    sequence_number: 17
  }
  network_state {}
}
```

---

#### SubscribeOdometryStatus
  - **Request Type:** [SubscribeOdometryStatusRequest](#subscribeodometrystatusrequest)
  - **Response Type:** [SubscribeOdometryStatusResponse](#subscribeodometrystatusresponse)
  - **Description:**
  Subscribe to the robot's odometry status.<br><br>Upon subscription, the server server provides regular updates (5Hz) of <br>the odometry status.

**Example in ASCII proto format**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
{
  metadata {
    timestamp {
      seconds: 1732363871000
      nanos: 966690012
    }
    sequence_number: 321
  }
  odometry_state {
    pose {
      x_meters: 0.44569823
      y_meters: 0.122843966
      heading_radians: 0.38896447
    }
    twist {
      linear_velocity: 0.04743719
      angular_velocity: 0.024076527
    }
  }
}
{
  metadata {
    timestamp {
      seconds: 1732363871001
      nanos: 148576818
    }
    sequence_number: 322
  }
  odometry_state {
    pose {
      x_meters: 0.44870216
      y_meters: 0.124077715
      heading_radians: 0.39042783
    }
    twist {
      linear_velocity: 0.00031081674
      angular_velocity: -0.00031484783
    }
  }
}
{
  metadata {
    timestamp {
      seconds: 1732363871001
      nanos: 340591393
    }
    sequence_number: 323
  }
  odometry_state {
    pose {
      x_meters: 0.44822562
      y_meters: 0.12388177
      heading_radians: 0.3896436
    }
    twist {
      linear_velocity: -8.1940074e-05
      angular_velocity: -0.00036711502
    }
  }
}
{
  metadata {
    timestamp {
      seconds: 1732363871001
      nanos: 528572177
    }
    sequence_number: 324
  }
  odometry_state {
    pose {
      x_meters: 0.44822484
      y_meters: 0.12388145
      heading_radians: 0.38963988
    }
    twist {}
  }
}
{
  metadata {
    timestamp {
      seconds: 1732363871001
      nanos: 768605432
    }
    sequence_number: 325
  }
  odometry_state {
    pose {
      x_meters: 0.44822484
      y_meters: 0.12388145
      heading_radians: 0.38963988
    }
    twist {}
  }
}
```

---

#### SubscribeRobotPose
  - **Request Type:** [SubscribeRobotPoseRequest](#subscriberobotposerequest)
  - **Response Type:** [SubscribeRobotPoseResponse](#subscriberobotposeresponse)
  - **Description:**
Clients can subscribe to receive robot pose updates.<br><br>Upon subscription, the latest known robot pose is received, followed by updates at 5Hz.

**Example in ASCII proto format**
```plaintext
// Sample Request
{}
```
```plaintext
// Sample Response
{
  metadata {
    timestamp {
      seconds: 1715262000
      nanos: 168576818
    }
    sequence_number: 175
  }
  pose {
    x_meters: 12.522097
    y_meters: -5.08858
    heading_radians: -1.3201984
  }
}
{
  metadata {
    timestamp {
      Seconds: 1715262000
      nanos: 360591391
    }
    sequence_number: 176
  }
  pose {
    x_meters: 12.522099
    y_meters: -5.088586
    heading_radians: -1.3201984
  }
}
{
  metadata {
    timestamp {
      Seconds: 1715262000
      nanos: 549562134
    }
    sequence_number: 177
  }
  pose {
    x_meters: 12.522101
    y_meters: -5.088586
    heading_radians: -1.3201984
  }
}
```

---

#### DriveRobot
  - **Request Type:** [DriveRobotRequest](#driverobotrequest)
  - **Response Type:** [DriveRobotResponse](#driverobotresponse)
  - **Description:**
  Manually drive the robot.<br><br>A fine grained level manual drive control that allows the user to<br>specify a desired linear and angular velocity. The command will be<br>smoothed by the robot.<br>The request message should be streamed at a rate of at least 5Hz for<br>smooth operation. If the frequency doesn't meet the requirements, it<br>will set the commanded velocity to zero.

**Example of driving in ASCII proto format**
Robot drives forward at 0.2 m/s
```plaintext
// Sample Request at 5Hz
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
```
```plaintext
// Sample Response
{}
```
Robot does an arced right turn at a constant speed of 0.2 m/s
```plaintext
// Sample Request at 5Hz
twist {
  linear_velocity: 0.2
  angular_velocity: 0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: 0.1
}
```
```plaintext
// Sample Response
{}
```
Robot does an arced left turn at a constant speed of -0.2 m/s
```plaintext
// Sample Request at 5Hz
twist {
  linear_velocity: 0.2
  angular_velocity: -0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: -0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: -0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: -0.1
}
twist {
  linear_velocity: 0.2
  angular_velocity: -0.1
}
```
```plaintext
// Sample Response
{}
```
Robot accelerating from speed of 0.2 m/s to 0.25 m/s forward
```plaintext
// Sample Request at 5Hz
twist {
  linear_velocity: 0.2
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.21
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.22
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.23
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.24
  angular_velocity: 0.0
}
twist {
  linear_velocity: 0.25
  angular_velocity: 0.0
}
```
```plaintext
// Sample Response
{}
```
---

### Message Types
#### ConnectWifiRequest
  - **Fields:**
    - `ssid` (string): SSID of Wi-Fi network.
    - `authentication` [(Authentication)](../Network/#authentication): Security details for the network.
This field can be omitted if the network is unsecure.
    - `connection_options` [(ConnectionOptions)](../Network/#connectionoptions): Optional parameters for static IP configuration.
#### ConnectWifiResponse
  - *(No fields defined)*
#### DriveRobotRequest
  - **Fields:**
    - `twist` [(Twist)](../../common/Math/#twist): The desired max linear and angular velocity to travel.
#### DriveRobotResponse
  - *(No fields defined)*
#### GetSystemInfoRequest
  - *(No fields defined)*
#### GetSystemInfoResponse
  - **Fields:**
    - `system_info` [(SystemInfo)](../System/#systeminfo): Robot system details
#### ListWifiConnectionsRequest
  - *(No fields defined)*
#### ListWifiConnectionsResponse
  - **Fields:**
    - `wifi_connections` [(WifiConnections)](../Network/#wificonnections): List of saved and available networks
#### SubscribeBatteryStatusRequest
  - *(No fields defined)*
#### SubscribeBatteryStatusResponse
  - **Fields:**
    - `metadata` [(EventMetadata)](../../common/Annotations/#eventmetadata): Timestamp and sequence number
    - `battery_state` [(BatteryState)](../Status/#batterystate): Battery and charge information
#### SubscribeNetworkStatusRequest
  - *(No fields defined)*
#### SubscribeNetworkStatusResponse
  - **Fields:**
    - `metadata` [(EventMetadata)](../../common/Annotations/#eventmetadata): Timestamp and sequence number
    - `network_state` [(NetworkState)](../Network/#networkstate): Network status
#### SubscribeOdometryStatusRequest
  - *(No fields defined)*
#### SubscribeOdometryStatusResponse
  - **Fields:**
    - `metadata` [(EventMetadata)](../../common/Annotations/#eventmetadata): Timestamp and sequence number
    - `odometry_state` [(OdometryState)](../Robot/#odometry_state): Current odometry information
#### SubscribeRobotPoseRequest
  - *(No fields defined)*
#### SubscribeRobotPoseResponse
  - **Fields:**
    - `metadata` [(EventMetadata)](../../common/Annotations/#eventmetadata): Timestamp and sequence number
    - `pose` [(Pose)](../Robot/#pose): Current robot position and orientation

