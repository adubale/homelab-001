# homelab-001
fooling around with homelab stuff

## homelab-001/pihole/
module for pihole stuff. use .env.example to as an example to build your own pihole.
from module root (/homelab-001/pihole), first:
- check that Docker Compose sees your configuration
```docker compose config```
- If it doesn't, ... Check your docker version.
- Start pihole with
```docker compose up -d```
- check with `docker compose ps` 
- finally, check dashboard at http://<VM-IP>:8080/admin
