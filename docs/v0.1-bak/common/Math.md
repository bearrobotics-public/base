

### Message Types

##### Point2D

| Name | Type | Description |
|------|------|-------------|
| `x` | float | The x coordinate of the point in a 2D plane. |
| `y` | float | The y coordinate of the point in a 2D plane. |

##### PointWithOrientation

| Name | Type | Description |
|------|------|-------------|
| `x` | float | The x coordinate of the point. |
| `y` | float | The y coordinate of the point. |
| `orientation` | [Quaternion](#quaternion) | The orientation represented as a quaternion. |

##### Quaternion

| Name | Type | Description |
|------|------|-------------|
| `x` | float | The x component of the quaternion (imaginary part). |
| `y` | float | The y component of the quaternion (imaginary part). |
| `z` | float | The z component of the quaternion (imaginary part). |
| `w` | float | The real (scalar) component of the quaternion. |

##### Twist

| Name | Type | Description |
|------|------|-------------|
| `linear_velocity` | float | The desired speed to drive up to in meters-per-second (m/s).<br>A positive value should be used for driving forward and a negative<br>value may be used to drive in reverse. |
| `angular_velocity` | float | The desired rate of rotation in radians-per-second (rad/s).<br>A positive value is used for a clockwise (right) point turn while a<br>negative value should be used for counter-clockwise (left) point turn. |
