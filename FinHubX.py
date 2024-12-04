import tkinter as tk
from tkinter import ttk, messagebox
from finnhub import Client
from tkinter import Scrollbar

# Initialize Finnhub API client
API_KEY = 'yourkeyhere'  # Replace with your Finnhub API key
finnhub_client = Client(api_key=API_KEY)


 

def fetch_company_profile():
    symbol = symbol_entry.get().strip().upper()
    try:
        # Use company_profile2 method from your old code
        data = finnhub_client.company_profile2(symbol=symbol)
        output_text.delete(1.0, tk.END)

        if 'name' in data:
            # Prepare data to display in a structured way
            data_to_display = [
                ["Name", data.get('name', 'N/A')],
                ["Ticker", data.get('ticker', 'N/A')],
                ["Industry", data.get('industry', 'N/A')],
                ["Country", data.get('country', 'N/A')],
                ["Exchange", data.get('exchange', 'N/A')],
                ["Market Capitalization", data.get('marketCapitalization', 'N/A')]
            ]

            # Display data in the output_text area
            for row in data_to_display:
                output_text.insert(tk.END, f"{row[0]}: {row[1]}\n")
        else:
            output_text.insert(tk.END, "No company profile data available.")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {str(e)}")

 


def fetch_sec_filings():
    symbol = symbol_entry.get().strip().upper()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    
    try:
        # Use the correct API method for fetching SEC filings
        data = finnhub_client.filings(symbol=symbol, _from=start_date, to=end_date)
        
        # Clear the output text area
        output_text.delete(1.0, tk.END)

        if data:
            # Loop through the filings and display relevant information
            for filing in data:
                output_text.insert(tk.END, f"Access Number: {filing['accessNumber']}\n")
                output_text.insert(tk.END, f"Form: {filing['form']}\n")
                output_text.insert(tk.END, f"Filed Date: {filing['filedDate']}\n")
                output_text.insert(tk.END, f"Report URL: {filing['reportUrl']}\n")
                output_text.insert(tk.END, f"Filing URL: {filing['filingUrl']}\n")
                output_text.insert(tk.END, "-" * 50 + "\n")
        else:
            output_text.insert(tk.END, "No SEC filings data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

        
        
def fetch_insider_sentiment():
    symbol = symbol_entry.get().strip().upper()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.stock_insider_sentiment(symbol, start_date, end_date)
        output_text.delete(1.0, tk.END)
        if 'data' in data:
            for entry in data['data']:
                output_text.insert(tk.END, f"Year: {entry['year']}, Month: {entry['month']}, Change: {entry['change']}, MSPR: {entry['mspr']}\n")
        else:
            output_text.insert(tk.END, "No insider sentiment data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_financials_reported():
    symbol = symbol_entry.get().strip().upper()
    try:
        data = finnhub_client.financials_reported(symbol=symbol, freq='annual')
        output_text.delete(1.0, tk.END)
        if 'data' in data:
            for report in data['data']:
                output_text.insert(tk.END, f"Year: {report['year']}, Form: {report['form']}, Start Date: {report['startDate']}, End Date: {report['endDate']}\n")
                assets = report['report']['bs'].get('Assets', 'N/A') if isinstance(report['report']['bs'], dict) else 'N/A'
                liabilities = report['report']['bs'].get('Liabilities', 'N/A') if isinstance(report['report']['bs'], dict) else 'N/A'
                output_text.insert(tk.END, f"Assets: {assets}, Liabilities: {liabilities}\n")
        else:
            output_text.insert(tk.END, "No financial reports available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_ipo_calendar():
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.ipo_calendar(_from=start_date, to=end_date)
        output_text.delete(1.0, tk.END)
        if 'ipoCalendar' in data:
            for ipo in data['ipoCalendar']:
                output_text.insert(tk.END, f"Name: {ipo['name']}, Symbol: {ipo['symbol']}, Date: {ipo['date']}, Exchange: {ipo['exchange']}, Shares: {ipo['numberOfShares']}\n")
        else:
            output_text.insert(tk.END, "No IPO data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_earnings_calendar():
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.earnings_calendar(_from=start_date, to=end_date, symbol="", international=False)
        output_text.delete(1.0, tk.END)
        if 'earningsCalendar' in data:
            for earning in data['earningsCalendar']:
                output_text.insert(tk.END, f"Symbol: {earning['symbol']}, Date: {earning['date']}, EPS Actual: {earning['epsActual']}, Revenue Actual: {earning['revenueActual']}\n")
        else:
            output_text.insert(tk.END, "No earnings data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_uspto_patents():
    symbol = symbol_entry.get().strip().upper()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.stock_uspto_patent(symbol, _from=start_date, to=end_date)
        output_text.delete(1.0, tk.END)
        if 'data' in data:
            for patent in data['data']:
                output_text.insert(tk.END, f"Patent Number: {patent['patentNumber']}, Description: {patent['description']}, Filing Date: {patent['filingDate']}, Publication Date: {patent['publicationDate']}, URL: {patent['url']}\n")
        else:
            output_text.insert(tk.END, "No USPTO patent data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

 

def fetch_usa_spending():
    symbol = symbol_entry.get().strip().upper()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.stock_usa_spending(symbol, start_date, end_date)
        output_text.delete(1.0, tk.END)
        if 'data' in data:
            for spending in data['data']:
                output_text.insert(tk.END, f"Recipient: {spending['recipientName']}, Agency: {spending['awardingAgencyName']}, Amount: {spending['totalValue']}, Date: {spending['actionDate']}, URL: {spending['permalink']}\n")
        else:
            output_text.insert(tk.END, "No USA spending data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_lobbying_data():
    symbol = symbol_entry.get().strip().upper()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    try:
        data = finnhub_client.stock_lobbying(symbol, start_date, end_date)
        output_text.delete(1.0, tk.END)
        if 'data' in data:
            for lobbying in data['data']:
                output_text.insert(tk.END, f"Name: {lobbying['name']}, Period: {lobbying['period']}, Income: {lobbying['income']}, Expenses: {lobbying['expenses']}, Document: {lobbying['documentUrl']}\n")
        else:
            output_text.insert(tk.END, "No lobbying data available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main application window
root = tk.Tk()
root.geometry("800x600")  # Adjust window size for better centralization
root.configure(bg="#1f3b6b")  # Set background color to enterprise blue

root.title("FinHubX v 7.0")
# Add the About section here (after root window creation)
about_frame = ttk.Frame(root, padding="20", relief="solid", borderwidth=2)
about_frame.grid(row=0, column=1, sticky="n", padx=10, pady=10)

about_label = ttk.Label(about_frame, text="FinHubX v 7.0\n(c) SIG LABS 2024", font=("Arial", 12), background="#f1f1f1")
about_label.grid(row=0, column=0, padx=10, pady=10)

# UI Elements
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.grid_rowconfigure(0, weight=1)  # Ensures the frame is centered vertically
root.grid_columnconfigure(0, weight=1)  # Ensures the frame is centered horizontally


symbol_label = ttk.Label(frame, text="Symbol:", font=("Arial", 12))
symbol_label.grid(row=0, column=0, sticky=tk.W)

symbol_entry = ttk.Entry(frame, width=20)
symbol_entry.grid(row=0, column=1, sticky=tk.W)

start_date_label = ttk.Label(frame, text="Start Date (YYYY-MM-DD):")
start_date_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

start_date_entry = ttk.Entry(frame, width=20)
start_date_entry.grid(row=1, column=1, sticky=tk.W)

end_date_label = ttk.Label(frame, text="End Date (YYYY-MM-DD):")
end_date_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
end_date_entry = ttk.Entry(frame, width=20)
end_date_entry.grid(row=2, column=1, sticky=tk.W)

button_style = ttk.Style()
button_style.configure("TButton", padding=6, relief="flat", background="#ffcc00")



# Styling for Buttons
button_style = ttk.Style()
button_style.configure("TButton", padding=6, relief="flat", background="#ffcc00")

# First 5 buttons in the first column (vertical)
fetch_company_profile_btn = ttk.Button(frame, text="Fetch Company Profile", style="TButton", command=fetch_company_profile)
fetch_company_profile_btn.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))

fetch_sec_filings_btn = ttk.Button(frame, text="Fetch SEC Filings", style="TButton", command=fetch_sec_filings)
fetch_sec_filings_btn.grid(row=2, column=0, pady=5, sticky=(tk.W, tk.E))

fetch_insider_btn = ttk.Button(frame, text="Fetch Insider Sentiment", style="TButton", command=fetch_insider_sentiment)
fetch_insider_btn.grid(row=3, column=0, pady=5, sticky=(tk.W, tk.E))

fetch_financials_btn = ttk.Button(frame, text="Fetch Financial Reports", style="TButton", command=fetch_financials_reported)
fetch_financials_btn.grid(row=4, column=0, pady=5, sticky=(tk.W, tk.E))

fetch_ipo_btn = ttk.Button(frame, text="Fetch IPO Calendar", style="TButton", command=fetch_ipo_calendar)
fetch_ipo_btn.grid(row=5, column=0, pady=5, sticky=(tk.W, tk.E))

# Additional buttons in the second column
fetch_earnings_btn = ttk.Button(frame, text="Fetch Earnings Calendar", style="TButton", command=fetch_earnings_calendar)
fetch_earnings_btn.grid(row=1, column=1, pady=5, sticky=(tk.W, tk.E))

fetch_uspto_btn = ttk.Button(frame, text="Fetch USPTO Patents", style="TButton", command=fetch_uspto_patents)
fetch_uspto_btn.grid(row=2, column=1, pady=5, sticky=(tk.W, tk.E))

fetch_spending_btn = ttk.Button(frame, text="Fetch USA Spending", style="TButton", command=fetch_usa_spending)
fetch_spending_btn.grid(row=3, column=1, pady=5, sticky=(tk.W, tk.E))

fetch_lobbying_btn = ttk.Button(frame, text="Fetch Lobbying Data", style="TButton", command=fetch_lobbying_data)
fetch_lobbying_btn.grid(row=4, column=1, pady=5, sticky=(tk.W, tk.E))



# Treeview for displaying data
tree = ttk.Treeview(root, columns=("Attribute", "Value"), show="headings")
tree.heading("Attribute", text="Attribute")
tree.heading("Value", text="Value")
tree.grid(row=1, column=0, padx=10, pady=10)

 


 

# Add Scrollbars for the output_text (Result window)
output_text = tk.Text(root, height=15, width=100, font=("Arial", 10), wrap="word")
output_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create the scrollbars
vsb = Scrollbar(root, orient="vertical", command=output_text.yview)
vsb.grid(row=1, column=1, sticky='ns')  # Place vertical scrollbar to the right

hsb = Scrollbar(root, orient="horizontal", command=output_text.xview)
hsb.grid(row=2, column=0, sticky='ew')  # Place horizontal scrollbar at the bottom

# Link the scrollbars to the Text widget
output_text.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set)



notebook = ttk.Notebook(root)
notebook.grid(row=1, column=0, padx=10, pady=10)

 


# Run the GUI
root.mainloop()




if __name__ == "__main__":
    main()                  