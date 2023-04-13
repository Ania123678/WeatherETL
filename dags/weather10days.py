import requests
import bs4 as BeautifulSoup
import wordninja


headers = {}
url_weather_10day = ""
response = requests.get(url_weather_10day, headers=headers)
print(response.status_code)
soup = BeautifulSoup.BeautifulSoup(response.text, 'html5lib')

def weather_10days(soup):
    spans = soup.find_all('div', {'class':'DaypartDetails--DetailSummaryContent--1-r0i Disclosure--SummaryDefault--2XBO9'})
    days10_list = []
    for span in spans:
        days10_list.append(span.text)

    days10_list = [x for xs in days10_list for x in xs.split(',')]

    day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15 = [day for day in days10_list]
    return day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15

def weather_day_info(info_list):

    if info_list[0:3] == 'Sat':
      day = [info_list[0:3]]
      info = info_list[4:]
      info = wordninja.split(info)
      info_list = day + info
    else: 
      info_list = wordninja.split(info_list)

    info_list_ = info_list[1]
    if len(info_list_)%2 == 0:
      day = info_list_[0:len(info_list_)//2]
      temp = info_list_[len(info_list_)//2:]

    info_list[0] = info_list[0] + ' ' + day
    info_list[1] = temp

    day = info_list[0]
    temperature_high = int((int(info_list[1]) - 32) * (5/9))
    temperature_low = int((int(info_list[2]) - 32) * (5/9))

    weather = ",".join(info_list[3:5])
    rain = info_list[-7]
    wind = info_list[-4]

    another_day = [day, temperature_high, temperature_low, weather, rain, wind]    
    return another_day


day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15 = weather_10days(soup)

day2 = weather_day_info(day2)
day3 = weather_day_info(day3)
day4 = weather_day_info(day4)
day5 = weather_day_info(day5)
day6 = weather_day_info(day6)
day7 = weather_day_info(day7)
day8 = weather_day_info(day8)
day9 = weather_day_info(day9)

print(day2, day3, day4, day5, day6, day7, day8, day9)



