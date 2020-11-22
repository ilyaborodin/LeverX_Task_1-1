from file_reader import File_reader
from distribution import Distribution
from unloading import Unloading_info_to_json


def main():
    rooms = File_reader("rooms.json").file_reader
    students = File_reader("students.json").file_reader
    new_info = Distribution(rooms, students).student_distribution
    result = Unloading_info_to_json(new_info).unloading
    print(result)


main()
