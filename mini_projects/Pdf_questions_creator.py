from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Technology Products & Enterprise ICT Solutions - MCQs", ln=True, align="C")
        self.ln(10)

# Creating a PDF document
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

questions = [
    # Easy (10 Questions)
    ("What does ICT stand for?", ["A) Internet Communication Technology", "B) Information and Communication Technology", 
                                  "C) International Computer Technology", "D) Integrated Cloud Technology"], "B"),
    ("Which of the following is a cloud computing service model?", ["A) SaaS", "B) HTTP", "C) FTP", "D) SMTP"], "A"),
    ("Which storage type is commonly used in enterprise storage solutions?", ["A) SSD", "B) HDD", "C) Tape Drives", "D) All of the above"], "D"),
    ("What is an example of an enterprise collaboration tool?", ["A) Microsoft Teams", "B) VLC Media Player", "C) Adobe Photoshop", "D) WinRAR"], "A"),
    ("Which protocol is used for secure web communication?", ["A) HTTP", "B) FTP", "C) HTTPS", "D) SMTP"], "C"),
    ("Which of the following is NOT an operating system?", ["A) Windows", "B) Linux", "C) Cisco", "D) macOS"], "C"),
    ("Which company is a leading provider of cloud computing services?", ["A) Google", "B) Amazon", "C) Microsoft", "D) All of the above"], "D"),
    ("What is the purpose of a firewall in network security?", ["A) Speed up the internet", "B) Block unauthorized access", 
                                                                 "C) Manage software updates", "D) Compress files"], "B"),
    ("Which of the following is an example of an ERP system?", ["A) SAP", "B) Twitter", "C) VLC", "D) Notepad"], "A"),
    ("Which technology is used for virtualization?", ["A) Docker", "B) Hyper-V", "C) VMware", "D) All of the above"], "D"),

    # Medium to Advanced (20 Questions)
    ("What is the primary function of a load balancer?", ["A) Secure the network", "B) Distribute incoming traffic", "C) Store data", "D) Encrypt communications"], "B"),
    ("Which of the following is a relational database management system?", ["A) MySQL", "B) MongoDB", "C) Redis", "D) Cassandra"], "A"),
    ("What is the full form of VPN?", ["A) Virtual Public Network", "B) Virtual Private Network", "C) Verified Protocol Network", "D) Very Private Network"], "B"),
    ("Which of the following is an open-source cloud platform?", ["A) AWS", "B) Google Cloud", "C) OpenStack", "D) Azure"], "C"),
    ("What is the purpose of SDN (Software-Defined Networking)?", ["A) Manage network hardware", "B) Decouple control from forwarding", 
                                                                   "C) Improve network latency", "D) Secure endpoints"], "B"),
    ("What does IaaS stand for?", ["A) Internet as a Service", "B) Infrastructure as a Service", "C) Integration as a Service", "D) Information as a Service"], "B"),
    ("Which security model is commonly used for enterprise access control?", ["A) Zero Trust", "B) Ring Topology", "C) Star Network", "D) IPv6"], "A"),
    ("What does SLA stand for in cloud computing?", ["A) Service Level Agreement", "B) Secure LAN Access", "C) Systematic Load Analysis", "D) Software Licensing Agreement"], "A"),
    ("Which of these is an example of a hybrid cloud deployment?", ["A) Google Drive", "B) Microsoft Azure", "C) Combination of public and private cloud", "D) AWS S3"], "C"),
    ("Which tool is commonly used for IT service management?", ["A) Jira", "B) ServiceNow", "C) AWS Lambda", "D) Jenkins"], "B"),

    # Hard (20 Questions)
    ("What is the main function of an Enterprise Service Bus (ESB)?", ["A) Manage network traffic", "B) Enable communication between different applications", "C) Store enterprise data", "D) Encrypt network packets"], "B"),
    ("Which technology underpins blockchain?", ["A) Distributed Ledger", "B) Centralized Database", "C) Peer-to-Peer FTP", "D) SaaS"], "A"),
    ("Which networking technology reduces reliance on hardware appliances?", ["A) SD-WAN", "B) VPN", "C) MPLS", "D) DNS"], "A"),
    ("What is the main advantage of Kubernetes in enterprise solutions?", ["A) Load balancing", "B) Automated container orchestration", "C) Increased RAM speed", "D) Antivirus protection"], "B"),
    ("Which of the following is a key benefit of microservices architecture?", ["A) Single point of failure", "B) Easier scalability", "C) Monolithic approach", "D) Decreased cloud performance"], "B"),
]

# Adding questions to the PDF
for i, (question, options, answer) in enumerate(questions, 1):
    pdf.multi_cell(0, 7, f"Q{i}: {question}")
    for option in options:
        pdf.cell(0, 7, option, ln=True)
    pdf.cell(0, 7, f"Answer: {answer}", ln=True)
    pdf.ln(5)

# Saving the file
pdf_filename = "/mnt/data/Technology_ICT_MCQs_Final_Complete.pdf"
pdf.output(pdf_filename)

pdf_filename
