

### Message Types

##### DirectionZone

| Name | Type | Description |
|------|------|-------------|
| `heading_radians` | float | The direction vector's angle in radians,<br>relative to the map's origin and measured from the x-axis. |
| `magnitude` | int32 | The magnitude of the direction vector.<br>Typically set to 254 for hard direction zones. The larger the magnitude, <br>the more the robot will try to align with the direction. |

##### ExclusiveZone

| Name | Type | Description |
|------|------|-------------|
| `max_robots` | int32 | Maximum number of robots allowed to enter the zone. |

##### ParameterZone

| Name | Type | Description |
|------|------|-------------|
| `zone_id` | string |  |
| `points` | [Point2D](../common/Math.md)<br>*repeated* | Polygon defining the zone.<br>The minimum number of points is 3. |
| `direction_zone` | [DirectionZone](#directionzone) |  |
| `exclusive_zone` | [ExclusiveZone](#exclusivezone) |  |
| `ramp_zone` | [RampZone](#rampzone) |  |
| `sound_zone` | [SoundZone](#soundzone) |  |
| `speed_zone` | [SpeedZone](#speedzone) |  |

##### RampZone
- *(No fields defined)*

##### SoundZone
- *(No fields defined)*

##### SpeedZone

| Name | Type | Description |
|------|------|-------------|
| `max_speed_m_per_sec` | float | Speed limit in the zone. |
