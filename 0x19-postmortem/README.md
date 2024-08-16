# Postmortem: Website Outage on 24/7/2024
***
Date: 24/7/2024

Author: Kareem Hany, Web Operations Team

Summary: A 50-minute outage caused by a firewall misconfiguration, impacting 100% of users.


***
![Postmortem](postmortem.png)
### Issue Summary
Between 15:30 and 16:20 on 24/7/2024 (UTC), our website experienced a 50-minute outage. Users were unable to access the site, resulting in a 100% service disruption. The root cause was a misconfiguration in the firewall, which blocked essential traffic to the web server.

### Timeline
15:30 - A new update was pushed to the website, enhancing security by modifying firewall settings.
15:32 - On-call monitoring systems triggered an alert.
15:35 - Users began reporting via email that the website was inaccessible.
15:40 - The on-call engineer attempted to access the website and found it down.
15:45 - The engineer reviewed log files, suspecting the new update as the cause.
16:00 - The engineer tried restarting the firewall, but the issue persisted.
16:15 - After multiple unsuccessful troubleshooting attempts, the decision was made to roll back the update.
16:20 - The rollback was completed, and the website was restored to normal operation.
### Root Cause and Resolution
The issue was caused by a misconfiguration in the firewall settings during the latest update. Specifically, the firewall was mistakenly set to listen on port 442 instead of the standard HTTPS port 443. This error was likely introduced when a developer was adding new port settings but inadvertently altered the HTTPS port.

To resolve the issue, the team initially attempted to restart the firewall, but this did not fix the problem. After further investigation and realizing that the update was the likely cause, the team decided to roll back to the previous configuration. This action immediately restored the website. A subsequent review of the firewall settings identified the incorrect port configuration, which was then corrected before redeploying the update.

### Corrective and Preventative Measures
To prevent similar issues in the future:

Improve pre-deployment reviews: All firewall and web server configurations will undergo a thorough review by the security team before deployment.
Implement automated testing: Develop and deploy automated tests to check firewall configurations and ensure correct port settings.
Enhance monitoring alerts: Adjust monitoring systems to detect and alert on incorrect port configurations specifically.
Training for developers: Provide additional training to developers on the critical importance of correct configuration, especially for security settings.

