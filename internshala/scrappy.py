import requests
from bs4 import BeautifulSoup
import time

# Constants for 2Captcha API
API_KEY = "295fb37f4a9e47b1dbae06466cd2c216"
BASE_URL = "http://2captcha.com"
SOLVE_ENDPOINT = "/in.php"
RESULT_ENDPOINT = "/res.php"

def download_voter_list(district):
    url = "https://ceoelection.maharashtra.gov.in/searchlist/"

    # Step 1: Visit the website and get the initial form data
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    fom = soup.find("form", {"id": "searchList"})

    # Step 2: Prepare the form data
    data = {
        "district": district,
        "type_of_revision": "SSR 2023",
        "language_of_e_rolls": "Marathi"
    }
    for input_field in fom.find_all("input"):
        data[input_field.get("name")] = input_field.get("value")

    # Step 3: Submit the form
    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 4: Extract the captcha image and solve it
    captcha_img = soup.find("img", {"id": "captcha_image"})
    captcha_solution = solve_captcha(captcha_img["src"])

    # Step 5: Submit the form with the captcha solution
    data["captcha"] = captcha_solution
    response = requests.post(url, data=data)

    # Step 6: Download the PDF
    pdf_link = soup.find("a", text="Open PDF")
    if pdf_link:
        pdf_url = pdf_link.get("href")
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            save_pdf(pdf_response.content, district)
            print(f"Successfully downloaded voter list for district: {district}")
        else:
            print(f"Failed to download voter list for district: {district}")
    else:
        print(f"No PDF available for district: {district}")

def solve_captcha(captcha_image_url):
    # Upload captcha image to 2Captcha
    captcha_payload = {
        "key": API_KEY,
        "method": "post",
        "file": captcha_image_url
    }
    captcha_response = requests.post(f"{BASE_URL}{SOLVE_ENDPOINT}", data=captcha_payload)
    captcha_id = captcha_response.text.split("|")[1]

    # Check if captcha is solved
    while True:
        result_payload = {
            "key": API_KEY,
            "action": "get",
            "id": captcha_id
        }
        result_response = requests.get(f"{BASE_URL}{RESULT_ENDPOINT}", params=result_payload)
        if result_response.text == "CAPCHA_NOT_READY":
            # Wait for a few seconds and check again
            time.sleep(3)
        else:
            captcha_solution = result_response.text.split("|")[1]
            return captcha_solution

def save_pdf(pdf_content, district):
    filename = f"{district}_voter_list.pdf"
    with open(filename, "wb") as f:
        f.write(pdf_content)

# Test the function by providing a district name
district = input("Enter the district: ")
download_voter_list(district)
