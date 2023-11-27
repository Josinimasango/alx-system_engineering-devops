Specifics about this infrastructure:

Load Balancer:
- Distributes incoming traffic across three web servers.

Web Servers (x3):
- Hosts the www.foobar.com website.

Database Servers (MySQL x2):
- For redundancy and fault tolerance.

Firewalls (x3):
- Implements network security. 
- controlling incoming and outgoing traffic.
- Prevents unauthorized access.

HTTPS:
- encrypts data during transmission.
- ensuring confidentiality and integrity.
- protects sensitive information and building trust with users.

SSL Certificate:
- Encrypts data transmitted between users and the website.
- Ensures secure communication.

Monitoring Clients (x3):
-Collects data for monitoring and analysis.
- Ensures system health. 
- identifies performance issues. 
- aids in proactive maintenance.

How the monitoring tool is collecting data:
- Monitoring agents are installed on each server within the infrastructure. These lightweight software components collect performance metrics, logs, and other relevant data directly from the server.(Agent-Based monitoring)
- Agents gather metrics such as CPU utilization, memory usage, disk I/O, network activity. (Metrics and Perfomance counters)
- Logs contain valuable information about system events, errors, and user activity. The monitoring tool collects and aggregates logs from different components (Log Collection)
- modern applications and infrastructure components expose Application Programming Interfaces(APIs) that allow monitoring tools to retrieve specific information(API Integration)

Monitoring Web Server QPS:
- To monitor web server QPS
- set up monitoring clients to collect and analyze request metrics.

Issues:
Terminating SSL at Load Balancer:
- Terminating SSL at the load balancer exposes decrypted traffic within the internal network.
- occur at the web servers for end-to-end encryption.

Single MySQL Server for Writes:
- Having only one MySQL server accepting writes creates a single point of failure. 
- Implements a master-slave or master-master replication setup can enhance fault tolerance and availability.

Uniform Server Components:
- Using identical components for all servers may lead to systemic failures if there's a vulnerability affecting a specific component.
- Diversifying components across servers reduces the risk of widespread issues.
