import datetime

year = 2024
start_date = datetime.date(year, 1, 1)
end_date = datetime.date(year, 12, 31)

mondays = []
saturdays = []

# for i in range((end_date - start_date).days + 1):
#     date = start_date + datetime.timedelta(days=i)
#     if date.weekday() == 0:
#         mondays.append(date.strftime("%Y-%m-%d"))
#     elif date.weekday() == 5:
#         saturdays.append(date.strftime("%Y-%m-%d"))

# print(f"2024年每周一的日期：{', '.join(mondays)}")
# print(f"2024年每周六的日期：{', '.join(saturdays)}")

for i in range((end_date - start_date).days + 1):
    date = start_date + datetime.timedelta(days=i)
    if date.weekday() == 0:
        mondays.append(date.strftime("%m.%d"))
    elif date.weekday() == 5:
        saturdays.append(date.strftime("%m.%d"))

# print(f"2024年每周一 - 周六的日期：{', '.join(mondays)} - {', '.join(saturdays)}")

print("2024年每周一 - 周六的日期：")
for i in range(len(mondays)):
    print(mondays[i], "-", saturdays[i])

