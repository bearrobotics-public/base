

### Message Types

##### Map

| Name | Type | Description |
|------|------|-------------|
| `map_id` | string | Example: "9578" |
| `created_time` | [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |
| `modified_time` | [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |
| `display_name` | string | Example: "ITCT SEOUL" |
| `map_data_id` | string | Current map data identifier that represents this map. |
| `annotation_ids` | string<br>*repeated* | List of annotation identifiers associated with this map. |
| `current_annotation_id` | string | Current annotation identifier. |

##### MapContent

| Name | Type | Description |
|------|------|-------------|
| `map_id` | string |  |
| `data` | [Data](#mapcontentdata) |  |
| `annotation` | [Annotation](Annotation.md#annotation) |  |

###### MapContent.Annotation

| Name | Type | Description |
|------|------|-------------|
| `destinations` | [Destination](Annotation.md#destination)<br>*repeated* |  |

###### MapContent.Data

| Name | Type | Description |
|------|------|-------------|
| `data` | bytes | The image PNG data for the map. |
| `origin` | [Origin](#origin) |  |
| `m_per_pixel` | float | Maps real-world size to pixelated size. (meters per pixel)<br>This value is equivalent to the resolution defined in the ROS map server. <br>https://wiki.ros.org/map_server |

##### MapData

| Name | Type | Description |
|------|------|-------------|
| `map_data_id` | string |  |
| `url` | string | URL to the image data for the map. |
| `origin` | [Origin](#origin) | The Origin of the map. |
| `m_per_pixel` | float | Maps real-world size to pixelated size (meters per pixel)<br>This value is equivalent to the "resolution" defined in the ROS map server <br>https://wiki.ros.org/map_server |

##### Origin

| Name | Type | Description |
|------|------|-------------|
| `x_m` | float | This is the (x, y) coordinate of the origin of the map in the world frame. |
| `y_m` | float | This is the y-coordinate of the origin of the map in the world frame. |
| `yaw_radians` | float | This is the rotation around the z-axis (counterclockwise)<br>of the map with respect to the world frame. A yaw of 0 means no rotation. |
