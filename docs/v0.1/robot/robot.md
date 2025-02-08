

### Message Types

##### OdometryState

| Name | Type | Description |
|------|------|-------------|
| `pose` | [Pose](#pose) |  |
| `twist` | [Twist](../common/Math.md#twist) | A message containing the linear and angular velocity of the robot.<br>A positive linear velocity means the robot is moving forward in the<br>direction of the Pose.heading, while a negative is opposite of the<br>Pose.heading.<br>A positive angular velocity means the robot is turning clockwise when<br>looking from above, and negative is counter-clockwise when looking<br>from above.<br>If twist is 0, i.e. linear and angular velocities are 0, the robot is<br>stationary. |

##### Pose

| Name | Type | Description |
|------|------|-------------|
| `x_meters` | float | x, y coordinates inside the Map relative to the map’s specified<br>origin. |
| `y_meters` | float |  |
| `heading_radians` | float | The heading of the robot in radians. Ranges from -PI to PI, with<br>0.0 pointing along the x-axis. |

##### PoseWithCovariance

| Name | Type | Description |
|------|------|-------------|
| `pose` | [Pose](#pose) |  |
| `covariance` | double<br>*repeated* | A 36-element array, which is a flattened 6×6 covariance matrix in<br>row-major order. Each element represents the covariance between state<br>variables (X, Y, Z, X-axis rotation, Y-axis rotation, Z-axis rotation). |
