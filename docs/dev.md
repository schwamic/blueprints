# Developer Documentation

## DevOps

Install and setup the following technologies:

### [Docker Desktop](https://docs.docker.com/desktop/) (Container, Kubernetes)

1. Fix context ([Docs](https://docs.docker.com/desktop/kubernetes/)):
```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
```

2. Setup [Docker for FastAPI](https://fastapi.tiangolo.com/deployment/docker/?h=docker#fastapi-in-containers-docker)

### [mogenius](https://mogenius.com) (Kubernetes Management)

1. Create an organisation
2. Create a cluster -> Install mogenius operator via helm ([Docs](https://docs.mogenius.com/tutorials/how-to-deploy-docker-container-on-kubernetes))
```bash
# find old deployment
helm list --all-namespacesCopied!
# delete old deployment
helm uninstall <deployment name> --namespace <namespace_name>
# install new deployment
helm install [...]
```

## Backend

* FastAPI (REST + ~Websockets)
* OpenAI API to generate Missions

## Frontend

* React
