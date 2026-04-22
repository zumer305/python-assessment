# Class to represent a log event
class LogEvent:

    # Constructor: initialize object attributes
    def __init__(self, timestamp, level, event, user):
        self.timestamp = timestamp   # time of event
        self.level = level           # level (ERROR, INFO, etc.)
        self.event = event           # event description
        self.user = user             # user who performed action

    # __repr__: gives readable string when object is printed
    def __repr__(self):
        return f"LogEvent(time={self.timestamp}, level='{self.level}', event='{self.event}', user='{self.user}')"

    # __eq__: defines equality between two objects
    def __eq__(self, other):
        # check if other object is also LogEvent
        if not isinstance(other, LogEvent):
            return NotImplemented
        
        # two objects are equal if timestamp, event, and user are same
        return (self.timestamp, self.event, self.user) == (other.timestamp, other.event, other.user)

    # __hash__: required for using objects in set/dictionary
    def __hash__(self):
        # hash based on same fields used in __eq__
        return hash((self.timestamp, self.event, self.user))

    # __lt__: used for sorting (less than comparison)
    def __lt__(self, other):
        # if timestamps are same, compare level alphabetically
        if self.timestamp == other.timestamp:
            return self.level < other.level
        
        # otherwise compare timestamps
        return self.timestamp < other.timestamp




# Creating log event objects
e1 = LogEvent(10, "ERROR", "Login Failed", "Ali")
e2 = LogEvent(10, "ERROR", "Login Failed", "Ali")   # duplicate
e3 = LogEvent(12, "INFO", "Logout", "Sara")
e4 = LogEvent(10, "WARNING", "Password Weak", "Ali")

#  Deduplication using set (hash,equal)
event_set = {e1, e2, e3, e4}

print("After removing duplicates:")
for e in event_set:
    print(e)   # __repr__ will be used


#  Sorting using list
event_list = [e1, e2, e3, e4]

# sorted() uses __lt__ method internally
sorted_events = sorted(event_list)

print("\nSorted Events:")
for e in sorted_events:
    print(e)