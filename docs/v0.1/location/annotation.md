

### Message Types

##### Annotation

| Name | Type | Description |
|------|------|-------------|
| `annotation_id` | string | Example: "67305" |
| `created_time` | [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |
| `display_name` | string | Example: "ITCT annotation A" |
| `obstacles` | [Obstacle](#obstacle)<br>*repeated* | Areas on the map that the robot will try to avoid. |
| `parameter_zones` | [ParameterZone](Zones.md#parameterzone)<br>*repeated* | Areas on the map that have specific parameters. |
| `destinations` | [Destination](#destination)<br>*repeated* | Destinations are used to define the single point of interest. |
| `preferred_paths` | [PreferredPath](#preferredpath)<br>*repeated* | Directional and Bi-Directional paths<br>which robots will try to follow when nearby. |
| `queues` | [Queue](#queue)<br>*repeated* | Queues are used to define the waiting area. |

##### Destination

| Name | Type | Description |
|------|------|-------------|
| `destination_id` | string |  |
| `display_name` | string |  |
| `destination_pose` | [PointWithOrientation](../common/Math.md#pointwithorientation) | Position on the map where the robot would try to navigate to and orient<br>itself along that direction. |
| `type` | [Type](#destinationtype) |  |
| `docking_param` | [DockingParam](#dockingparam) | DockingParam is used to specify the docking process at the destination.<br>If docking_param exists, docking is needed.<br>If docking_param does not exist, no docking is needed. |
| `default_type_data` | [StringMapData](#stringmapdata) | Data specific to the destination type.<br>The robot will use this data to interact with the destination. |

###### Destination.Type

| Name | Number | Description |
|------|-------|-------------|
| `TYPE_UNKNOWN` | 0 | |
| `TYPE_DEFAULT` | 1 | The default destination type. The robot will try to navigate to this point. |
| `TYPE_CONTACT_CHARGER` | 2 | The contact-type charger. The robot can charge through docking. |
| `TYPE_INDUCTIVE_CHARGER` | 3 | The inductive-type charger. The robot can charge through docking, but no physical contact is needed. |

##### DockingParam

| Name | Type | Description |
|------|------|-------------|
| `type` | [Type](#dockingparamtype) |  |
| `reference` | [Reference](#dockingparamreference) |  |
| `reference_id` | string |  |
| `tuning_params` | [Point2D](../common/Math.md#point2d) | The tuning parameters are used to define relative docking pose to the<br>reference. |

###### DockingParam.Reference

| Name | Number | Description |
|------|-------|-------------|
| `REFERENCE_UNKNOWN` | 0 | |
| `REFERENCE_DEFAULT` | 1 | The default reference is different for each destination type. For example, the default reference for TYPE_CONTACT_CHARGER is VL Marker. |
| `REFERENCE_QR_CODE` | 2 | The QR code reference is used to specify the docking position. |
| `REFERENCE_VL_MARKER` | 3 | The VL marker reference is used to specify the docking position. |

###### DockingParam.Type

| Name | Number | Description |
|------|-------|-------------|
| `TYPE_UNKNOWN` | 0 | |
| `TYPE_DEFAULT` | 1 | The robot will run the default docking process at the destination. |

##### StringMapData

| Name | Type | Description |
|------|------|-------------|
| `data` | [DataEntry](#dataentry) |  |

##### DataEntry

| Name | Type | Description |
|------|------|-------------|
| `key` | string |  |
| `value` | string |  |

##### Obstacle

| Name | Type | Description |
|------|------|-------------|
| `obstacle_id` | string |  |
| `points` | [Point2D](../common/Math.md#point2d)<br>*repeated* | Points that define a polygon where the robot should avoid entering.<br>The minimum number of points is 3. |
| `type` | [Type](#obstacletype) |  |

###### Obstacle.Type

| Name | Number | Description |
|------|-------|-------------|
| `TYPE_UNKNOWN` | 0 | |
| `TYPE_SOFT_OBSTACLE` | 1 | Soft obstacle that the robot will try to avoid, but can still drive through if necessary. |
| `TYPE_RESTRICTED_OBSTACLE` | 2 | Restricted obstacle that the robot cannot enter and cannot exit if it becomes stuck inside this zone. |

##### PreferredPath

| Name | Type | Description |
|------|------|-------------|
| `preferred_path_id` | string |  |
| `graph_nodes` | [GraphNode](Types.md#graphnode)<br>*repeated* | List of graph nodes that make up the preferred path. |

##### Queue

| Name | Type | Description |
|------|------|-------------|
| `queue_id` | string |  |
| `queue_poses` | [GraphNode](Types.md#graphnode)<br>*repeated* | Represents a list of queuing points where the robot will wait. |
| `destination_ids` | string<br>*repeated* | These are end destinations that a queue can dequeue the robot to. |
