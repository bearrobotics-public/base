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