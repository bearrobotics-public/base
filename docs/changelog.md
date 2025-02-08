# Changelog

## v0.1 - February 5, 2025

### Breaking Changes

- OdometryState has been moved from `robot/status.proto` to `robot/robot.proto`

### Newly Added Endpoints

API are now grouped in the following categories:

- [Map](../v0.1/robot/RobotApiService#map)
- [Mission](../v0.1/robot/RobotApiService#mission)
- [Navigation](../v0.1/robot/RobotApiService#navigation)
- [Settings](../v0.1/robot/RobotApiService#settings)
- [Status](../v0.1/robot/RobotApiService#status)
- [System](../v0.1/robot/RobotApiService#system)

#### [Map](../v0.1/robot/RobotApiService#map)

- [GetAnnotation](../v0.1/robot/RobotApiService#getannotation)
- [GetLocation](../v0.1/robot/RobotApiService#getlocation)
- [GetMap](../v0.1/robot/RobotApiService#getmap)
- [GetMapContent](../v0.1/robot/RobotApiService#getmapcontent)
- [GetMapData](../v0.1/robot/RobotApiService#getmapdata)
- [SwitchMap](../v0.1/robot/RobotApiService#switchmap)

#### [Mission](../v0.1/robot/RobotApiService#mission)

- [AppendMission](../v0.1/robot/RobotApiService#appendmission)
- [ChargeRobot](../v0.1/robot/RobotApiService#chargerobot)
- [CreateMission](../v0.1/robot/RobotApiService#createmission)
- [SubscribeMissionStatus](../v0.1/robot/RobotApiService#subscribemissionstatus)
- [UpdateMission](../v0.1/robot/RobotApiService#updatemission)

#### [Navigation](../v0.1/robot/RobotApiService#navigation)

- [LocalizeRobot](../v0.1/robot/RobotApiService#localizerobot)
- [SetEmergencyStop](../v0.1/robot/RobotApiService#setemergencystop)
- [SetPose](../v0.1/robot/RobotApiService#setpose)
- [SubscribeEmergencyStopStatus](../v0.1/robot/RobotApiService#subscribeemergencystopstatus)
- [SubscribeLocalizationStatus](../v0.1/robot/RobotApiService#subscribelocalizationstatus)

#### [Settings](../v0.1/robot/RobotApiService#settings)

- [SetSetting](../v0.1/robot/RobotApiService#setsetting)
- [SubscribeSettings](../v0.1/robot/RobotApiService#subscribesettings)

#### [Status](../v0.1/robot/RobotApiService#status)

- [SubscribeOperationStatus](../v0.1/robot/RobotApiService#subscribeoperationstatus)

#### [System](../v0.1/robot/RobotApiService#system)

- [ForgetWifi](../v0.1/robot/RobotApiService#forgetwifi)
- [RunSystemCommand](../v0.1/robot/RobotApiService#runsystemcommand)
- [SubscribeSystemStatus](../v0.1/robot/RobotApiService#subscribesystemstatus)

## v0.0 - December 5, 2024

The start of the journey...

### Newly Added Endpoints

- [ConnectWifi](../v0.0/robot/RobotApiService#connectwifi)
- [DriveRobot](../v0.0/robot/RobotApiService#driverobot)
- [GetSystemInfo](../v0.0/robot/RobotApiService.md#getsysteminfo)
- [ListWifiConnections](../v0.0/robot/RobotApiService#listwificonnections)
- [SubscribeBatteryStatus](../v0.0/robot/RobotApiService#subscribebatterystatus)
- [SubscribeNetworkStatus](../v0.0/robot/RobotApiService#subscribenetworkstatus)
- [SubscribeOdometryStatus](../v0.0/robot/RobotApiService#subscribeodometrystatus)
- [SubscribeRobotPose](../v0.0/robot/RobotApiService#subscriberobotpose)
