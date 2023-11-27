- A server can be physical or virtual it is only accessed by a network and it runs an Operating System.
- DNS(Domain Name Server) is a technology that translates texted-based domain name to a numerical-domain name which is known as the IP address
- The type of DNS record www is in www.foobar.com is called the CName(Canonical Name).
- A web server is a software that delivers web pages, it handles the HTTP protocol
- An application server is an application server exposes business logic to client applications through various protocols, possibly including HTTP.
- The server communicates with the computer of the user through HTTP.

ISSUES
- The entire system relies on a single server (8.8.8.8). If it fails, the entire website becomes inaccessible.(SPOF)
- Deploying new code may require restarting the web server, causing downtime.
- using a load balancer with multiple servers can help minimize downtime during maintenance.
- The current infrastructure may struggle to handle a sudden increase in incoming traffic.  
