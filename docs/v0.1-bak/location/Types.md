

### Message Types

##### GraphNode

| Name | Type | Description |
|------|------|-------------|
| `graph_node_id` | string |  |
| `graph_node_pose` | [PointWithOrientation](../common/Math.md#pointwithorientation) | Point with orientation of the GraphNode. |
| `adjacent_graph_node_ids` | string<br>*repeated* | Adjacent GraphNode IDs that robot can navigate from the current GraphNode. |
