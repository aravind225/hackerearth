class telephone:
    def __init__(self):
        print("calls")
class mob(telephone):
    def __init__(self):
        super().__init__()
        print("messages")
class andr(mob):
    def __init__(self):
        super().__init__()
        print("games","music","cam")
samsung=andr()
