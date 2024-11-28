### Message Types

#### BatteryState
  - **Fields:**
    - `charge_percent` (int32): State of charge percent from 0 (empty) ~ 100 (full).
    - `state` [(State)](#state): Represents the current state of the battery.
  - **Enums:**

      | <a id="state">State</a> | Numeric Value | Description                   |
      |:------------------------|--------------:|:------------------------------|
      | STATE_UNKNOWN           |             0 | The state is unknown.         |
      | STATE_CHARGING          |             1 | The battery is charging.      |
      | STATE_DISCHARGING       |             2 | The battery is discharging.   |
      | STATE_FULL              |             3 | The battery is fully charged. |


#### OdometryState
  - **Fields:**
    - `pose` [(Pose)](#pose): Current robot position and orientation
    - `twist` [(Twist)](../../common/Math/#twist): A message containing the linear and angular velocity of the robot.

A positive linear velocity means the robot is moving forward in the
direction of the Pose.heading, while a negative is opposite of the
Pose.heading.

A positive angular velocity means the robot is turning clockwise when
looking from above, and negative is counter-clockwise when looking
from above.

If twist is 0, i.e. linear and angular velocities are 0, the robot is
stationary.