

### Message Types

##### LocalizationGoal

| Name | Type | Description |
|------|------|-------------|
| `pose` | [Pose](Robot.md#pose) |  |

##### LocalizationState

| Name | Type | Description |
|------|------|-------------|
| `state` | State |  |

###### LocalizationState.State

| Name             | Number | Description                                               |
|------------------|--------|-----------------------------------------------------------|
| `STATE_UNKNOWN`    | 0      |                                                           |
| `STATE_PREEMPTED`  | 1      | Happens when the localization process is preempted before completion. |
| `STATE_FAILED`     | 2      |                                                           |
| `STATE_SUCCEEDED`  | 3      |                                                           |
| `STATE_LOCALIZING` | 4      | The robot is actively performing localization.            |
