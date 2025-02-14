# Settings

Settings are set through the [SetSetting](robot/RobotApiService.md#setsetting)
RPC. Both key and values are strings so types for each value must be filled as a
string.

To access the current and available settings, the [SubscribeSettings](robot/RobotApiService.md#subscribesettings)
RPC may be used.

## Maximum Navigation Speed

The maximum navigation speed of the robot. The robot will accelerate up to this
speed during navigation

Key | Unit | Min | Max | Default
----|------|-----|-----|--------
`robot-max-vel-x` | meters-per-second | `0.2` | `1.2` | `0.8`

## Wheel Coasting During Idle

Locking state of the wheels when the robot is idle.

True indicates that the wheels will not lock in idle. This allows the user to
push the robot during this state.

False indicate that the wheels will be locked during idle. This prevents the
robot from being pushed or from rolling if it is idle on a slope.

Key | Value | Default
----|-------|--------
`robot-enable-motors-coast-in-idle` | `True` \| `False` | `True`
