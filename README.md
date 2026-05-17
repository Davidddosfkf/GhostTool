README.md
🔧 Network Toolkit (IP Toolkit v2.0.0)

This is a Python-based menu-driven network toolkit that includes various features for IP analysis, port scanning, and network diagnostics.

⚠️ Responsible Use: This tool is intended for educational purposes and authorized testing only. Misuse of network features may be illegal.

📌 Features

The tool includes the following features:

1. IP Lookup
Finds geographic and network information about an IP address
Data is retrieved via ip-api.com
2. (Stress test / UDP flood feature)
Sends UDP packets to a specified IP and port
Multithreaded (can use multiple threads)
Only to be used in controlled and legal testing environments
3. Ping IP
Pings an IP address via the system ping command
Supports Windows and Linux
4. Port Scanner
Scans open, closed, and filtered ports
Uses nmap
5–7. In Progress
Features in development
8. Exit
Exiting the program
📦 Requirements

Make sure to install the following dependencies:

pip install requests python-nmap

Additionally required:

Python 3.8+
Nmap installed on the system:
Windows: https://nmap.org/download.html

Linux:

sudo apt install nmap
🚀 Installation
Clone or download the project:
git clone <repo-url>
Go to the folder:
cd <project-folder>
Run the script:
python main.py
🖥️ Usage

When the program is started, a menu will appear:

01 IP Lookup
02 DDos IP and Site
03 Ping IP
04 Port Scanner
08 Exit

Select a function by entering the corresponding number.

⚠️ Disclaimer

This tool is developed for:

Education
Network analysis
Authorized security testing

You are responsible for how you use the tool. Unauthorized use against third-party systems is not permitted and may be illegal.

👨‍💻 Author

Made By JJ Joost
Version: 2.0.0
