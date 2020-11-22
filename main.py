from file_reader import File_reader
from distribution import Distribution


def main():
    rooms = File_reader.file_reader("rooms.json")
    students = File_reader.file_reader("students.json")
    print(Distribution.student_distribution(rooms, students))