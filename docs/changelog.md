# Changelog

## v0.1 - February 5, 2025

### Breaking Changes

- [OdometryState](v0.1/robot/Robot.md#odometrystate) has been moved from `robot/status.proto` to `robot/robot.proto`

### Newly Added Endpoints

API are now grouped in the following categories:

- [Map](v0.1/robot/RobotApiService.md#map)
- [Mission](v0.1/robot/RobotApiService.md#mission)
- [Navigation](v0.1/robot/RobotApiService.md#navigation)
- [Settings](v0.1/robot/RobotApiService.md#settings)
- [Status](v0.1/robot/RobotApiService.md#status)
- [System](v0.1/robot/RobotApiService.md#system)

#### [Map](v0.1/robot/RobotApiService.md#map)

- [GetAnnotation](v0.1/robot/RobotApiService.md#getannotation)
- [GetLocation](v0.1/robot/RobotApiService.md#getlocation)
- [GetMap](v0.1/robot/RobotApiService.md#getmap)
- [GetMapContent](v0.1/robot/RobotApiService.md#getmapcontent)
- [GetMapData](v0.1/robot/RobotApiService.md#getmapdata)
- [SwitchMap](v0.1/robot/RobotApiService.md#switchmap)

#### [Mission](v0.1/robot/RobotApiService.md#mission)

- [AppendMission](v0.1/robot/RobotApiService.md#appendmission)
- [ChargeRobot](v0.1/robot/RobotApiService.md#chargerobot)
- [CreateMission](v0.1/robot/RobotApiService.md#createmission)
- [SubscribeMissionStatus](v0.1/robot/RobotApiService.md#subscribemissionstatus)
- [UpdateMission](v0.1/robot/RobotApiService.md#updatemission)

#### [Navigation](v0.1/robot/RobotApiService.md#navigation)

- [LocalizeRobot](v0.1/robot/RobotApiService.md#localizerobot)
- [SetEmergencyStop](v0.1/robot/RobotApiService.md#setemergencystop)
- [SetPose](v0.1/robot/RobotApiService.md#setpose)
- [SubscribeEmergencyStopStatus](v0.1/robot/RobotApiService.md#subscribeemergencystopstatus)
- [SubscribeLocalizationStatus](v0.1/robot/RobotApiService.md#subscribelocalizationstatus)

#### [Settings](v0.1/robot/RobotApiService.md#settings)

- [SetSetting](v0.1/robot/RobotApiService.md#setsetting)
- [SubscribeSettings](v0.1/robot/RobotApiService.md#subscribesettings)

#### [Status](v0.1/robot/RobotApiService.md#status)

- [SubscribeOperationStatus](v0.1/robot/RobotApiService.md#subscribeoperationstatus)

#### [System](v0.1/robot/RobotApiService.md#system)

- [ForgetWifi](v0.1/robot/RobotApiService.md#forgetwifi)
- [RunSystemCommand](v0.1/robot/RobotApiService.md#runsystemcommand)
- [SubscribeSystemStatus](v0.1/robot/RobotApiService.md#subscribesystemstatus)

## v0.0 - December 5, 2024

The start of the journey...

### Newly Added Endpoints

- [ConnectWifi](../v0.0/robot/RobotApiService.md#connectwifi)
- [DriveRobot](../v0.0/robot/RobotApiService.md#driverobot)
- [GetSystemInfo](../v0.0/robot/RobotApiService.md#getsysteminfo)
- [ListWifiConnections](../v0.0/robot/RobotApiService.md#listwificonnections)
- [SubscribeBatteryStatus](../v0.0/robot/RobotApiService.md#subscribebatterystatus)
- [SubscribeNetworkStatus](../v0.0/robot/RobotApiService.md#subscribenetworkstatus)
- [SubscribeOdometryStatus](../v0.0/robot/RobotApiService.md#subscribeodometrystatus)
- [SubscribeRobotPose](../v0.0/robot/RobotApiService.md#subscriberobotpose)
