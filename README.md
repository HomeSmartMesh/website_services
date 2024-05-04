# website_services
Copper pipeline for markdown website building

# Usage

run both docker compsoe files from the root and from the `./copper` submodule

```shell
docker compose -f docker-compose.yaml -f copper/docker-compose.yaml up -d
```

then publish on `fetcher/fetch`

```json
[
    {
        "type":         "github",
        "repository":   "HomeSmartMesh/website",
        "ref":          "main",
        "filter":       "content/3dprinting/*",
        "resource":     "markdown-content",
        "action":       "markdown/build"
    }
]
```

on completion `markdown/build` will be triggered which will build the markdown website
