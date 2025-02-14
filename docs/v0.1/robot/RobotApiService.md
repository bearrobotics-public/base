# Robot API Service

The definition of Bear Robot API service.

### Map

#### GetAnnotation

- **Request Type:** [GetAnnotationRequest](#getannotationrequest)
- **Response Type:** [GetAnnotationResponse](#getannotationresponse)
- **Description:**
  Retrieve annotation data for a specified annotation_id from the Universe.<br>
  If offline, it uses the cached Annotation data.
#### GetLocation

- **Request Type:** [GetLocationRequest](#getlocationrequest)
- **Response Type:** [GetLocationResponse](#getlocationresponse)
- **Description:**
  Retrieve the current location data to which the robot is connected from
  the Universe. If the robot is offline, it uses the cached Location data.

#### GetMap

- **Request Type:** [GetMapRequest](#getmaprequest)
- **Response Type:** [GetMapResponse](#getmapresponse)
- **Description:**
  Retrieve the map corresponding to a given map_id from the Universe.<br>
  If offline, it uses the cached Map data.

#### GetMapContent

- **Request Type:** [GetMapContentRequest](#getmapcontentrequest)
- **Response Type:** [GetMapContentResponse](#getmapcontentresponse)
- **Description:**
  Retrieve the current map content data, which is loaded on the robot.

#### GetMapData
- **Request Type:** [GetMapDataRequest](#getmapdatarequest)
- **Response Type:** [GetMapDataResponse](#getmapdataresponse)
- **Description:**
  Retrieve map data for a specified map_data_id from the Universe.<br>
  If offline, it uses the cached MapData data.

#### SwitchMap

- **Request Type:** [SwitchMapRequest](#switchmaprequest)
- **Response Type:** [SwitchMapResponse](#switchmapresponse)
- **Description:**
  Switches the current map to a specified map.<br>
The request should specify a
  floor level and section index to be used. Returns the map_id of the switched
  map.

---

### Mission

#### AppendMission

- **Request Type:** [AppendMissionRequest](#appendmissionrequest)
- **Response Type:** [AppendMissionResponse](#appendmissionresponse)
- **Description:**
  Appends the given mission to the end of the queue.<br>
  The mission will be added in the order it is received.

#### ChargeRobot

- **Request Type:** [ChargeRobotRequest](#chargerobotrequest)
- **Response Type:** [ChargeRobotResponse](#chargerobotresponse)
- **Description:**
  Create a mission to go charge a robot regardless of battery state.<br>
  The call will fail if the robot is already on a different mission. The current
  mission needs to be canceled before the robot can be charged.

#### CreateMission

- **Request Type:** [CreateMissionRequest](#createmissionrequest)
- **Response Type:** [CreateMissionResponse](#createmissionresponse)
- **Description:**
  Creates a mission for a given type.<br>
  The call will fail if the robot cannot go on the requested mission.

#### SubscribeMissionStatus

- **Request Type:** [SubscribeMissionStatusRequest](#subscribemissionstatusrequest)
- **Response Type:** [SubscribeMissionStatusResponse](#subscribemissionstatusresponse)
- **Description:**
  Subscribe to robot's mission status.<br>
  Upon subscription, the server immediately sends the latest known mission
  status, followed by updates whenever the mission status changes.

#### UpdateMission

- **Request Type:** [UpdateMissionRequest](#updatemissionrequest)
- **Response Type:** [UpdateMissionResponse](#updatemissionresponse)
- **Description:**
  Updates the specified mission with the given command.<br>
  The call will fail if the robot is not on the specified mission or cannot
  execute the command.

---

### Navigation

#### DriveRobot

- **Request Type:** [DriveRobotRequest](#driverobotrequest)
- **Response Type:** [DriveRobotResponse](#driverobotresponse)
- **Description:**
  Manually drive the robot.<br>
  A fine grained level manual drive control that allows the user to specify a
  desired linear and angular velocity. The command will be smoothed by the
  robot. The request message should be streamed at a rate of at least 5Hz for
  smooth operation. If the frequency doesn't meet the requirements, it will set
  the commanded velocity to zero.

#### LocalizeRobot

- **Request Type:** [LocalizeRobotRequest](#localizerobotrequest)
- **Response Type:** [LocalizeRobotResponse](#localizerobotresponse)
- **Description:**
  Localize the robot to a localization goal.<br>
  If the goal is accepted, subcribe to SubscribeLocalizationStatus to get the
  localization status.

#### SetEmergencyStop

- **Request Type:** [SetEmergencyStopRequest](#setemergencystoprequest)
- **Response Type:** [SetEmergencyStopResponse](#setemergencystopresponse)
- **Description:**
  Enable or disable the emergency stop.

#### SetPose

- **Request Type:** [SetPoseRequest](#setposerequest)
- **Response Type:** [SetPoseResponse](#setposeresponse)
- **Description:**
  Manually set the robot pose given a pose on the map and covariance matrix.

#### SubscribeEmergencyStopStatus

- **Request Type:** [SubscribeEmergencyStopStatusRequest](#subscribeemergencystopstatusrequest)
- **Response Type:** [SubscribeEmergencyStopStatusResponse](#subscribeemergencystopstatusresponse)
- **Description:**
  Subscribe to the software emergency stop state.<br>
  Upon subscription, the server sends the current emergency stop state, followed
  by updates whenever the emergency stop state changes.

#### SubscribeLocalizationStatus

- **Request Type:** [SubscribeLocalizationStatusRequest](#subscribelocalizationstatusrequest)
- **Response Type:** [SubscribeLocalizationStatusResponse](#subscribelocalizationstatusresponse)
- **Description:**
  Subscribe to the robot's localization status.<br>
  Upon subscription, the latest known localization status will be sent. If the
  robot is actively localizing, status will be published upon changes.

#### SubscribeOdometryStatus

- **Request Type:** [SubscribeOdometryStatusRequest](#subscribeodometrystatusrequest)
- **Response Type:** [SubscribeOdometryStatusResponse](#subscribeodometrystatusresponse)
- **Description:**
  Subscribe to the robot's odometry status.<br>
  Upon subscription, the server provides regular updates (5Hz) of the odometry
  status.

#### SubscribeRobotPose

- **Request Type:** [SubscribeRobotPoseRequest](#subscriberobotposerequest)
- **Response Type:** [SubscribeRobotPoseResponse](#subscriberobotposeresponse)
- **Description:**
  Subscribe to the robot's pose.<br>
  Upon subscription, the server provides regular updates (5Hz) of the robot's
  estimated position.

---

### Settings

#### SetSetting

- **Request Type:** [SetSettingRequest](#setsettingrequest)
- **Response Type:** [SetSettingResponse](#setsettingresponse)
- **Description:**
  Set the specified setting.<br>
  The request will be rejected if the setting key does not exists.

#### SubscribeSettings

- **Request Type:** [SubscribeSettingsRequest](#subscribesettingsrequest)
- **Response Type:** [SubscribeSettingsResponse](#subscribesettingsresponse)
- **Description:**
  Upon subscription, the latest setting states will be sent.<br>
  For every setting change, a full snapshot of the states will be sent.

---

### Status

#### SubscribeBatteryStatus

- **Request Type:** [SubscribeBatteryStatusRequest](#subscribebatterystatusrequest)
- **Response Type:** [SubscribeBatteryStatusResponse](#subscribebatterystatusresponse)
- **Description:**
  Subscribe to the robot's battery status.<br>
  Upon subscription, the server immediately sends the latest known battery
  status, followed by updates whenever the battery status changes.

#### SubscribeOperationStatus

- **Request Type:** [SubscribeOperationStatusRequest](#subscribeoperationstatusrequest)
- **Response Type:** [SubscribeOperationStatusResponse](#subscribeoperationstatusresponse)
- **Description:**
  Subscribe to the robots's operation status.<br>
  Upon subscription, the server immediately sends the latest known operation
  status, followed by updates whenever the operation status changes.

---

### System

#### ConnectWifi

- **Request Type:** [ConnectWifiRequest](#connectwifirequest)
- **Response Type:** [ConnectWifiResponse](#connectwifiresponse)
- **Description:**
  Connect to a specified Wi-Fi network.<br>
  SSID should be provided and nearby broadcasted networks may be scanned with
  ListWifiConnections.

#### ForgetWifi

- **Request Type:** [ForgetWifiRequest](#forgetwifirequest)
- **Response Type:** [ForgetWifiResponse](#forgetwifiresponse)
- **Description:**
  Forget a saved Wi-Fi network.<br>
  When called, it forgets a Wi-Fi network identified by its ssid. The call will
  fail if a network operation is in progress or the network is not found.

#### GetSystemInfo

- **Request Type:** [GetSystemInfoRequest](#getsysteminforequest)
- **Response Type:** [GetSystemInfoResponse](#getsysteminforesponse)
- **Description:**
  Get the overall robot system information.<br>
  When called, the server returns robot system information. The system info
  tends to be static and does not change often.

#### ListWifiConnections

- **Request Type:** [ListWifiConnectionsRequest](#listwificonnectionsrequest)
- **Response Type:** [ListWifiConnectionsResponse](#listwificonnectionsresponse)
- **Description:**
  List available and remembered network connections.<br>
  When called, the server returns lists of remembered Wi-Fi networks, which may
  not necessarily be available, and returns lists of other available networks.

#### RunSystemCommand

- **Request Type:** [RunSystemCommandRequest](#runsystemcommandrequest)
- **Response Type:** [RunSystemCommandResponse](#runsystemcommandresponse)
- **Description:**
  Execute a system command on the robot.<br>
  Runs a system command. e.g. initiate robot reboot.
  Refer to the SystemCommand proto for all available commands.

#### SubscribeNetworkStatus

- **Request Type:** [SubscribeNetworkStatusRequest](#subscribenetworkstatusrequest)
- **Response Type:** [SubscribeNetworkStatusResponse](#subscribenetworkstatusresponse)
- **Description:**
  Subscribe to the robot's network status.<br>
  Upon subscription, the server immediately sends the latest known network
  status, followed by updates whenever the network status changes.

#### SubscribeSystemStatus

- **Request Type:** [SubscribeSystemStatusRequest](#subscribesystemstatusrequest)
- **Response Type:** [SubscribeSystemStatusResponse](#subscribesystemstatusresponse)
- **Description:**
  Subscribe to the robot's system status.<br>
  Upon subscription, the server immediately sends the latest known system
  status, followed by updates whenever the system status changes.

## Message Types

##### AppendMissionRequest

| Name | Type | Description |
|------|------|-------------|
| `mission` | [Mission](Mission.md#mission) |  |

##### AppendMissionResponse

| Name | Type | Description |
|------|------|-------------|
| `mission_id` | string | The unique identifier of the appended mission. |

##### ChargeRobotRequest

- *(No fields defined)*

##### ChargeRobotResponse

| Name | Type | Description |
|------|------|-------------|
| `mission_id` | string |  |

##### ConnectWifiRequest

| Name | Type | Description |
|------|------|-------------|
| `ssid` | string | SSID of Wi-Fi network. |
| `authentication` | [Authentication](Network.md#authentication) | Security details for the network.<br>This field can be omitted if the network is unsecure. |
| `connection_options` | [ConnectionOptions](Network.md#connectionoptions) | Optional parameters for static IP configuration. |

##### ConnectWifiResponse

- *(No fields defined)*

##### CreateMissionRequest

| Name | Type | Description |
|------|------|-------------|
| `mission` | [Mission](Mission.md#mission) |  |

##### CreateMissionResponse

| Name | Type | Description |
|------|------|-------------|
| `mission_id` | string |  |

##### DriveRobotRequest

| Name | Type | Description |
|------|------|-------------|
| `twist` | [Twist](../common/Math.md#twist) | The desired max linear and angular velocity to travel. |

##### DriveRobotResponse

- *(No fields defined)*

##### ForgetWifiRequest

| Name | Type | Description |
|------|------|-------------|
| `ssid` | string |  |

##### ForgetWifiResponse

- *(No fields defined)*

##### GetAnnotationRequest

| Name | Type | Description |
|------|------|-------------|
| `annotation_id` | string |  |

##### GetAnnotationResponse

| Name | Type | Description |
|------|------|-------------|
| `annotation` | [Annotation](../location/Annotation.md#annotation) |  |

##### GetLocationRequest

- *(No fields defined)*

##### GetLocationResponse

| Name | Type | Description |
|------|------|-------------|
| `location` | [Location](../location/Location.md#location) |  |

##### GetMapContentRequest

- *(No fields defined)*

##### GetMapContentResponse

| Name | Type | Description |
|------|------|-------------|
| `map_content` | [MapContent](../location/Map.md#mapcontent) |  |

##### GetMapDataRequest

| Name | Type | Description |
|------|------|-------------|
| `map_data_id` | string |  |

##### GetMapDataResponse

| Name | Type | Description |
|------|------|-------------|
| `map_data` | [MapData](../location/Map.md#mapdata) |  |

##### GetMapRequest

| Name | Type | Description |
|------|------|-------------|
| `map_id` | string |  |

##### GetMapResponse

| Name | Type | Description |
|------|------|-------------|
| `map` | [Map](../location/Map.md#map) |  |

##### GetSystemInfoRequest

- *(No fields defined)*

##### GetSystemInfoResponse

| Name | Type | Description |
|------|------|-------------|
| `system_info` | [SystemInfo](System.md#systeminfo) |  |

##### ListWifiConnectionsRequest

- *(No fields defined)*

##### ListWifiConnectionsResponse

| Name | Type | Description |
|------|------|-------------|
| `wifi_connections` | [WifiConnections](Network.md#wificonnections) |  |

##### LocalizeRobotRequest

| Name | Type | Description |
|------|------|-------------|
| `goal` | [LocalizationGoal](Localization.md#localizationgoal) |  |

##### LocalizeRobotResponse

- *(No fields defined)*

##### RunSystemCommandRequest

| Name | Type | Description |
|------|------|-------------|
| `system_command` | [SystemCommand](System.md#systemcommand) |  |

##### RunSystemCommandResponse

- *(No fields defined)*

##### SetEmergencyStopRequest

| Name | Type | Description |
|------|------|-------------|
| `e_stop_state` | [EmergencyStopState](Status.md#emergencystopstate) |  |

##### SetEmergencyStopResponse

- *(No fields defined)*

##### SetPoseRequest

| Name | Type | Description |
|------|------|-------------|
| `pose_with_covariance` | [PoseWithCovariance](Robot.md#posewithcovariance) | A pose and a covariance matrix, if the covariance is not set, the internal default values will be applied. |

##### SetPoseResponse

- *(No fields defined)*

##### SetSettingRequest

| Name | Type | Description |
|------|------|-------------|
| `setting` | [Setting](Settings.md#setting) |  |

##### SetSettingResponse

- *(No fields defined)*

##### SubscribeBatteryStatusRequest

- *(No fields defined)*

##### SubscribeBatteryStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `battery_state` | [BatteryState](Status.md#batterystate) |  |

##### SubscribeEmergencyStopStatusRequest

- *(No fields defined)*

##### SubscribeEmergencyStopStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `e_stop_state` | [EmergencyStopState](Status.md#emergencystopstate) |  |

##### SubscribeLocalizationStatusRequest

- *(No fields defined)*

##### SubscribeLocalizationStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetatdata) |  |
| `localization_state` | [LocalizationState](Localization.md#localizationstate) |  |

##### SubscribeMissionStatusRequest

- *(No fields defined)*

##### SubscribeMissionStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `mission_state` | [MissionState](Mission.md#missionstate) |  |

##### SubscribeNetworkStatusRequest

- *(No fields defined)*

##### SubscribeNetworkStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `network_state` | [NetworkState](Network.md#networkstate) |  |

##### SubscribeOdometryStatusRequest

- *(No fields defined)*

##### SubscribeOdometryStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `odometry_state` | [OdometryState](Robot.md#odometrystate) |  |

##### SubscribeOperationStatusRequest

- *(No fields defined)*

##### SubscribeOperationStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `operation_state` | [OperationState](Status.md#operationstate) |  |

##### SubscribeRobotPoseRequest

- *(No fields defined)*

##### SubscribeRobotPoseResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `pose` | [Pose](Robot.md#pose) |  |

##### SubscribeSettingsRequest

- *(No fields defined)*

##### SubscribeSettingsResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `settings_state` | [SettingsState](Settings.md#settingsstate) |  |

##### SubscribeSystemStatusRequest

- *(No fields defined)*

##### SubscribeSystemStatusResponse

| Name | Type | Description |
|------|------|-------------|
| `metadata` | [EventMetadata](../common/Annotations.md#eventmetadata) |  |
| `system_state` | [SystemState](System.md#systemstate) |  |

##### SwitchMapRequest

| Name | Type | Description |
|------|------|-------------|
| `floor_level` | int32 |  |
| `section_index` | int32 |  |

##### SwitchMapResponse

| Name | Type | Description |
|------|------|-------------|
| `map_id` | string |  |

##### UpdateMissionRequest

| Name | Type | Description |
|------|------|-------------|
| `mission_command` | [MissionCommand](Mission.md#missioncommand) |  |

##### UpdateMissionResponse

- *(No fields defined)*
