

### Message Types

##### SystemCommand

| Name | Type | Description |
|------|------|-------------|
| `reboot` | [RebootCommand](#systemcommandrebootcommand) |  |

###### SystemCommand.RebootCommand

- *(No fields defined)*

##### SystemInfo

| Name | Type | Description |
|------|------|-------------|
| `software_version` | string | Distribution version. e.g. `"servi-24.03"` |
| `firmware_version` | string | Firmware version. e.g. `"3.2.4.1"` |
| `robot_family` | [RobotFamily](#systeminforobotfamily) | Robot product family. |
| `robot_id` | string | Unique robot ID. e.g. `"pennybot-abc123"` |
| `display_name` | string | Display name set for the robot. e.g. `"Sir V"` |
| `locale_language` | string | IETF language tag represented in string. e.g. `"en-US"` |
| `wifi_info` | [WifiInfo](Network.md#wifiinfo) | Various information of the wireless interface and connected Wi-Fi network. |

###### SystemInfo.RobotFamily

| Name | Number | Description |
|------|--------|-------------|
| `ROBOT_FAMILY_UNKNOWN` | 0 | |
| `ROBOT_FAMILY_SERVI` | 1 | |
| `ROBOT_FAMILY_SERVI_MINI` | 2 | |
| `ROBOT_FAMILY_SERVI_PLUS` | 3 | |
| `ROBOT_FAMILY_SERVI_LIFT` | 4 | |

##### SystemState

| Name | Type | Description |
|------|------|-------------|
| `health` | [Health](#systemstatehealth) | State representing whether robot is in a healthy condition. |

###### SystemState.Health

| Name | Number | Description |
|------|--------|-------------|
| `HEALTH_UNKNOWN` | 0 | |
| `HEALTH_OK` | 1 | |
| `HEALTH_ERROR` | 2 | |
