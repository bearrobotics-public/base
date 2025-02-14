

### Message Types

##### Destination

| Name | Type | Description |
|------|------|-------------|
| `destination_id` | string |  |

##### GenericGoal

| Name | Type | Description |
|------|------|-------------|
| `goal_type` | string | The type of the goal (e.g., "Pickup", "Dropoff"). |
| `parameters` | map<string, string\> | Any optional parameters for the goal in a key-value format. |

##### GenericMission

| Name | Type | Description |
|------|------|-------------|
| `type` | string | The type of the generic mission (e.g., "Traverse", "Loop"). |
| `goals` | [GenericGoal](#genericgoal)<br>*repeated* | A list of generic goals associated with the mission.<br>Each goal includes its type and other relevant information. |
| `override_params` | map<string, string\> | A map of key-value pairs for overriding default mission parameters.<br>This provides flexibility to customize the mission's behavior. |

##### Goal

| Name | Type | Description |
|------|------|-------------|
| `destination` | [Destination](#destination) |  |
| `zone` | [Zone](#zone) |  |
| `pose` | [Pose](Robot.md#pose) |  |

##### Mission

| Name | Type | Description |
|------|------|-------------|
| `type` | [Type](#missiontype) |  |
| `goals` | [Goal](#goal)<br>*repeated* | The list of goals or destinations for the mission. |
| `override_params` | [MissionParams](#missionparams) | Override parameters for the mission settings, allowing specific<br>configuration for this mission instance. |

###### Mission.Type

| Name               | Number | Description                                                                |
|--------------------|--------|----------------------------------------------------------------------------|
| `TYPE_UNKNOWN`       | 0      | Default value, indicates an unknown or unspecified mission type.           |
| `TYPE_ONEOFF`        | 1      | A single-goal mission.                                                     |
| `TYPE_ONEOFF_AUTO`   | 2      | An automated single-goal mission that selects the best available goal.     |
| `TYPE_TRAVERSE`      | 3      | A mission involving multiple destinations until a condition, such as weight limit, is met. |
| `TYPE_LOOP`          | 4      | A mission that repeatedly visits multiple destinations until a condition, such as weight limit, is met. |
| `TYPE_WAIT`          | 5      | A mission that remains at a specific location until triggered by an external event. |

##### MissionCommand

| Name | Type | Description |
|------|------|-------------|
| `mission_id` | string |  |
| `command` | Command |  |

###### MissionCommand.Command

| Name | Number | Description |
|------|--------|-------------|
| `COMMAND_UNKNOWN` | 0 | |
| `COMMAND_CANCEL` | 1 | |
| `COMMAND_PAUSE` | 2 | |
| `COMMAND_RESUME` | 3 | |
| `COMMAND_FINISH` | 4 | |

##### MissionParams

| Name | Type | Description |
|------|------|-------------|
| `traverse_params` | [TraverseParams](#traverseparams) |  |
| `loop_params` | [LoopParams](#loopparams) |  |

###### MissionParams.Mode

| Name | Number | Description |
|------|--------|-------------|
| `MODE_UNKNOWN` | 0 | |
| `MODE_DEFAULT` | 1 | |
| `MODE_BUSSING` | 2 | |

###### MissionParams.LoopParams

| Name | Type | Description |
|------|------|-------------|
| `mode` | [Mode](#missionparamsmode) |  |

###### MissionParams.TraverseParams

| Name | Type | Description |
|------|------|-------------|
| `mode` | [Mode](#missionparamsmode) |  |

##### MissionState

| Name | Type | Description |
|------|------|-------------|
| `mission_id` | string |  |
| `state` | [State](#missionstatestate) |  |
| `goals` | [Goal](#goal)<br>*repeated* | All goals for a given mission. |
| `current_goal_index` | int32 |  |
| `navigation_status` | [NavigationStatus](#missionstatenavigationstatus) | The current navigation status of the mission, reflecting the robot's<br>progress toward or at its destination. |
| `feedback` | [Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any) |  |

###### MissionState.NavigationStatus

| Name | Number | Description |
|------|--------|-------------|
| `NAVIGATION_STATUS_UNKNOWN` | 0 | Default value, indicates an unknown or undefined navigation status. |
| `NAVIGATION_STATUS_FINISHED` | 1 | Indicates that the robot has successfully arrived at its goal. |
| `NAVIGATION_STATUS_FINISHED` | 2 | Indicates that the robot failed to reach its goal. |
| `NAVIGATION_STATUS_STUCK` | 3 | Indicates that the robot is temporarily stuck but has not yet failed. |
| `NAVIGATION_STATUS_DOCKING` | 4 | Indicates that the robot is in the process of docking at a charger or station. |
| `NAVIGATION_STATUS_UNDOCKING` | 5 | Indicates that the robot is in the process of undocking at a charger or station. |
| `NAVIGATION_STATUS_NAVIGATING` | 6 | Indicates that the robot is navigating to a destination but is not currently docking or undocking. |

###### MissionState.State

| Name | Number | Description |
|------|--------|-------------|
| `STATE_UNKNOWN` | 0 | |
| `STATE_DEFAULT` | 1 | Initial state when no mission has been run (e.g. empty feedback). |
| `STATE_RUNNING` | 2 | |
| `STATE_PAUSED` | 3 | |
| `STATE_CANCELED` | 4 | |
| `STATE_SUCCEEDED` | 5 | |
| `STATE_FAILED` | 6 | |

##### Zone

| Name | Type | Description |
|------|------|-------------|
| `zone_id` | string |  |
