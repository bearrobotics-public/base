

### Message Types

##### BatteryState

| Name | Type | Description |
|------|------|-------------|
| `charge_percent` | int32 | State of charge from 0 (battery empty) to 100 (battery full). |
| `state` | [State](#batterystatestate) |  |
| `charge_method` | [ChargeMethod](#batterystatechargemethod) |  |


###### BatteryState.ChargeMethod
| Name                     | Number | Description |
|--------------------------|--------|-------------|
| `CHARGE_METHOD_UNKNOWN`    | 0      |             |
| `CHARGE_METHOD_NOT_CHARGING` | 1    |             |
| `CHARGE_METHOD_WIRED`      | 2      |             |
| `CHARGE_METHOD_WIRELESS`   | 3      |             |

###### BatteryState.State

| Name               | Number | Description                                                                 |
|--------------------|--------|-----------------------------------------------------------------------------|
| `STATE_UNKNOWN`      | 0      |                                                                             |
| `STATE_CHARGING`     | 1      |                                                                             |
| `STATE_DISCHARGING`  | 2      | Robot is not connected to the charger and is draining energy from the battery. |
| `STATE_FULL`         | 3      | While connected to the charger, the battery is fully charged, no more energy can be stored into the battery. |

##### EmergencyStopState

| Name | Type | Description |
|------|------|-------------|
| `emergency` | [Emergency](#emergencystopstateemergency) |  |

###### EmergencyStopState.Emergency

| Name | Number | Description |
|------|--------|-------------|
| `EMERGENCY_UNKNOWN` | 0 | |
| `EMERGENCY_ENGAGED` | 1 | Triggers an emergency stop. Overrides and sets navigation-related velocity command to 0 to the motor. |
| `EMERGENCY_DISENGAGED` | 2 | Wheels will resume acting upon software navigation commands. |

##### OperationState

| Name | Type | Description |
|------|------|-------------|
| `system` | System |  |
| `system_message` | string | Optional message for human readability. Could be empty. |
| `emergency` | Emergency |  |
| `emergency_message` | string | Optional message for human readability. Could be empty. |
| `charging` | Charging |  |
| `mission` | Mission |  |

###### OperationState.Charging

| Name | Number | Description |
|------|--------|-------------|
| `CHARGING_UNKNOWN` | 0 | |
| `CHARGING_DISCHARGING` | 1 | No charging method is detected. The robot is able to navigate freely in this state. |
| `CHARGING_WIRED` | 2 |  The robot is connected to a cable charger. Navigation-related commands will be ignored until the cable charger is unplugged. |
| `CHARGING_WIRELESS` | 3 | The robot is charging without being plugged into a cable charger. (i.e. inductive or contact charger)<br> It is possible to navigate freely during this charging state. |

###### OperationState.Emergency

| Name | Number | Description |
|------|--------|-------------|
| `EMERGENCY_UNKNOWN` | 0 | |
| `EMERGENCY_ENGAGED` | 1 | Either robot's physical e-stop button is presses or a software e-stop has been triggered. Wheels are locked in a halted state and will not respond to software navigation commands. |
| `EMERGENCY_DISENGAGED` | 2 | Both physical e-stop button is released and software e-stop is not triggered. Wheels will resume acting up on software navigation commands. |

###### OperationState.Mission

| Name | Number | Description |
|------|--------|-------------|
| `MISSION_UNKNOWN` | 0 | |
| `MISSION_IDLE` | 1 | Indicates no mission is currently in progress irrespective of other states. |
| `MISSION_IN_PROGRESS` | 2 | The robot is currently on a mission. While in progress, the robot cannot accept any new mission. |

###### OperationState.System

| Name | Number | Description |
|------|--------|-------------|
| `SYSTEM_UNKNOWN` | 0 | |
| `SYSTEM_OK` | 1 | No faults are detected in system operation. |
| `SYSTEM_ERROR` | 2 | One or more errors are present on the robot. This could be software-related or hardware communication. The robot may not be operable depending on the nature of the error. |
