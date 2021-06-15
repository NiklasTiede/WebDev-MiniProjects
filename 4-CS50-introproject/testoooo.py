
# # convert list into string:
# sports_lst = ['Tennis', 'Soccer']
# sports_str = ' '.join(sports_lst)
#
# # string is converted into a string:
# sports_lst = sports_str.split(' ')
# print(sports_lst)

# ----

# from application import db, Registrant
#
# registrants_lst = Registrant.query.all()
# print(registrants_lst)
# for entry in registrants_lst:
#     print(entry)
#
# q = Registrant.query.filter_by(email='niklastiede2@gmail.com').all()
# print(q)
# if q != list():
#     print('queried email is already saved within the db')

# --------
# import os
# x = os.getenv("HOME")
# print(x)


import requests

# analysing a github page and whats extractable
# res = requests.get('https://github.com/NiklasTiede/molecule_data_handler')
# print(res.text)
# res = requests.post('https://github.com/NiklasTiede/molecule_data_handler')
# print(res.text)
# res = requests.put('https://github.com/NiklasTiede/molecule_data_handler')
# print(res.text)
# res = requests.patch('https://github.com/NiklasTiede/molecule_data_handler')
# print(res.text)


def main():
    res = requests.get('https://api.exchangeratesapi.io/latest')
    print(res.text)
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f'1 EUR is equal to {rate} USD')


if __name__ == "__main__":
    main()



def rt_currency_value(currency1='EUR',currency2='USD'):
    """ """













