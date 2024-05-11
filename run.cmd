mkdir cache\data\typesense
set WORKFLOW=../workflow.yaml
docker compose -f copper/docker-compose.yaml -f markdown/docker-compose.yaml up -d
