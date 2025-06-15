import pandas as pd
import re
from collections import Counter, defaultdict

def extract_jira_ticket(text):
    if pd.isna(text):
        return None, None
    # Extract Jira ticket ID and status from hyperlink text
    match = re.search(r'([A-Z]+-\d+).*?(\w+)', str(text))
    if match:
        return match.group(1), match.group(2)
    return None, None

def analyze_jira_tickets(csv_file):
    try:
        # Read the CSV file with UTF-16 encoding
        df = pd.read_csv(csv_file, encoding='utf-16', delimiter='\t')
        
        # Create dictionaries to store mappings
        ticket_to_services = defaultdict(set)  # Jira ticket -> Set of services
        ticket_status = {}  # Jira ticket -> Status
        all_tickets = []
        
        # Process each row
        for _, row in df.iterrows():
            try:
                # Skip the header row that might be repeated in the data
                if str(row['(C) Business Service Name']).strip() == "(C) Business Service Name":
                    continue
                    
                service = str(row['(C) Business Service Name']).strip()
                jira_info = str(row['(I) Commitment Date & Jira for Adopting Environment Based Prefix Lists']).strip()
                
                if pd.notna(service) and pd.notna(jira_info) and service and jira_info:
                    ticket_id, status = extract_jira_ticket(jira_info)
                    if ticket_id and status:
                        ticket_to_services[ticket_id].add(service)
                        ticket_status[ticket_id] = status
                        all_tickets.append(ticket_id)
            except Exception as row_error:
                print(f"Warning: Skipping row due to error: {str(row_error)}")
                continue
        
        # Count unique tickets and their frequencies
        ticket_counter = Counter(all_tickets)
        unique_tickets = len(ticket_counter)
        total_tickets = len(all_tickets)
        
        # Generate report
        report = []
        report.append("📊 *Jira Tickets Status Report* 📊\n")
        report.append(f"Total Unique Jira Tickets: {unique_tickets}")
        report.append(f"Total Ticket References: {total_tickets}\n")
        
        # Detailed mapping section
        report.append("*Detailed Ticket Mapping*")
        report.append("Format: JIRA-TICKET | STATUS | SERVICES")
        report.append("-" * 50)
        
        # Sort tickets by their project key and number
        sorted_tickets = sorted(ticket_to_services.keys(), 
                              key=lambda x: (x.split('-')[0], int(x.split('-')[1])))
        
        for ticket in sorted_tickets:
            status = ticket_status[ticket]
            services = sorted(ticket_to_services[ticket])
            emoji = "✅" if status.upper() in ["DONE", "CLOSED", "RESOLVED", "COMPLETED"] else "🔄"
            services_str = ", ".join(services)
            report.append(f"{emoji} {ticket} | {status} | {services_str}")
        
        report.append("\n*Summary of Most Referenced Tickets:*")
        for ticket, count in sorted(ticket_counter.items(), key=lambda x: (-x[1], x[0]))[:5]:
            services = sorted(ticket_to_services[ticket])
            report.append(f"• {ticket} ({ticket_status[ticket]}) - Referenced {count} times")
            report.append(f"  Services: {', '.join(services)}")
        
        return "\n".join(report)
        
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {str(e)}")

if __name__ == "__main__":
    try:
        report = analyze_jira_tickets("14-06-2025.csv")
        print(report)
    except Exception as e:
        print(f"Error: {str(e)}") 