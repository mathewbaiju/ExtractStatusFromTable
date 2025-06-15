# Extract Status From Table

A Python-based tool to analyze Jira tickets from CSV files and generate Slack-friendly status reports.

## Tech Stack
- Python 3.x
- pandas: Data manipulation and analysis
- re: Regular expression operations
- collections: Specialized container datatypes

## Features
1. **CSV Processing**: Handles UTF-16 encoded CSV files with complex data structures
2. **Jira Ticket Analysis**: 
   - Extracts Jira ticket IDs and their statuses
   - Groups tickets by service name
   - Tracks ticket status across different services
3. **Slack-Friendly Output**:
   - Uses emojis for better visualization (✅, 🔄, 🚫, ⏸️)
   - Proper formatting with bold text and sections
   - Easy to copy-paste into Slack

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ExtractStatusFromTable.git
cd ExtractStatusFromTable
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your CSV file in the project directory
2. Run the script:
```bash
python3 analyze_jira_tickets.py
```

The script will:
- Read the CSV file
- Extract Jira ticket information
- Generate a formatted report
- Save the report to `jira_status_report.txt`

## Benefits

1. **Time Saving**: 
   - Automatically processes large CSV files
   - Generates ready-to-use Slack reports
   - Eliminates manual ticket status tracking

2. **Better Visibility**:
   - Clear status categorization (To Do, In Progress, Done, etc.)
   - Service-wise grouping of tickets
   - Visual indicators for different statuses

3. **Error Prevention**:
   - Handles various CSV encodings
   - Validates data before processing
   - Maintains data integrity

4. **Easy Maintenance**:
   - Simple Python codebase
   - Modular design
   - Easy to extend functionality

## Input Format

The CSV file should contain the following columns:
- Service Name
- Jira Ticket information
- Status information

## Output Format

The generated report includes:
1. Overall status distribution
2. Tickets grouped by status:
   - To Do/Open
   - In Progress
   - Done/Closed
   - Resolved/Ready
   - Blocked
   - On Hold

Each ticket entry includes:
- Jira ticket ID
- Description
- Current status with emoji indicator
