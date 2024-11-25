### Message Types
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
#### Pose
  - **Fields:**
    - `x_meters` (float): x coordinate inside the Map relative to the map’s specified origin.
    - `y_meters` (float): y coordinate inside the Map relative to the map’s specified origin.
    - `heading_radians` (float): The heading of the robot in radians. Ranges from -PI to PI, with
0.0 pointing along the x-axis.

