import re
import csv

def task_number_3():
    with open("task3.txt", "r") as f:
        text = f.read()

    pattern_id = r'(?<!\S)[1-9]\d*(?!\S)'
    pattern_name = r'\b[A-Z][a-z]+\b'
    pattern_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    pattern_date = r'\b\d{4}-\d{2}-\d{2}\b'
    pattern_website = r'\bhttps?://[^\s<>"]+\b'
    text_users = re.findall(r'\S+(?:\s+\S+){4}', text)
    with open("task3_result.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(["ID", "name", "mail", "date", "website"])
    
        for user in text_users:
            id_users = re.findall(pattern_id, user)
            name = re.findall(pattern_name, user)
            mail = re.findall(pattern_mail, user)
            date = re.findall(pattern_date, user)
            website = re.findall(pattern_website, user)
            
            writer.writerow([id_users[0], name[0], mail[0], date[0], website[0]])
if __name__ == '__main__':
    task_number_3()