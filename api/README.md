# Edge-API

OpenAPI 3.0 specification for the Edge-API — the backend that sits between the BIND5G NaaS API and a Kubernetes
MEC cluster, exposing cluster inventory, namespace-scoped resource lifecycle, workload scaling, and KNF
orchestration through ETSI OSM.

- Specification: [`edge-api.yaml`](edge-api.yaml) — version 1.0.2, 32 paths, 46 operations
- License: Apache 2.0 (declared in the spec itself)

## Viewing it

```bash
npx @redocly/cli preview-docs api/edge-api.yaml
```

or paste it into [editor.swagger.io](https://editor.swagger.io/).

## Generating a client or server

Server stubs and clients are intentionally not committed — regenerate them when you need them:

```bash
# Python Flask server
docker run --rm -v "$PWD:/local" openapitools/openapi-generator-cli generate \
  -i /local/api/edge-api.yaml -g python-flask -o /local/out/server

# Python client
docker run --rm -v "$PWD:/local" openapitools/openapi-generator-cli generate \
  -i /local/api/edge-api.yaml -g python -o /local/out/client
```

## Endpoint groups

| Group | Operations |
|---|---|
| `/cluster/*` | Read-only inventory across all namespaces: nodes, node status, pods, deployments, services, ServiceMonitors, ResourceQuotas, LimitRanges |
| `/namespaces/*` | Create/list/delete namespaces; full lifecycle for pods (plus logs), deployments, services, ServiceMonitors, quotas, limit ranges |
| `/namespaces/{ns}/deployments/{name}/scaleHorizontal` | Adjust replica count |
| `/namespaces/{ns}/deployments/{name}/{container}/scaleVertical` | Adjust per-container CPU and memory |
| `/kns/*` | List, create, delete Kubernetes Network Services via OSM; trigger `day2actions` |

## Known limitations

- **No authentication.** The specification defines no `securitySchemes` and no `security` block, so every one of
  the 46 operations is unauthenticated — including `DELETE /namespaces/{name}` and the scaling endpoints. The
  design assumption was that this API runs on a private network behind the BIND5G NaaS API, which handled
  authorisation. Anyone reusing it on a reachable network needs to put authentication in front of it first.
- **No pagination.** The `/cluster/*` list endpoints return every object in every namespace in a single
  response.
- The `servers` block lists only `localhost:8084`, since the API was deployed next to the cluster it manages.
