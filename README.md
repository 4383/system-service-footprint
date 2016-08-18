# System Footprint Scanner
Security footprint system scanner

Security scanner footprint (nmap) ~~torified~~ and dockerized
* Free software: GNU General Public License v3

# Usage
```shell
docker pull 4383/system-service-footprint:latest
```

Scan your local docker container ports

```shell
docker run 4383/system-service-footprint:latest
```

Scan any host

```shell
docker run -e 'TARGET=google.com' 4383/system-service-footprint:latest
```

## Features
* Nmap port scanning

## Credits
Author Hervé Beraud

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and 
the [docker base package](https://github.com/4383/docker-cookiepackage) project template.  
