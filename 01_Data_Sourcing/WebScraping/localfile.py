from bs4 import BeautifulSoup

# Accessing a file
with open('C:\\Users\\DELL\\PycharmProjects\\WebDevelopment\\index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # Find the 'h3' tag with the text 'Academic Education'
    academic_education = soup.find('h3', string='Academic Education')

    # Find the nearest 'table' tag after the 'h3' tag
    table = academic_education.find_next('table')

    # Find all 'tr' tags within the 'tbody' tag of the table
    rows = table.select('tbody tr')

    for row in rows:
        # Extract the required data from the row
        cells = row.find_all('td')
        institution_name = cells[3].string.strip()
        cgpa = cells[4].string.strip()

        # Print the extracted information
        print("Institution Name:", institution_name, "   |CGPA:", cgpa)