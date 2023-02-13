## 0x19. Postmortem

> This repository contains the tasks for `Postmortem` project:

### Learning Objectives

* A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:
    * To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
    * And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.


### Tasks

#### Task: My first postmortem
____


## Techcreative's infrastructure outage incident report

The following is the incident report for the "Code Deployment Error" that affected Techcreative's web application (`iCreate`) that occurred on January 17, 2023.

### Issue Summary:

On January 17, 2023, from 12:30 PM to 1:45 PM (UTC+03:00), `iCreate` experienced a complete shutdown as a result of an incorrect code deployment. The application was unable to process user requests and all requests were met with 500 error response messages. At its peak, the issue affected 100% of traffic to the web application. The root cause of this outage was a code deployment error that caused a critical component of `iCreate` to crash.

### Timeline (all times UTC+03:00)
| Time (UTC+03:00) | Actions |
| -------------- | -------- |
|12:20 PM: | Code deployment begins |
|12:30 PM: | Outage begins |
|12:32 PM: | Pagers alerted teams |
|12:45 PM: | Root cause identified as code deployment error |
|1:10 PM: | Code rollback begins |
|1:30 PM: | Code rollback complete |
|1:45 PM: | 100% of traffic back online |

### Root Cause

At 12:20 PM, the code deployment team began a code deployment process to release a new version of `iCreate`. The code deployment process was automated and the code was deployed to the production environment without any human intervention. Unfortunately, a critical component of the application was not updated correctly, which caused the component to crash and bring down the entire application. The application monitoring systems quickly alerted the incident response team of the issue.

### Resolution and Recovery

At 12:32 PM, the monitoring systems alerted the incident response team who quickly investigated the issue. By 12:45 PM, the root cause was identified as a code deployment error. The team decided to perform a code rollback to restore the previous version of the application, which was known to be stable. The code rollback process began at 1:10 PM and was completed by 1:30 PM.

Some jobs started to recover slowly, and the team decided to perform a restart of the web application servers to ensure full recovery. By 1:45 PM, 100% of traffic was restored and `iCreate` was back to normal operation.

Corrective and Preventative Measures

The following are the actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
Implement a more thorough code review process before deployment to production.
Implement a code deployment process that requires human intervention before deployment to production.
Implement a better mechanism for quickly delivering status notifications during incidents.
Perform regular health checks on critical components of the web application to identify issues before they become major problems.
Ensure that the web application monitoring systems are configured to alert the incident response team as soon as any issues arise.
Develop a disaster recovery plan to quickly recover from similar incidents in the future.

Tasks:

Review and revise the deployment process.
Add automated tests to the deployment process.
Conduct regular training sessions for the deployment team.

We apologize for the impact that this outage has had on our users and customers. We are committed to improving our technology and operational processes to prevent similar incidents from happening in the future. Thank you for your patience and continued support.

Sincerely,

The `iCreate` Team



