from dataclasses import dataclass

@dataclass
class Node:
    customer: str
    next: "Node | None" = None

@dataclass
class QueueVersion:
    head: Node | None
    tail: Node | None

class TippyMemory:
    def __init__(self):
        self.versions: dict[int, QueueVersion] = {}
        self.current: QueueVersion = QueueVersion(None, None)

    def entered_line(self, t: int, customer: str) -> None:
        # clone current version logically
        head, tail = self.current.head, self.current.tail
        new_node = Node(customer)
        if tail:
            tail = Node(tail.customer, tail.next)  # careful: persistence
            tail.next = new_node
        else:
            head = new_node
        tail = new_node
        new_version = QueueVersion(head, tail)
        self.versions[t] = new_version
        self.current = new_version

    def front_served(self, t: int) -> None:
        head, tail = self.current.head, self.current.tail
        if head:
            head = head.next
            if head is None:
                tail = None
        new_version = QueueVersion(head, tail)
        self.versions[t] = new_version
        self.current = new_version

    def slept(self, t: int) -> None:
        # drop all versions after t
        self.versions = {time: v for time, v in self.versions.items() if time <= t}
        # reset current to the latest ≤ t
        if self.versions:
            maxt = max(self.versions.keys())
            self.current = self.versions[maxt]
        else:
            self.current = QueueVersion(None, None)

    def front(self, t: int) -> str | None:
        # find latest version ≤ t
        candidates = [time for time in self.versions if time <= t]
        if not candidates:
            return None
        v = self.versions[max(candidates)]
        return v.head.customer if v.head else None
