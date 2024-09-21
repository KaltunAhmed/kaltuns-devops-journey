# Networking labs

## `nslookup`

**`nslookup`** is a basic yet powerful DNS query tool used for troubleshooting networking and DNS-related issues.

### Basic Usage
To perform a DNS lookup for a domain, use the following command:

```bash
nslookup google.com
```

### Breakdown of the Response:

- **Server**: The DNS server being queried, usually your local router or DNS server.
- **Address**: The IP address of the DNS server, often shown with the DNS port number (default is port 53).

- **Non-authoritative answer**: The response is retrieved from a cache rather than directly from the authoritative DNS server for the domain.
- **Name**: The domain name that was queried (e.g., `google.com`).
- **Address**: The IP address associated with the domain name (e.g., `google.com`).



## `dig`

**`dig`** (Domain Information Groper) is a command-line tool used for querying DNS name servers. It's more detailed than `nslookup` and is commonly used for DNS troubleshooting.

### Basic Usage
To perform a DNS lookup for a domain, use the following command:

```bash
dig google.com
```

### Breakdown of the Response:

- **Question Section**: Displays the query that was sent to the DNS server, including the domain name and record type (e.g., A, MX).
  
- **Answer Section**: Contains the DNS response, such as the IP address or other records (e.g., CNAME, NS) associated with the domain.

- **Authority Section**: Lists the authoritative name servers for the domain.

- **Additional Section**: Provides extra information, such as IP addresses for the name servers.

### Key Terms:

- **ANSWER**: The number of records returned in the answer section.
- **Query Time**: The time it took for the query to complete, measured in milliseconds.
- **TTL (Time-to-Live)**: The duration in seconds that the DNS record will be cached before needing to be refreshed.
- **Non-authoritative answer**: Indicates that the answer came from a cache, not directly from the authoritative name server.
- **Authoritative answer**: The response is directly from the authoritative DNS server for the domain.


## `dig +short`

This command returns a shorter version of the DNS query response, showing only the essential information, such as the IP address.

```bash
dig +short google.com
```


## `dig +short ns`

This command returns the name servers for the specified domain, providing a concise output.

```bash
dig +short ns google.com
```