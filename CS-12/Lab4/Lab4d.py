from typing import TypeVar, Mapping

T = TypeVar("T")

def pass_to_the_left(students: Mapping[str, tuple[int, T]]) -> dict[str, list[T]]:
    students = dict(students)
    student_seats: list[tuple[int, str]] = []
    seat_num: list[int] = []

    for name in students:
        seat = students[name][0]
        student_seats.append((seat, name))
        if seat > 0 and seat not in seat_num:
            seat_num.append(seat)
        else:
            raise ValueError
        
    student_seats.sort(key=lambda x: x[0])
    paper: dict[str , list[T]] = {}
    i = 0
    j = 1
    while i <= len(students)-1:
        name = student_seats[i][1]
        paper[name] = [students[name][1]]
        while i <= len(students) and j < len(students) and student_seats[j][0] - student_seats[i][0] == 1:
            seatmate = student_seats[j][1]
            paper[name].append(students[seatmate][1])
            j += 1
            i += 1
        j += 1
        i += 1
    return paper

print(pass_to_the_left({
        "Awamo":     (10, 'BABA'),
        "Camparri":  (12, 'DADA'),
        "Cognac":    (13, '.A.A'),
        "Cukatail":  (56, '....'),
        "Korn":      (64, 'BABE'),
        "Kusu":      (66, 'BAD.'),
        "Marcarita": (67, '.ADA'),
        "Martinu":   (68, 'BEAD'),
        "Mohito":    (65, 'BEBA'),
        "Sour":      (11, 'AAAA'),
        "Vados":     (61, 'BABA'),
        "Whis":      (62, 'BABA'),
    }))

