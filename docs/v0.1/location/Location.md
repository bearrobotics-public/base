

### Message Types

##### Location

| Name | Type | Description |
|------|------|-------------|
| `location_id` | string | Example: "4RVF" |
| `created_time` | [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |
| `modified_time` | [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |
| `display_name` | string | Examples: "City Deli & Grill", "KNTH" |
| `floors` | map<int32, [Floor](#locationfloor)\> | Map of floor identifiers to floor information.<br>The key is the floor level, and the value is the floor information. |

###### Location.Floor

| Name | Type | Description |
|------|------|-------------|
| `display_name` | string | Example: "Ground" |
| `sections` | [Section](#section) |  |

####### Location.Floor.Section

| Name | Type | Description |
|------|------|-------------|
| `display_name` | string | Usually display_name will be empty if the section is not named. |
| `map_ids` | string<br>*repeated* | List of map identifiers associated with this section. |
| `current_map_id` | string | Current map identifier. |
