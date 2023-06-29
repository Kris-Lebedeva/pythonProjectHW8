# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения.
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий.
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.
# class PhoneBook:
#     def __init__(self):
#         self.contacts = []
#
#     def add_contact(self, name, phone):
#         self.contacts.append({'name': name, 'phone': phone})
#
#     def search_contact(self, name):
#         results = []
#         for contact in self.contacts:
#             if contact['name'] == name:
#                 results.append(contact)
#         return results
#
#     def export_contacts(self, filename):
#         with open(filename, 'w') as file:
#             for contact in self.contacts:
#                 file.write(f"{contact['name']},{contact['phone']}\n")
#
#     def import_contacts(self, filename):
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 name, phone = line.strip().split(',')
#                 self.add_contact(name, phone)
#
# phone_book = PhoneBook()
# phone_book.add_contact('Ivanov Nikita', '9285551234')
# phone_book.add_contact('Sidorova Maria', '9385555678')
# phone_book.add_contact('Voronova Daria', '9185559012')
#
# results = phone_book.search_contact('Sidorova Maria')
# print(results)
#
# phone_book.export_contacts('phonebook.txt')
#
# phone_book2 = PhoneBook()
# phone_book2.import_contacts('phonebook.txt')
# print(phone_book2.contacts)
