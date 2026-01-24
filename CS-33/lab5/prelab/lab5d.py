# from collections.abc import Sequence
# from collections import defaultdict

# class MenuPlanning:
#     def __init__(self, initial_menu: Sequence[str]):
#         self.initial_menu: Sequence[str] = initial_menu
#         self.versions: dict[int, list[str]] = defaultdict()
#         super().__init__()

#     def use_without_last(self, m: int) -> None:
#         if m not in self.versions.keys():
#             self.versions[m] = list(self.initial_menu)
#         self.versions[m].pop()
        
 
        
#     def use_with_new(self, m: int, item: str) -> None:
#         if m not in self.versions.keys():
#             self.versions[m] = list(self.initial_menu)
#         self.versions[m].append(item)
        

#     def last_menu_item(self, m: int) -> str | None:
#         if 0 <= m < len(self.versions):
#             return self.versions[m][-1]
#         return None


# # pyright: strict

# def test_MenuPlanning():
#     menu_planning = MenuPlanning(["Trio of Shiny Pearls", "Frozen Evergreen"])
#     print(menu_planning.initial_menu)
#     menu_planning.use_with_new(0, "Melted Essence")  # month 1
    
#     menu_planning.use_with_new(0, "Jet Black Queen") # month 2
#     menu_planning.use_with_new(2, "Twilight Ocean")  # month 3

#     assert menu_planning.last_menu_item(0) == "Jet Black Queen"

#     # menu_planning.use_without_last(3)                # month 4

#     # assert menu_planning.last_menu_item(4) == "Jet Black Queen"
# test_MenuPlanning()
#     # TODO add more tests here

from dataclasses import dataclass
from collections.abc import Sequence

@dataclass
class Node:
    dish: str # value of the top ptr
    next: "Node | None" = None

class MenuPlanning:
    def __init__(self, initial_menu: Sequence[str]):
        stack: "Node | None" = None

        # creates a stack out of the initial menu
        for dish in initial_menu:
            curr = Node(dish, stack)
            stack = curr
            
        self.menus: list[Node | None] = [stack]

        super().__init__()

    def use_without_last(self, m: int) -> None:
        current_menu = self.menus[m]
        new_stack = current_menu.next if current_menu else None
        # push new version of stack
        self.menus.append(new_stack)

    def use_with_new(self, m: int, item: str) -> None:
        current_menu = self.menus[m]
        # creates node that points the new item as the top
        new_item = Node(item, current_menu) if current_menu else Node(item, None)
        self.menus.append(new_item)

    def last_menu_item(self, m: int) -> str | None:
        if self.menus[m]:
            current_stack = self.menus[m]
            return current_stack.dish if current_stack else None
        return None
# pyright: strict


def test_MenuPlanning():
    menu_planning = MenuPlanning(["Trio of Shiny Pearls", "Frozen Evergreen"])

    menu_planning.use_with_new(0, "Melted Essence")  # month 1
    menu_planning.use_with_new(0, "Jet Black Queen") # month 2
    menu_planning.use_with_new(2, "Twilight Ocean")  # month 3

    assert menu_planning.last_menu_item(0) == "Frozen Evergreen"

    menu_planning.use_without_last(3)                # month 4

    assert menu_planning.last_menu_item(4) == "Jet Black Queen"

test_MenuPlanning()