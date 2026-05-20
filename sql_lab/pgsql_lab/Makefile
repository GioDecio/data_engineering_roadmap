COMPOSE := docker compose -f docker-compose.yml
PSQL := $(COMPOSE) exec -T db psql -U lab_user -d lab_db

.PHONY: start stop reset load-schema

start:
	@echo "▶ Starting Postgres container..."
	$(COMPOSE) up -d db
	@echo "▶ Waiting for Postgres to be ready..."
	@until $(COMPOSE) exec -T db pg_isready -U lab_user -d lab_db >/dev/null 2>&1; do sleep 0.5; done
	@$(MAKE) --no-print-directory load-schema
	@echo "✔ Postgres is up."

stop:
	@echo "▶ Stopping containers..."
	$(COMPOSE) down
	@echo "✔ All containers stopped."

reset:
	@echo "⚠  This will DROP the Postgres volume and ALL data in it."
	@echo "   The schema in ddl/db_schema.sql will be reloaded from scratch."
	@printf "   Are you sure? [y/N] "
	@read ans; [ "$$ans" = "y" ] || [ "$$ans" = "Y" ] || { echo "✖ Aborted."; exit 1; }
	@echo "▶ Tearing down containers and volumes..."
	$(COMPOSE) down -v
	@$(MAKE) --no-print-directory start
	@echo "✔ Postgres reset complete."

# Apply schema only if the public schema is empty (no user tables yet).
load-schema:
	@if [ "$$($(PSQL) -tAc "SELECT count(*) FROM pg_tables WHERE schemaname='public'")" = "0" ]; then \
		echo "▶ Loading schema from ddl/db_schema.sql..."; \
		$(PSQL) < ddl/db_schema.sql; \
		echo "✔ Schema loaded."; \
	else \
		echo "ℹ Schema already present, skipping load."; \
	fi
