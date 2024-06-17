from m3.actions import ActionPack
from app import models

class PersonPack(ActionPack):
    print('hellow')

    model = models.Person

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True

# class PersonPack(ObjectPack):
#     model = models.Person

#     add_window = edit_window = ModelEditWindow.fabricate(model)

#     add_to_menu = True

#     columns = [
#         {
#             'data_index': 'name',
#             'header': u'Имя',
#             'width': 2,
#         },
#         {
#             'data_index': 'surname',
#             'header': u'Фамилия',
#             'width': 2,
#         },
#         {
#             'data_index': 'gender',
#             'header': u'Пол',
#             'width': 1,
#         },
#         {
#             'data_index': 'birthday',
#             'header': u'Дата рождения',
#             'width': 1,
#         }
#     ]
