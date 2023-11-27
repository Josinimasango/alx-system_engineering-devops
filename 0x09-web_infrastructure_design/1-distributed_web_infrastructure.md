Web Server (Nginx):
- Responsible for handling incoming HTTP requests.
- Serves static content and forwards dynamic content requests to the application server.
- Improves performance through caching and load balancing.

Application Server:
- Executes the application code and processes dynamic content requests.
- Separates the application logic from the web server to enhance scalability.

Load Balancer (HAproxy):
- Distributes incoming web traffic across multiple servers to ensure high availability and even load distribution
- Configuration: Use Round Robin distribution algorithm for simplicity and equal load distribution.

Type of setup:
- This is a Active-Active setup since all the servers are serving traffic simultaneously

Difference between Active-Active setup and Active-Passive setup:
- the Active-Active setup all servers are serving traffic simultaneously whereas the Active-Passive setup only one server handles incoming traffic while others remain on standby

Application Files (Code Base):
- The set of files containing the code for the www.foobar.com application.

Database (MySQL):
- Stores and manages data for the application.

Primary-Replica Cluster: 
- Utilizes MySQL replication for data redundancy and fault tolerance.

Issues:

Single Point of Failure (SPOF):
- The load balancer can become a single point of failure. Consider adding redundancy or a failover mechanism for the load balancer.

Security Issues:
No Firewall: 
- Implement a firewall to control incoming and outgoing traffic, adding an additional layer of security.

No HTTPS: 
- Encrypt data in transit by implementing HTTPS to secure communication between clients and the web server.

No Monitoring:
- Implement monitoring tools to track server performance, detect potential issues, and ensure proactive maintenance.
