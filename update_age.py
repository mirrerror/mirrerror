import os
import datetime
import re

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def update_readme():
    dob_secret = os.getenv("MY_DOB")
    if not dob_secret:
        raise ValueError("DOB environment variable is missing!")
    
    year, month, day = map(int, dob_secret.split('-'))
    birthdate = datetime.date(year, month, day)
    
    current_age = calculate_age(birthdate)
    
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(
        r'<!--AGE-->\d+<!--/AGE-->', 
        f'<!--AGE-->{current_age}<!--/AGE-->', 
        content
    )
    
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == '__main__':
    update_readme()
