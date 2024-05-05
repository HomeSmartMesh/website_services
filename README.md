# website_services
Copper pipeline for markdown website building

# Usage

run both docker compsoe files from the root and from the `./copper` submodule

```shell
cd copper
docker compose up -d
cd ..
cd markdown
docker compose up -d
```

the root `workflow.yaml` will be executed by the runner that pulishes each action topics and subscribes to wait for the action to finish

```yaml
- action: fetcher/fetch
  type: github
  repository: MicroWebStacks/astro-big-doc
  ref: main
  filter: content/*
  resource: test-website
- action: markdown/build
  resource: test-website
  path: /fetch/test-website/content
```
