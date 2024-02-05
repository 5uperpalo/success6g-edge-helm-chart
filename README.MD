![GitHub](https://img.shields.io/github/license/5uperpalo/success6g-edge-helm-chart)

# success6g-edge-helm-chart

This repository is for the Helm chart for edge pod implementation in [SUCCESS6G](https://success-6g-project.cttc.es/) project.  We are using `gh-pages` branch to host and index the chart.  When modifying the chart please bump the version in the [Chart.yaml](/chart/edge/Chart.yaml) file.

## Publishing new Docker

Repository includes a [DockerFile](/edge_docker/Dockerfile)
```
cd edge_docker
# build the image
docker build -t success6g-edge-pod .
# correctly tag the image
docker image tag success6g-edge-pod 5uperpalo/success6g-edge-pod:[TAG]
# push the image to dockerhub
docker push 5uperpalo/success6g-edge-pod:[TAG]
```

## Installing using Helm

[Helm](https://helm.sh) must be installed to use the charts.
Please refer to Helm's [documentation](https://helm.sh/docs/) to get started.

The chart is accessible using the following commands:

Add the helm repo

```bash
helm repo add success6g-edge https://5uperpalo.github.io/success6g-edge-helm-chart
```

You can see the latest version by using the folllowing command:

```bash
helm search repo success6g-edge
```

If you would like to test and look at the manifest files before deploying you can run:

```bash
helm install success6g-edge success6g-edge/success6g-edge --namespace success6g-edge --create-namespace --dry-run --devel
```

Then to install run the following:

```bash
helm install success6g-edge success6g-edge/success6g-edge --namespace success6g-edge --create-namespace
```