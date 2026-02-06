# **Secure File Transfer Monitoring System**

---

## **1. Introduction**

In modern organizations, file transfers pose serious security risks such as data leakage, unauthorized access, and file tampering. Sensitive data may be copied to external devices, network shares, or cloud storage without authorization.
To address these risks, this project implements a **Secure File Transfer Monitoring System** that continuously monitors file system activity, detects unauthorized file movements, verifies file integrity, and generates audit logs and alerts.

---

## **2. Objectives**

The main objectives of this project are:

1. To monitor file transfer activities such as copy, move, modify, and delete operations
2. To detect unauthorized movement of sensitive files
3. To verify file integrity using cryptographic hashing
4. To generate alerts for policy violations
5. To maintain detailed audit logs for forensic analysis

---

## **3. Practical Scope of the Project**

### **A. File Transfer Logging**

* Monitors file creation, modification, movement, and deletion events
* Logs timestamp, source path, destination path, user, and process name

### **B. Unauthorized Movement Detection**

* Maintains a list of sensitive directories
* Detects suspicious outbound transfers to USB devices and network shares
* Generates alerts for unauthorized file movements

### **C. File Integrity Checks**

* Calculates cryptographic hash values before and after file transfers
* Detects tampering, corruption, or unauthorized modification
* Highlights integrity mismatches

### **D. Reporting & Alert System**

* Generates logs for all file events
* Highlights violations and suspicious activities
* Produces an audit trail for security review

---

## **4. System Architecture**

The system consists of the following components:

* **File System Monitor** – Tracks file events in sensitive directories
* **Integrity Checker** – Computes SHA-256 hash values
* **Unauthorized Movement Detector** – Identifies suspicious destinations
* **Logging & Alert Module** – Records events and raises alerts

All components work together to ensure secure file monitoring and detection.

---

## **5. Workflow**

1. Monitor file system events
2. Identify whether the file is sensitive
3. Perform hash and authorization checks
4. Log normal activity
5. Generate alerts for violations
6. Produce audit logs

---

## **6. Tools & Technologies Used**

* **Operating System:** Windows
* **Programming Language:** Python
* **Libraries:**

  * watchdog – file system monitoring
  * psutil – user and process identification
  * hashlib – integrity hashing

---

## **7. Implementation Details**

The system monitors an **administrator-defined sensitive directory** that represents confidential or restricted data.
This directory can be configured based on organizational requirements.

A polling-based file system observer is used to ensure stable monitoring on Windows systems.
File integrity verification is performed during file transfers, and alerts are generated only for unauthorized or suspicious activities to reduce false positives.

---

## **8. How to Run the System**

### **Prerequisites**

* Windows operating system
* Python 3.x installed
* Required Python libraries

### **Installation**

Install the required dependencies:

```
pip install watchdog psutil pywin32
```

### **Setup**

1. Create a directory to represent **sensitive data**
2. Configure the sensitive directory path in the monitoring script
3. Ensure the script is executed with appropriate permissions

### **Execution**

Run the monitoring tool using:

```
python monitor_windows.py
```

Once started, the system continuously monitors file activity within the sensitive directory.

### **Stopping the System**

The monitoring process can be stopped safely using:

```
Ctrl + C
```

---

## **9. Testing & Results**

### **Test Cases**

* File creation inside the sensitive directory
* File modification detection
* Unauthorized transfer to external devices
* Integrity violation during transfer
* File deletion logging

### **Results**

* All file events were successfully logged
* Unauthorized transfers triggered alerts
* Integrity mismatches were detected accurately
* Audit logs were generated without system noise

## **9.1 File Activity Logging Test**
<img width="1863" height="214" alt="Screenshot 2026-01-04 003351" src="https://github.com/user-attachments/assets/da50458e-ad91-40bb-a828-8b0897a97b88" />

---

## **10. Deliverables**

1. Project documentation (PDF)
2. Working file transfer monitoring toolkit
3. Logs and screenshots of monitoring activity
4. Integrity check evidence
5. Flowchart and architecture diagrams
6. Final presentation (PPT)

---

## **11. Learning Outcomes**

* Understanding of file system monitoring
* Knowledge of data loss prevention techniques
* Practical experience with integrity verification
* Exposure to real-world security monitoring concepts

---

## **12. Limitations**

* Monitoring is limited to configured directories
* Cloud-synchronized folders may generate complex events
* The system focuses on detection rather than prevention

---

## **13. Future Enhancements**

* Real-time dashboard for alerts
* Automatic USB detection
* Email or SIEM integration
* Machine-learning-based anomaly detection

---

## **14. Conclusion**

The Secure File Transfer Monitoring System successfully fulfills its objectives by monitoring sensitive file activities, detecting unauthorized transfers, verifying file integrity, and generating audit logs. This project demonstrates practical security monitoring techniques used in real-world defensive security environments.


