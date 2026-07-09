class Meeting:
    def __init__(self, start_time : int, end_time : int) -> None:
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return f"Meeting: {self.start_time} to {self.end_time}"

def conflict(meeting : Meeting, accepted : list):
    x = meeting.start_time
    y = meeting.end_time
    for i in accepted:
        if i is None:
            continue
        if x < i.end_time and y > i.start_time:
            return True
        
    return False

meetings = [m1 := Meeting(6,9), m2 := Meeting(3,4), m3 := Meeting(7, 10), m4 := Meeting(9, 10)]
accepted = []
for meeting in meetings:
    if not conflict(meeting, accepted):
        accepted.append(meeting)
print(accepted)
