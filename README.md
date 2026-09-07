# homelab repo
fooling around with homelab stuff

## homelab/pihole/
module for pihole stuff. use env.example to as an example to build your own pihole.
from module root (/homelab-001/pihole), first:
- write your `pihole/.env` file using `pihole/env.example`
- check that Docker Compose sees your configuration
```docker compose config```
- If it doesn't, ... Check your docker version.
- Start pihole with
```docker compose up -d```
- check with `docker compose ps` 
- finally, check dashboard at http://<VM-IP>:8080/admin

to setup adblocking on your home network:
- go to http://192.168.0.1
- go to your DHCP settings (or whatever they're called for you)
- set primary DNS as your VM IP (`ip a` in terminal)
- secondary DNS should either be your primary DNS again, or 0.0.0.0
- should be good
