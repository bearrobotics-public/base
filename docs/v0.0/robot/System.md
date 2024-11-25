### Message Types
#### SystemInfo
  - **Fields:**
    - `software_version` (string): Distribution version e.g. "servi-24.03"
    - `firmware_version` (string): Firmware version e.g. "3.2.4.1"
    - `robot_family` [(RobotFamily)](#robot_family): Robot product family
    - `robot_id` (string): Unique robot id e.g. "pennybot-abc123"
    - `display_name` (string): Display name set for the robot e.g. "Sir V"
    - `locale_language` (string): IETF language tag represented in string e.g. "en-US"
    - `wifi_info` [(WifiInfo)](../Network/#wifi_info): Various information of the wireless interface and connected Wi-Fi
network.
  - **Enums:**

      | <a id="robot_family">RobotFamily</a> | Numeric Value | Description                     |
      |:-------------------------------------|--------------:|:--------------------------------|
      | ROBOT_FAMILY_UNKNOWN                 |             0 | The family is unknown.          |
      | ROBOT_FAMILY_SERVI                   |             1 | The robot is a SERVI.           |
      | ROBOT_FAMILY_SERVI_MINI              |             2 | The robot is a SERVI MINI.      |
      | ROBOT_FAMILY_SERVI_PLUS              |             3 | The robot is a SERVI PLUS.      |
      | ROBOT_FAMILY_SERVI_LIFT              |             4 | The robot is a SERVI MINI LIFT. |