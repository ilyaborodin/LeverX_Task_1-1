import json


class Unloading_info_to_json:
    def __init__(self, info_list):
        self.info_list = info_list

    def unloading(self):
        try:
            with open("rooms_with_students.json", 'w') as new_file:
                json.dump(self.info_list, new_file)
        except:
            return "Sorry, you failed"
        finally:
            return "Mission completed"
