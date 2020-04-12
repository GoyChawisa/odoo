# Odoo training with TR

Just sample on training sections.

### Required
- Docker
- Docker-compose

### Running

```bash
$docker-compose up
```

### Updated source code

```bash
$docker-compose down
$docker-compose exec odoo odoo --no-xmlrpc -i openacademy -d master --db_host db -r odoo -w odoo --stop-after-init
```
