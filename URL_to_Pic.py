import time
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_profile_picture_url(url: str, u_name: str, p_word: str) -> \
        Optional[str]:
    """
    Given the url to a linkedin user's profile, return the url to their profile
    picture, if they have one. Here, <u_name> is a valid linkedin username, and
    for <p_word> is the password associated with <u_name>.

    === Preconditions ===
    - <url> must be a valid url to a user's linkedin profile.
    - <u_name> must be a valid linkedin username.
    - <p_word> must be the password associated with <u_name>.

    >>> profile = "https://www.linkedin.com/in/yazan10x/"
    >>> get_profile_picture_url(profile, 'eiqanahmed1@gmail.com', 'eiqan027')
    'https://media.licdn.com/dms/image/C4D03AQFXr80IYXm71g/profile-displayphoto-shrink_400_400/0/1649271866992?e=1683158400&v=beta&t=FaADWh3fUh_SyjWM65lJQyB3RHx2h7tkyleVDCcQ8s8'
    """
    driver = webdriver.Chrome()
    driver.get('https://linkedin.com/')
    time.sleep(5)

    username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
    password = driver.find_element(By.XPATH, '//*[@id="session_password"]')

    username.send_keys(u_name)
    password.send_keys(p_word)

    btn_xpath = '//*[@id="main-content"]/section[1]/div/form[1]/div[2]/button'
    login_btn = driver.find_element(By.XPATH, btn_xpath)
    login_btn.click()

    driver.get(url)
    time.sleep(5)

    img_path = '/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[1]/div/button/img'
    img = driver.find_element(By.XPATH, img_path)

    img_url = img.get_attribute('src')

    driver.quit()

    return img_url
