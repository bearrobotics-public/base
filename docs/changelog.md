# Changelog

<!-- TODO: set the official release date once Robot SW 26.02 ships to Prod. -->
## v1.3 - Robot SW 26.02 (June 2026)

Adds documentation for the **v1** robot API
(`bearrobotics.api.v1.services.robot.APIService`), aligned with Robot SW 26.02.

!!! note
    The v1 API is a new surface published alongside the existing
    [v0.1](v0.1/robot/RobotApiService.md) API.

### Newly Added Endpoints

API is grouped into the following categories:

#### [Mission](v1.3/resources/Mission.md)

- [CreateMission](v1.3/resources/Mission.md#createmission)
- [CreateMissionBatch](v1.3/resources/Mission.md#createmissionbatch)
- [CreateMissionWorkflow](v1.3/resources/Mission.md#createmissionworkflow)
- [AppendMission](v1.3/resources/Mission.md#appendmission)
- [AppendMissionBatch](v1.3/resources/Mission.md#appendmissionbatch)
- [ChargeRobot](v1.3/resources/Mission.md#chargerobot)
- [ClearMissionStatus](v1.3/resources/Mission.md#clearmissionstatus)
- [SkipGoal](v1.3/resources/Mission.md#skipgoal)
- [UpdateMission](v1.3/resources/Mission.md#updatemission)
- [SubscribeMissionStatus](v1.3/resources/Mission.md#subscribemissionstatus)

#### [Robot Status](v1.3/resources/RobotStatus.md)

- [GetRobotStatus](v1.3/resources/RobotStatus.md#getrobotstatus)
- [SubscribeRobotStatus](v1.3/resources/RobotStatus.md#subscriberobotstatus)
- [SubscribeNavigationStatus](v1.3/resources/RobotStatus.md#subscribenavigationstatus)
- [SubscribeErrorCodes](v1.3/resources/RobotStatus.md#subscribeerrorcodes)

#### [Robot System](v1.3/resources/RobotSystem.md)

- [RunSystemCommand](v1.3/resources/RobotSystem.md#runsystemcommand)

#### [Settings](v1.3/resources/Settings.md)

- [GetSettings](v1.3/resources/Settings.md#getsettings)
- [GetAllSettings](v1.3/resources/Settings.md#getallsettings)
- [SetSetting](v1.3/resources/Settings.md#setsetting)
- [ResetSettings](v1.3/resources/Settings.md#resetsettings)

#### [Servi](v1.3/resources/Servi.md)

- [CalibrateTrays](v1.3/resources/Servi.md#calibratetrays)

#### [Carti](v1.3/resources/Carti.md)

- [GetConveyorIndex](v1.3/resources/Carti.md#getconveyorindex)
- [SubscribeConveyorStatus](v1.3/resources/Carti.md#subscribeconveyorstatus)
- [ControlConveyor](v1.3/resources/Carti.md#controlconveyor)

### Minimum Robot Software Versions (for full support)

1. Servi: 26.02
2. Carti: 26.02
3. AMR: 26.02

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

- [GetLocation](v0.1/robot/RobotApiService.md#getlocation)
- [GetMapContent](v0.1/robot/RobotApiService.md#getmapcontent)
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

## v0.0 - December 5, 2024

The start of the journey...

### Newly Added Endpoints

- [ConnectWifi](v0.0/robot/RobotApiService.md#connectwifi)
- [DriveRobot](v0.0/robot/RobotApiService.md#driverobot)
- [GetSystemInfo](v0.0/robot/RobotApiService.md#getsysteminfo)
- [ListWifiConnections](v0.0/robot/RobotApiService.md#listwificonnections)
- [SubscribeBatteryStatus](v0.0/robot/RobotApiService.md#subscribebatterystatus)
- [SubscribeNetworkStatus](v0.0/robot/RobotApiService.md#subscribenetworkstatus)
- [SubscribeOdometryStatus](v0.0/robot/RobotApiService.md#subscribeodometrystatus)
- [SubscribeRobotPose](v0.0/robot/RobotApiService.md#subscriberobotpose)
