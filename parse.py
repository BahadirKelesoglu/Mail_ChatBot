import pyodbc
import requests
from bs4 import BeautifulSoup

# Establish a connection to the SQL Server database
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=xx;"
    "Database=xx;"
    "UID=xxx;"
    "PWD=xxx;"
)

# Create a cursor to interact with the database
cursor = conn.cursor()

url = "https://www.miuul.com/katalog?arama=&tur=tumu&sure="
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

courses = soup.find_all("div", class_="card catalog border-0 shadow rounded-3 h-100 d-none d-md-block")  # Example selector, adjust according to your needs

# Iterate over the found elements and extract the desired information
for course in courses:
    title_element = course.find("h6", class_="fs-19 ff-medium")
    description_element = course.find("p", class_="mb-0 ff-regular fs-13")
    information_elements = course.find_all("div", class_="col-auto p-3")
    skill_elements = course.find_all("span", class_="d-inline-block fs-11 ff-regular text-secondary mb-1 border rounded p-1 px-3 text-nowrap")
    title = title_element.text
    description = description_element.text    
    print("Title:", title)
    print("Description:", description)
    
    if title_element is not None and information_elements:
        
        informations = [information.text for information in information_elements]
        
        for information in informations:
            print("Information:", information)
        print("---")
    else:
        print("")
    
    if title_element is not None and skill_elements:
        
        skills = [skill.text for skill in skill_elements]
        
        for skill in skills:
            print("Skill:", skill)
        print("---")
    else:
        print("None")
        skills="None"
        
        
    # Construct the SQL insert statement
    sql = "INSERT INTO miuul_Courses (Title, Description, Information, Skills) VALUES (?, ?, ?, ?)"

    
    # Execute the insert statement with the data values
    cursor.execute(sql, (title, description, '\n'.join(informations), '\n'.join(skills)))
    
# Commit the changes and close the cursor and connection
cursor.commit()
cursor.close()
conn.close()
