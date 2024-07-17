
# Network Security Suite

## Overall View of Network Security Suite
The Network Security Suite is a comprehensive software solution designed to enhance network security through a combination of advanced machine learning techniques and robust firewall configurations. The suite integrates several key components, including real-time phishing URL detection, a powerful firewall implemented using iptables, a customized password manager with encryption and decryption capabilities, domain blocking using the hosts file in Linux, and an informative dashboard displaying essential network information.

### Phishing URL Detection: 
This module employs machine learning algorithms like Random Forest, Logistic Regression, and Support Vector Classifier to analyze URLs and identify phishing attempts in real-time. By leveraging these algorithms, the suite provides accurate predictions, enhancing the security of the network against malicious websites.

### Firewall Implementation: 
The suite utilizes iptables to create a robust firewall setup. It includes default policies to drop all incoming and forwarding traffic, while allowing outgoing connections. The firewall rules are configured to allow established and related connections, providing a secure environment that prevents unauthorized access.

### Password Manager: 
The password manager in the suite offers secure storage and management of passwords using custom encryption and decryption mechanisms. This ensures that users' credentials are safely stored and easily accessible when needed, reducing the risk of password-related security breaches.

### Domain Blocking: 
By modifying the hosts file in Linux, the suite enables domain blocking, preventing access to known malicious or unwanted domains. This feature helps in mitigating risks associated with browsing harmful websites and enhances overall network security.

### Dashboard: 
The dashboard provides a centralized view of critical network information, including public and private IP addresses, geographical location, ISP details, and more. This real-time information is crucial for monitoring and managing network security effectively.

### Future Enhancements: 
The suite is designed with scalability and future improvements in mind. Potential enhancements include integrating more sophisticated machine learning models, expanding the firewall rules for more granular control, and adding support for additional operating systems and network configurations.

### Work Plan: 
The development of the Network Security Suite follows a structured work plan, starting with the design and implementation of core modules, followed by rigorous testing and refinement. The project will include phases for user feedback collection, performance optimization, and documentation to ensure a seamless user experience.

### Objective: 
The primary objective of the Network Security Suite is to provide a robust, multi-faceted approach to network security, combining the strengths of machine learning and traditional security practices to protect against a wide range of threats.

### Purpose: 
The purpose of this suite is to offer a reliable and comprehensive solution for individuals and organizations seeking to enhance their network security posture. By integrating multiple security features into a single package, the suite aims to simplify security management and improve overall protection.

### Scope: 
The scope of the Network Security Suite encompasses various aspects of network security, including real-time threat detection, firewall management, secure password storage, and domain blocking. The suite is designed to be flexible and adaptable, catering to different network environments and security requirements.

### Feasibility Study: 
A detailed feasibility study has been conducted to ensure the technical, economic, and social viability of the Network Security Suite. The study confirms that the suite is practical, cost-effective, and beneficial for enhancing network security.

### Economic Feasibility: 
The suite is designed to be cost-effective, utilizing open-source technologies and minimizing the need for expensive hardware or software licenses. The potential cost savings from preventing security breaches further justify the investment in the suite.

### Technical Feasibility: 
The suite leverages widely-used technologies and frameworks, ensuring compatibility with various network configurations and operating systems. The technical design is robust, scalable, and capable of handling real-time security threats efficiently.

### Social Feasibility:
The suite addresses the growing need for comprehensive network security solutions in today's digital age. It aims to protect users' data and privacy, contributing to a safer online environment for individuals and organizations.

The Network Security Suite is a versatile and powerful tool designed to address multiple facets of network security. By combining advanced machine learning techniques with traditional security practices, it provides a comprehensive solution for protecting against a wide range of cyber threats.











## Run Locally

Clone the project

```bash
  git clone https://github.com/imkarthik-i/Network_Security_Suite.git
```

Go to the project directory

```bash
  cd Network_Security_Suite
```

Install dependencies
It required super user permission
```bash
   sudo ls
```

Start the server

```bash
  python app.py
```

## Screenshots
<img src='screenshots/Screenshot from 2024-07-18 04-27-15.png' align='center'>
<img src='screenshots/screenshots/Screenshot from 2024-07-18 04-28-53.png' align='center'>


Upon launching, the application displays a login page, ensuring that no features can be accessed without logging in. If you don't have an account, please register to create one. Your account information is securely stored to protect your data. This security measure ensures that only authorized users can access the application.
<img src='screenshots/Screenshot from 2024-07-18 04-29-14.png' align='center'>

### 1. dashboard
<img src='screenshots/Screenshot from 2024-07-18 04-29-21.png' align='center'>
The dashboard is a hub for essential host machine details, including ISP and time zone data. It displays both private and public IP addresses alongside network specifics like country. Streamlining vital network insights, it offers a comprehensive snapshot of connectivity.

### 2. domain blocking
<img src='screenshots/Screenshot from 2024-07-18 04-29-43.png' align='center'>
Domain blocking serves as a robust barrier against unwanted websites while also doubling as parental control, regulating access to approved sites.

### 3. password manager
<img src='screenshots/Screenshot from 2024-07-18 04-29-50.png' align='center'>
A password manager securely stores and organizes login credentials for various accounts. It generates complex, unique passwords to enhance security. Password managers often feature autofill capabilities for seamless login experiences. Additionally, they may offer password auditing to identify and update weak or reused passwords.

### 4. phishing url detection
<img src='screenshots/Screenshot from 2024-07-18 04-29-56.png' align='center'>
Phishing URL detection employs advanced algorithms to identify suspicious links. It analyzes URLs for signs of phishing attempts, such as irregular domain structures or known scam indicators. Real-time scanning ensures prompt detection and alerts users to potential risks. Integration with browsers or email clients enhances proactive protection against phishing threats.

### 5. firewall
<img src='screenshots/Screenshot from 2024-07-18 04-29-35.png' align='center'>
A stateful firewall monitors the state of active connections, tracking their progress from initiation to termination. It inspects incoming and outgoing packets against established session states, allowing or denying traffic based on predefined rules. This enables better security by distinguishing legitimate packets from potential threats. Stateful inspection offers enhanced protection against advanced threats like DoS attacks and packet spoofing. Additionally, it can provide logging and reporting features for network administrators to analyze traffic patterns and potential security incidents.
