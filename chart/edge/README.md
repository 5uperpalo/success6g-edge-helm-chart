# SUCCESS6G-EDGE

Edge pod in SUCCESS6G project uses Redis database to receive vehicle On Board Unit(OBU) measurements

## Parameters

| Name           | Description                     | Value |
| -------------- | ------------------------------- | ----- |
| `nameOverride` | overrides the name of the chart | `""`  |


## Resources

| Name                        | Description    | Value   |
| --------------------------- | -------------- | ------- |
| `resources.requests.cpu`    | cpu request    | `100m`  |
| `resources.requests.memory` | memory request | `200Mi` |
| `resources.limits.cpu`      | cpu limit      | `100m`  |
| `resources.limits.memory`   | memory limit   | `200Mi` |


## Service

| Name                  | Description                 | Value       |
| --------------------- | --------------------------- | ----------- |
| `service.annotations` | annotations for the service | `{}`        |
| `service.type`        | the service type            | `ClusterIP` |
| `service.port`        | the service port            | `6666`      |