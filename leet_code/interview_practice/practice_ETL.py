import json
import csv
from dateutil import parser, tz

# with open("mapreduce/input.txt", "r") as file:
#     sessions = json.load(file)
#     print(f"we found {len(sessions)} sessions")

#     # for session in sessions:
#     #     print(session)

#     sesh = sessions[0]

class Session:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.cleaned = { }

    def is_valid(self):
        try:
            return all([
                "session_id" in self.raw,
                "user" in self.raw,
                "language" in self.raw,
                "start_time" in self.raw,
                "end_time" in self.raw,
                "feedback_score" in self.raw,
                "metadata" in self.raw,
                "id" in self.raw["user"],
                "name" in self.raw["user"],
                "device" in self.raw["metadata"]
            ])
        except:
            False

    def to_utc(self, time_str):
        return parser.isoparse(time_str).astimezone(tz.UTC).isoformat()
    
    def get_duration(self, start_str, end_str):
        start = parser.isoparse(start_str)
        end = parser.isoparse(end_str)
        return round((end - start).total_seconds() / 60, 2)
    

    def transform(self):
        self.cleaned = {
            "session_id": self.raw["session_id"],
            "user_id": self.raw["user"]["id"],
            "user_name": self.raw["user"]["name"],
            "language": self.raw["language"],
            "start_time": self.to_utc(self.raw["start_time"]),
            "end_time": self.to_utc(self.raw["end_time"]),
            "duration_minutes": self.get_duration(self.raw["start_time"], self.raw["end_time"]),
            "feedback_score": self.raw["feedback_score"],
            "device": self.raw["metadata"]["device"]
        }

class SessionProcessor:
    pass

    

