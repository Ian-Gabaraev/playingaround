from collections import deque


class FaceBookFriend:

    def __init__(self, name: str, is_seller: bool = False):
        self.name = name
        self.is_seller = is_seller

    def __str__(self):
        return self.name


alice = FaceBookFriend("Alice")
bob = FaceBookFriend("Bob")
jack = FaceBookFriend("Jack")
kate = FaceBookFriend("Kate")
kyle = FaceBookFriend("Kyle", True)
hue = FaceBookFriend("Hue")

graph = {
    "you": [alice, bob, jack],
    jack: [kate],
    kate: [kyle, hue]
}

"""
                  YOU
                /  |  \
          alice   bob   jack
                            \
                             kate
                            /    \
                        kyle      hue
"""

search_queue = deque()
search_queue += graph["you"]

while search_queue:
    friend: FaceBookFriend = search_queue.popleft()
    if friend.is_seller:
        print(f"{friend} sells what you want")
        break
    else:
        try:
            search_queue += graph[friend]
        except KeyError:
            continue
