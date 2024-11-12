import requests
import os

#github links

url_html = "https://raw.githubusercontent.com/alstjr6211/calendar_project/mail/mail.html"
url_js = "https://raw.githubusercontent.com/alstjr6211/calendar_project/mail/script.js"
url_css = "https://raw.githubusercontent.com/alstjr6211/calendar_project/mail/style.css"

#github link에서 가져온 코드를 사용할 files name

file_name_html = "new.html"
file_name_js = "new.js"
file_name_css = "new.css"


#html

try:
    if os.path.exists(file_name_html):
        overwrite = input(f"'{file_name_html}' file이 존재합니다. 덮어쓰시겠습니까? (y/n): ")
        if overwrite.lower() != 'y':
            print("종료합니다.")
            exit()

    response = requests.get(url_html)
    response.raise_for_status()

    with open(file_name_html, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"'{file_name_html}' 파일이 성공적으로 생성되었습니다.")

except requests.exceptions.RequestException as e:
    print("RequestsException 발생:", e)
except Exception as e:
    print("Exception 발생:", e)

#js

try:
    if os.path.exists(file_name_js):
        overwrite = input(f"'{file_name_js}' file이 존재합니다. 덮어쓰시겠습니까? (y/n): ")
        if overwrite.lower() != 'y':
            print("종료합니다.")
            exit()

    response = requests.get(url_js)
    response.raise_for_status()

    with open(file_name_js, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"'{file_name_js}' 파일이 성공적으로 생성되었습니다.")

except requests.exceptions.RequestException as e:
    print("RequestsException 발생:", e)
except Exception as e:
    print("Exception 발생:", e)

# css
try:
    if os.path.exists(file_name_css):
        overwrite = input(f"'{file_name_css}' file이 존재합니다. 덮어쓰시겠습니까? (y/n): ")
        if overwrite.lower() != 'y':
            print("종료합니다.")
            exit()

    response = requests.get(url_css)
    response.raise_for_status()

    with open(file_name_css, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"'{file_name_css}' 파일이 성공적으로 생성되었습니다.")

except requests.exceptions.RequestException as e:
    print("RequestsException 발생:", e)
except Exception as e:
    print("Exception 발생:", e)
