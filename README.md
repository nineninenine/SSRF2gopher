# SSRF2gopher
Gopher protocol is used a lot when exploiting SSRF. This script generates a gopher payload what can be used to submit data to a webform.
A Server-side Request Forgery (SSRF) vulnerability occurs when an attacker manipulates a server-side application into making HTTP requests to a domain of their choice, even internal applications can be a target.

![image](https://github.com/eMVee-NL/SSRF2gopher/assets/45883753/55ce27c4-9f24-4c13-9212-3822fb7032e3)



## Usage

```
usage: SSRF2gopher.py [-h] [-u HOST] [-p PORT] [-e ENDPOINT] [-H [HEADERS ...]] [-m METHOD]

Gopher payload generator with custom headers support

options:
  -h, --help            show this help message and exit
  -u, --host HOST       Target host address
  -p, --port PORT       Gopher port number
  -e, --endpoint ENDPOINT
                        Target endpoint
  -H, --headers [HEADERS ...]
                        Custom headers in format "Name:Value"
  -m, --method METHOD   HTTP method (GET, POST, PUT, etc.)
```

Enter the following details:
- Host, example `localhost`
- Port number on target (host) for gopher, example `80`
- Endpoint (path), example `/api/user/create/`
- Data what should be submitted something like, example `username=Hacker&password=Password1234&email=email@domain.tld`
- Method (POST, GET...)
- HTTP Headers (Header:value)
