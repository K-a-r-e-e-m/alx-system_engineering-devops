# What happens when you type google.com in your browser and press Enter

When you type google.com in your browser and press Enter, a series of events occur to load the webpage. This process involves multiple layers of the web stack, each playing a crucial role in delivering the final content to your browser. Let's break down these steps:
## 1. URL Check
When you type google.com in your browser, the browser first checks if the input is a URL or a search query. If there is no protocol defined or the domain name is invalid, it will perform a search. Otherwise, it will go to your destination (google.com).
## 2. DNS Request
Your browser needs to know the address of Google's server to respond with the site resources. This essential step is called DNS (Domain Name System) lookup. You enter a friendly user domain name (e.g., google.com), but the server understands computer-friendly IP addresses (e.g., 192.168.1.1). Here's how the process of converting a domain name to an IP address works:
Browser Cache: The browser first checks its local cache for the IP address of google.com.
OS Cache: If not found, it checks the operating system's DNS cache.
Router Cache: If still not found, the query is sent to the router, which has its own DNS cache.
ISP DNS Server: The request is then sent to the Internet Service Provider's (ISP) DNS server.
Recursive Search: If the ISP's DNS server doesn't have the IP address, it performs a recursive search through various DNS servers until it finds the IP address.
The DNS servers return the IP address associated with google.com.
## 3. TCP/IP
To establish a connection between your computer's browser and Google's server, the Transmission Control Protocol/Internet Protocol (TCP/IP) is used. TCP works with IP to transport data packets and connect computers, applications, and web servers. Before data is delivered, a connection is established using a three-way handshake:
SYN: The browser sends a SYN (synchronize) packet to Google's server to start the connection.
SYN-ACK: Google's server responds with a SYN-ACK (synchronize-acknowledge) packet.
ACK: The browser sends an ACK (acknowledge) packet to establish and confirm the connection.
## 4. Firewall
A firewall is a network security device (software or hardware) that monitors and controls incoming and outgoing network traffic based on predefined security rules. Firewalls ensure that data packets are secure. There are firewalls on the client side, intermediate traffic at routers and ISPs, and the server side to inspect incoming data.
## 5. HTTPS/SSL
SSL (Secure Socket Layer) is a certificate used to establish an encrypted connection between the browser and server. HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP, indicating that the site has an SSL/TLS certificate. This protocol encrypts communication using asymmetric public key infrastructure, which involves:
Private Key: A key that exists only with the owner of the website and is used to decrypt information encrypted by the public key.
Public Key: A key available to anyone who wants to interact with the server.
This system ensures secure communication, making it unreadable by hackers who might sniff the connection.
## 6. Load Balancer
Once the connection is established, the request often passes through a load balancer, which acts like a proxy. A load balancer distributes network traffic load between multiple servers to ensure reliability and performance. It also performs health checks to direct traffic only to healthy servers.
## 7. Web Server
The request then reaches Google's web server, which hosts the website's code and data. When you enter a URL, it acts as the address identifier of the web server. The browser sends an HTTP request to the server, which then communicates with a database server to return the relevant data. The web server returns the static content of the website (HTML pages, CSS, images).
## 8. Application Server
If the request requires dynamic content or backend processing, it is forwarded to an application server. The application server applies business logic and communicates with other servers to fulfill the request, renders a new HTML page, and returns it as a response to the web server.
## 9. Database
For requests that need data storage or retrieval, the application server interacts with a database. It sends queries to the database to retrieve or store data, and the database processes these queries and returns the results to the application server.
## 10. Response to Client
Finally, the application server sends the processed data back to the web server, which forwards it to the load balancer. The load balancer routes the response back to the client's browser through the established secure connection.
Rendering the Page
HTML Parsing: The browser parses the HTML document.
Resource Requests: The browser makes additional requests for CSS, JavaScript, images, etc.
DOM Construction: The Document Object Model (DOM) is constructed.
CSSOM Construction: The CSS Object Model (CSSOM) is constructed.
Render Tree: The browser combines the DOM and CSSOM into a render tree.
Layout and Paint: The render tree is laid out in the viewport, and the page is painted on the screen.
Conclusion
This entire process happens in a fraction of a second, seamlessly delivering the requested webpage to your browser.
