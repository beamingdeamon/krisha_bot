from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()

browser.get('https://id.kolesa.kz/login/?destination=https%3A%2F%2Fkrisha.kz%2Fmy')

type = "sell flat"
# type = "sell house"
# type = "sell dacha"
# type = "sell office"
# type = "sell premises"
# type = "sell building"
# type = "sell shop"
# type = "sell industrial"
# type = "sell land"
# type = "sell estate"


login = browser.find_element(By.NAME, 'login')  # Find the search box
login.send_keys('77075586854' + Keys.RETURN)

password = browser.find_element(By.NAME, 'password')  # Find the search box
password.send_keys('Salam2019' + Keys.RETURN)

browser.get('https://krisha.kz/my')
time.sleep(2)
if(type == "sell flat"):
    room_count = 2
    price = 1000
    is_zalog = False
    house_year = 2000
    # flat_type = "kirpich"
    # flat_type = "panel"
    flat_type = "monolit"
    # flat_type = "another"
    flat_floor = 2
    house_floors = 7
    total_S = 110
    live_S = 80
    kitchen_S = 12
    is_obshaga = True


    flat_status = "good"
    # flat_status = "middle"
    # flat_status = "need_remont"
    # flat_status = "free_plan"
    # flat_status = "black"


    phone = "separate"
    # phone = "block"
    # phone = "can_add"
    # phone = "no"


    internet = "ADSL"
    # internet = "TV"
    # internet = "cabel"
    # internet = "optic"


    toilet = "separate"
    # toilet = "combined"
    # toilet = "2 more"
    # toilet = "no"


    balcony = "balcony"
    # balcony = "loggia"
    # balcony = "balcony and loggia"
    # balcony = "some"

    balcony_window = "yes"
    # balcony_window = "no"

    door_type = "wood"
    # door_type = "metal"
    # door_type = "armed"

    parking = "parking"
    # parking = "garage"
    # parking = "security"

    furniture = "all"
    # furniture = "mixed"
    # furniture = "no"

    floor = "linoleum"
    # floor = "parket"
    # floor = "laminat"
    # floor = "wood"
    # floor = "cavrolan"
    # floor = "tile"
    # floor = "cork"

    roof_height = 3

        #Security
    is_reshetki = True
    is_security = True
    is_domophone = True
    is_zamok = True
    is_signal = True
    is_camera = True
    is_videodomophone = True
    is_konsier = True


        #Another
    is_plastic_windows = True
    is_angle = True
    is_upgraded = True
    is_isolated = True
    is_kitchen_studio = True
    is_kitchen_in = True
    is_new_plumbing = True
    is_storage = True
    is_counters = True
    is_quiet = True
    is_conditioner = True
    is_commerce = True


    city = "Алматы"
    # district = "Алатауский р-н"
    # microdistrict = "мкр Айгерим-2"
    street = "Байзакова"
    house_number = "316"
    second_street = ""
    text="test text"
    company_name = "HUILA"
    mail = "test@test"

    browser.get('https://krisha.kz/a/new/?cat=sell.flat')

    room_count_input = browser.find_element(By.NAME, 'live_rooms')
    room_count_input.send_keys(room_count)

    price_input = browser.find_element(By.NAME, 'price')
    price_input.send_keys(price)


    if(is_zalog):
        zalog_select = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[3]/div/div/div/div/div[1]/span')
        zalog_select.click()


    if(flat_type == "kirpich"):
        flat_type_span = Select(browser.find_element(By.NAME, 'flat_building'))
        flat_type_span.select_by_value('1')
    elif(flat_type == "panel"):
        flat_type_span = Select(browser.find_element(By.NAME, 'flat_building'))
        flat_type_span.select_by_value('2')
    elif(flat_type == "monolit"):
        flat_type_span = Select(browser.find_element(By.NAME, 'flat_building'))
        flat_type_span.select_by_value('3')
    elif(flat_type == "another"):
        flat_type_span = Select(browser.find_element(By.NAME, 'flat_building'))
        flat_type_span.select_by_value('0')

    house_year_input = browser.find_element(By.NAME, 'house_year')
    house_year_input.send_keys(house_year)

    flat_floor_input = browser.find_element(By.NAME, 'flat_floor')
    flat_floor_input.send_keys(flat_floor)

    house_floors_input = browser.find_element(By.NAME, 'house_floor_num')
    house_floors_input.send_keys(house_floors)

    total_S_input = browser.find_element(By.NAME, 'live_square')
    total_S_input.send_keys(total_S)

    live_S_input = browser.find_element(By.NAME, 'live_square_l')
    live_S_input.send_keys(live_S)

    kitchen_S_input = browser.find_element(By.NAME, 'live_square_k')
    kitchen_S_input.send_keys(kitchen_S)

    if(is_obshaga):
        obshaga_select = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[8]/div/div/div/div/div[1]/span')
        obshaga_select.click()


    
    #Город
    city_span = Select(browser.find_element(By.NAME, 'map_geo_id'))
    city_span.select_by_visible_text(city)
    # district_span = Select(browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[10]/div/div/div/div[2]/div[2]/select'))
    # district_span.select_by_visible_text(district)
    # microdistrict_span = Select(browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[10]/div/div/div/div[2]/div[3]/select'))
    # microdistrict_span.select_by_visible_text(microdistrict)
    #ЖК не получилось
    # zk_ul = browser.find_element(By.XPATH, "//*[@id='new-form']/form/div[11]/div/div/div/ulul//li[text()[contains(.,'4YOU')]]")
    # zk_ul.click()

    #Адрес

    street_input = browser.find_element(By.NAME, 'map_street')
    street_input.send_keys(street)

    house_number_input = browser.find_element(By.NAME, 'map_house_num')
    house_number_input.send_keys(house_number)

    second_street_input = browser.find_element(By.NAME, 'map_corner_street')
    second_street_input.send_keys(second_street)

    # Параметры

    if(flat_status == "good"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[22]/div/div/div/div/div[1]/span')
        flat_status_span.click()
    elif(flat_status == "middle"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[22]/div/div/div/div/div[2]/span')
        flat_status_span.click()
    elif(flat_status == "need_remont"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[22]/div/div/div/div/div[3]/span')
        flat_status_span.click()
    elif(flat_status == "free_plan"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[22]/div/div/div/div/div[4]/span')
        flat_status_span.click()
    elif(flat_status == "black"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[22]/div/div/div/div/div[5]/span')
        flat_status_span.click()


    if(phone == "separate"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[23]/div/div/div/div/div[1]/span')
        flat_status_span.click()
    elif(phone == "block"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[23]/div/div/div/div/div[2]/span')
        flat_status_span.click()
    elif(phone == "can_add"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[23]/div/div/div/div/div[3]/span')
        flat_status_span.click()
    elif(phone == "no"):
        flat_status_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[23]/div/div/div/div/div[4]/span')
        flat_status_span.click()


    if(internet == "ADSL"):
        internet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[24]/div/div/div/div/div[1]/span')
        internet_span.click()
    elif(internet == "TV"):
        internet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[24]/div/div/div/div/div[2]/span')
        internet_span.click()
    elif(internet == "cabel"):
        internet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[24]/div/div/div/div/div[3]/span')
        internet_span.click()
    elif(internet == "optic"):
        internet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[24]/div/div/div/div/div[4]/span')
        internet_span.click()


    if(toilet == "separate"):
        toilet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[25]/div/div/div/div/div[1]/span')
        toilet_span.click()
    elif(toilet == "combined"):
        toilet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[25]/div/div/div/div/div[2]/span')
        toilet_span.click()
    elif(toilet == "2 more"):
        toilet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[25]/div/div/div/div/div[3]/span')
        toilet_span.click()
    elif(toilet == "no"):
        toilet_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[25]/div/div/div/div/div[4]/span')
        toilet_span.click()
    

    if(balcony == "balcony"):
        balcony_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[26]/div/div/div/div/div[1]/span')
        balcony_span.click()
    elif(balcony == "loggia"):
        balcony_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[26]/div/div/div/div/div[2]/span')
        balcony_span.click()
    elif(balcony == "balcony and loggia"):
        balcony_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[26]/div/div/div/div/div[3]/span')
        balcony_span.click()
    elif(balcony == "some"):
        balcony_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[26]/div/div/div/div/div[4]/span')
        balcony_span.click()

    
    if(balcony_window == "yes"):
        balcony_window_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[27]/div/div/div/div/div[2]/span')
        balcony_window_span.click()
    elif(balcony_window == "no"):
        balcony_window_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[27]/div/div/div/div/div[1]/span')
        balcony_window_span.click()


    if(door_type == "wood"):
        door_type_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[28]/div/div/div/div/div[1]/span')
        door_type_span.click()
    elif(door_type == "metal"):
        door_type_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[28]/div/div/div/div/div[2]/span')
        door_type_span.click()
    elif(door_type == "armed"):
        door_type_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[28]/div/div/div/div/div[3]/span')
        door_type_span.click()


    if(parking == "parking"):
        parking_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[29]/div/div/div/div/div[1]/span')
        parking_span.click()
    elif(parking == "garage"):
        parking_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[29]/div/div/div/div/div[2]/span')
        parking_span.click()
    elif(parking == "security"):
        parking_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[29]/div/div/div/div/div[3]/span')
        parking_span.click()


    if(furniture == "all"):
        furniture_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[30]/div/div/div/div/div[1]/span')
        furniture_span.click()
    elif(furniture == "mixed"):
        furniture_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[30]/div/div/div/div/div[2]/span')
        furniture_span.click()
    elif(furniture == "no"):
        furniture_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[30]/div/div/div/div/div[3]/span')
        furniture_span.click()


    if(floor == "linoleum"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[1]/span')
        floor_span.click()
    elif(floor == "parket"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[2]/span')
        floor_span.click()
    elif(floor == "laminat"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[3]/span')
        floor_span.click()
    elif(floor == "wood"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[4]/span')
        floor_span.click()
    elif(floor == "cavrolan"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[5]/span')
        floor_span.click()
    elif(floor == "tile"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[6]/span')
        floor_span.click()
    elif(floor == "cork"):
        floor_span = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[31]/div/div/div/div/div[7]/span')
        floor_span.click()



    roof_height_input = browser.find_element(By.NAME, 'ceiling')
    roof_height_input.send_keys(roof_height)

    # Конченный чек лист не сделал
    if(is_reshetki):
        is_reshetki_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[1]/label')
        is_reshetki_check.click()
    if(is_security):
        is_security_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[2]/label')
        is_security_check.click()
    if(is_domophone):
        is_domophone_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[3]/label')
        is_domophone_check.click()
    if(is_zamok):
        is_zamok_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[4]/label')
        is_zamok_check.click()
    if(is_signal):
        is_signal_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[5]/label')
        is_signal_check.click()
    if(is_camera):
        is_camera_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[6]/label')
        is_camera_check.click()
    if(is_videodomophone):
        is_videodomophone_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[7]/label')
        is_videodomophone_check.click()
    if(is_konsier):
        is_konsier_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[33]/div/div/div/div[8]/label')
        is_konsier_check.click()


    #Another
    if(is_plastic_windows):
        is_plastic_windows_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[1]/label')
        is_plastic_windows_check.click()
    if(is_angle):
        is_angle_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[2]/label')
        is_angle_check.click()
    if(is_upgraded):
        is_upgraded_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[3]/label')
        is_upgraded_check.click()
    if(is_isolated):
        is_isolated_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[4]/label')
        is_isolated_check.click()
    if(is_kitchen_studio):
        is_kitchen_studio_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[5]/label')
        is_kitchen_studio_check.click()
    if(is_kitchen_in):
        is_kitchen_in_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[6]/label')
        is_kitchen_in_check.click()
    if(is_new_plumbing):
        is_new_plumbing_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[7]/label')
        is_new_plumbing_check.click()
    if(is_storage):
        is_storage_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[8]/label')
        is_storage_check.click()
    if(is_counters):
        is_counters_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[9]/label')
        is_counters_check.click()
    if(is_quiet):
        is_quiet_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[10]/label')
        is_quiet_check.click()
    if(is_conditioner):
        is_conditioner_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[11]/label')
        is_conditioner_check.click()
    if(is_commerce):
        is_commerce_check = browser.find_element(By.XPATH, '//*[@id="new-form"]/form/div[34]/div/div/div/div[12]/label')
        is_commerce_check.click()
    

    text_input = browser.find_element(By.NAME, 'text')
    text_input.send_keys(text)

    # company_name_input = browser.find_element(By.NAME, 'profileName')
    # company_name_input.send_keys(company_name)


    mail_input = browser.find_element(By.NAME, 'email')
    mail_input.send_keys(mail)

time.sleep(1000) 
browser.quit()