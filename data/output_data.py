import json
from pathlib import Path


class ActionFile:
    def __init__(self, file):
        self.file = file
        self.data = {}

    def read_file(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as read_file:
                self.data = json.load(read_file)
        except FileNotFoundError:
            if 'price' in str(self.file) or 'sett' in str(self.file):
                Path(self.file).touch()
                self.writer_file()
                # не декоратор?
                self.read_file()


    def writer_file(self, mode='w'):
        with open(self.file, mode) as outfile:
            json.dump(self.data, outfile)

    def get_group_list(self)-> list:
        """Получение списка групп."""
        group_list = []
        for i in self.data['races'][0]['groups']:
            group = {'uuid': i['id'],'name': i['name']}
            group_list.append(group)
        return group_list

    def get_person_list(self)-> list:
        """Получение списка участников."""
        person_list = []
        for i in self.data['races'][0]['persons']:
            person_list.append(i['name'])
        return person_list

    def get_team_list(self)-> list:
        """Получение списка коллективов."""
        team_list = []
        for i in self.data['races'][0]['organizations']:
            team = {'uuid': i['id'],'name': i['name']}
            team_list.append(team)
        return team_list

    def get_group_dict(self)-> dict:
        """Получение словаря групп."""
        return self.data['races'][0]['groups']

    def get_person_dict(self)-> dict:
        """Получение словаря участников."""
        return self.data['races'][0]['persons']

    def get_team_dict(self)-> dict:
        """Получение словаря коллективов."""
        return self.data['races'][0]['organizations']


    def check_is_nan(self):
        """Проверка на пустоту. True -> Пустой."""
        if self.data:
            return False
        else:
            return True