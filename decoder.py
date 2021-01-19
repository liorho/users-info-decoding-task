import re
import json
from datetime import datetime

file_to_decode = "ex_v7.txt"
file_data = open(file_to_decode, encoding="ISO-8859-1").read()
sections = file_data.split("\n")

first_names_str = sections[0][4:]
last_names_str = sections[1][4:]
phones_str = sections[2][4:]
times_str = sections[3][4:]

first_names_list = re.split('(\w{4}000\w{2}(?!\d))', first_names_str)[1:]
last_names_list = re.split('(\w{4}000\w{2}(?!\d))', last_names_str)[1:]
phones_list = re.split('(\w{4}000\w{2}(?=[\d\+\-]))', phones_str)[1:]
times_list = re.split('(\w{4}000\w{2}(?=\d))', times_str)[1:]

users_info = {}

for i in range(0, len(first_names_list), 2):
  if users_info.get(first_names_list[i][:4]):
    users_info[first_names_list[i][:4]]['first_name'] = first_names_list[i + 1].replace('\xa0', ' ')
  else:
    users_info[first_names_list[i][:4]] = {'first_name': first_names_list[i + 1].replace('\xa0', ' ')}

for i in range(0, len(last_names_list), 2):
  if users_info.get(last_names_list[i][:4]):
    users_info[last_names_list[i][:4]]['last_name'] = last_names_list[i + 1].replace('\xa0', ' ')
  else:
    users_info[last_names_list[i][:4]] = {'last_name': last_names_list[i + 1].replace('\xa0', ' ')}

for i in range(0, len(phones_list), 2):
  if users_info.get(phones_list[i][:4]):
    users_info[phones_list[i][:4]]['phone'] = phones_list[i + 1]
  else:
    users_info[phones_list[i][:4]] = {'phone': phones_list[i + 1]}

for i in range(0, len(times_list), 2):
  if users_info.get(times_list[i][:4]):
    users_info[times_list[i][:4]]['time'] = datetime.fromtimestamp(int(times_list[i + 1])).strftime('%Y-%m-%d %H:%M:%S')
  else:
    users_info[times_list[i][:4]] = {'time': datetime.fromtimestamp(int(times_list[i + 1])).strftime('%Y-%m-%d %H:%M:%S')}

with open('users_info.txt', 'w') as file:
  for k, v in users_info.items():
      file.write(str(k) + ' >>> ' + str(v) + '\n\n')