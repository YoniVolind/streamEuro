from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.uefa.com/euro2024/fixtures-results/#/d/2024-06-14")
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-tab-id='2024-06-14']>div>div")))
g="'"
a=f"[data-tab-id={g}2024-03-26{g}]>div>div>a"

x=driver.page_source

with open('content.txt','w',encoding="utf-8") as file:
    file.write(x)

# Define the string to search for
search_string = "eventAttendanceMode"

# Define the file path
file_path = 'content.txt'

all_strings=[]
try:
    with open(file_path, "r",encoding="utf-8") as file:
        file_contents = file.read()
        search_index = 0

        # Find all occurrences of the search string within the file contents
        while True:
            # Find the next occurrence of the search string
            index = file_contents.find(search_string, search_index)

            if index == -1:
                break  # No more occurrences found

            # Get the text before the search string, up to 50 characters
            start_index = max(0, index - 50)  # Ensure not to start before the beginning of the file
            result = file_contents[start_index:index]
            all_strings.append(result)

            # Move the search index to the next position
            search_index = index + len(search_string) + 1
except FileNotFoundError:
    pass


final_strings=[]

for i in all_strings:
    print(i)
    index = i.find('name')

    if index != -1:  # If the substring is found
        # Find the index of the next double quote '"' after the substring '"name":'
        start_index = index + 7

        if start_index != -1:  # If the double quote is found
            result = i[start_index :-3]
            final_strings.append(result)

for i in final_strings:
    print(i)





# for i in range(1,7):
#     a=f"[data-tab-id={g}2024-03-2{i}{g}]>div>div>a"
#     try:
#         team_element = driver.find_elements(By.CSS_SELECTOR, a)
#         for e in team_element:
#             # print(e)
#             print(e.get_attribute('title'))
#     except:
#         pass



print('Done')
