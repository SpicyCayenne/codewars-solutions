"""
Solution for the codewars python challenge "Human Readable Time"
"""

def make_readable(seconds):
    """
    Converts non-negative integer in seconds to human readable format HH:MM:SS
    """
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    seconds = seconds % 60

    return "%02d:%02d:%02d" % (hours, minutes, seconds)


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
