import os

def create_simple_pdf(filepath, title, lines):
    # Minimal standard conforming PDF 1.4
    content_stream = "BT /F1 14 Tf 50 750 Td (" + title + ") Tj ET\n"
    y = 720
    for line in lines:
        safe_line = line.replace("(", "[").replace(")", "]")
        content_stream += f"BT /F1 10 Tf 50 {y} Td ({safe_line}) Tj ET\n"
        y -= 25

    stream_len = len(content_stream.encode('latin1'))
    
    pdf_content = (
        "%PDF-1.4\n"
        "1 0 obj\n"
        "<< /Type /Catalog /Pages 2 0 R >>\n"
        "endobj\n"
        "2 0 obj\n"
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n"
        "endobj\n"
        "3 0 obj\n"
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\n"
        "endobj\n"
        "4 0 obj\n"
        f"<< /Length {stream_len} >>\n"
        "stream\n"
        f"{content_stream}"
        "endstream\n"
        "endobj\n"
        "5 0 obj\n"
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\n"
        "endobj\n"
        "xref\n"
        "0 6\n"
        "0000000000 65535 f \n"
        "0000000009 00000 n \n"
        "0000000058 00000 n \n"
        "0000000115 00000 n \n"
        "0000000244 00000 n \n"
        f"0000000{300 + stream_len:03d} 00000 n \n"
        "trailer\n"
        "<< /Size 6 /Root 1 0 R >>\n"
        "startxref\n"
        f"{380 + stream_len}\n"
        "%%EOF\n"
    )

    with open(filepath, 'wb') as f:
        f.write(pdf_content.encode('latin1'))
    print(f"Generated: {filepath}")

os.makedirs('sample_docs', exist_ok=True)

create_simple_pdf(
    'sample_docs/Aadhaar_Card_Sample.pdf',
    'GOVERNMENT OF INDIA - UNIQUE IDENTIFICATION AUTHORITY',
    [
        'Government of India - Unique Identification Authority of India',
        'Mera Aadhaar, Meri Pehchan',
        'Aadhaar Number: 5412 8921 4410',
        'Name: Rahul Sharma',
        'DOB: 15/06/1994',
        'Gender: Male',
        'Address: Flat 402, Skyline Towers, Sector 62, Noida, UP - 201309',
        'UIDAI Toll Free Helpdesk: 1947 | help@uidai.gov.in'
    ]
)

create_simple_pdf(
    'sample_docs/PAN_Card_Sample.pdf',
    'INCOME TAX DEPARTMENT - GOVT. OF INDIA',
    [
        'INCOME TAX DEPARTMENT - GOVT. OF INDIA',
        'Permanent Account Number Card',
        'PAN: ABCDE1234F',
        'Name: RAHUL SHARMA',
        'Father Name: SURESH SHARMA',
        'Date of Birth: 15/06/1994',
        'Signature verified digitally under section 139A of IT Act'
    ]
)

create_simple_pdf(
    'sample_docs/Salary_Slip_Sample.pdf',
    'INFOSYS TECHNOLOGIES LIMITED - SALARY SLIP',
    [
        'Company: Infosys Technologies Limited',
        'Pay Slip for the Month of August 2026',
        'Employee Code: INF98421 | Designation: Senior Software Engineer',
        'Basic Pay: INR 45,000.00 | HRA: INR 20,000.00 | Special Allowance: INR 25,400.00',
        'Gross Earnings: INR 90,400.00',
        'Deductions: Provident Fund EPF INR 5,400.00 | Professional Tax: INR 200.00',
        'Net Take Home Salary: INR 85,000.00'
    ]
)

create_simple_pdf(
    'sample_docs/Bank_Statement_Sample.pdf',
    'HDFC BANK LIMITED - ACCOUNT STATEMENT',
    [
        'HDFC Bank Limited - Branch Sector 62 Noida',
        'Account Statement for Period 01-08-2026 to 31-08-2026',
        'Account Number: 918020045812901 | IFSC Code: HDFC0001024',
        'Account Holder: Rahul Sharma',
        'Opening Balance: INR 52,400.00 | Total Credit: INR 85,000.00 (Salary Infosys)',
        'Total Debit: INR 25,400.00 | Closing Balance: INR 112,000.00'
    ]
)

create_simple_pdf(
    'sample_docs/Electricity_Bill_Address_Proof.pdf',
    'NOIDA POWER COMPANY LIMITED - ELECTRICITY BILL',
    [
        'Utility Bill / Address Proof Document',
        'Consumer Number: 9928120041 | Bill Date: 05-09-2026',
        'Consumer Name: Rahul Sharma',
        'Billing Residential Address: Flat 402, Skyline Towers, Sector 62, Noida - 201309',
        'Meter Reading Units: 340 kWh | Total Bill Amount: INR 2,450.00'
    ]
)

create_simple_pdf(
    'sample_docs/Wrong_Document_Recipe.pdf',
    'CHOCOLATE CAKE BAKING RECIPE',
    [
        'Ingredients:',
        '2 cups all-purpose flour',
        '2 cups granulated sugar',
        '3/4 cup unsweetened cocoa powder',
        '2 teaspoons baking powder',
        'Bake at 350 degrees Fahrenheit for 30 minutes.'
    ]
)

print("All sample test documents generated successfully!")
