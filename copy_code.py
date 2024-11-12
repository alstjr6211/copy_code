import requests
import os

user_name = "alstjr6211"
repo_name = "basic_pro_lab"
branch_name = "navigatorBar"

api_url = f"https://api.github.com/repos/{user_name}/{repo_name}/contents/lib?ref={branch_name}"
repo_contents_url = f"https://api.github.com/repos/{user_name}/{repo_name}/contents?ref={branch_name}"
def download_file(file_url, local_path):
    try:
        file_response = requests.get(file_url)
        file_response.raise_for_status()

        directory = os.path.dirname(local_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(local_path, "w", encoding="utf-8") as file:
            file.write(file_response.text)
        print(f"'{local_path}' 파일 생성")

    except requests.exceptions.RequestException as e:
        print(f"파일 다운로드 오류: {e}")
    except OSError as e:
        print(f"파일 저장 오류: {e}")


def check_and_download_pubspec(repo_url):
    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        files = response.json()

        for file_info in files:
            if file_info['name'] == 'pubspec.yaml':
                print("'pubspec.yaml' 파일이 발견되었습니다. 생성합니다.")
                download_file(file_info['download_url'], 'pubspec.yaml')
                break
        else:
            print("'pubspec.yaml' 파일이 github에 없습니다.")

    except requests.exceptions.RequestException as e:
        print(f"'pubspec.yaml' 파일 확인 오류: {e}")


def create_folder_and_files(folder_url, local_folder):
    try:
        response = requests.get(folder_url)
        response.raise_for_status()
        files = response.json()

        for file_info in files:
            file_name = file_info['name']
            file_path = os.path.join(local_folder, file_name)

            if file_info['type'] == 'dir':
                print(f"'{file_name}'은 폴더입니다. 생성하시겠습니까? (y/n): ")
                create_folder = input()
                if create_folder.lower() == 'y':
                    if not os.path.exists(file_path):
                        os.makedirs(file_path)
                    create_folder_and_files(file_info['url'], file_path)

            elif file_info['type'] == 'file':
                print(f"'{file_name}' 파일을 생성하시겠습니까? (y/n): ")
                create_file = input()
                if create_file.lower() == 'y':
                    download_file(file_info['download_url'], file_path)

    except requests.exceptions.RequestException as e:
        print(f"폴더 내용 가져오기 오류: {e}")


check_and_download_pubspec(repo_contents_url)

create_folder_and_files(api_url, 'lib')
