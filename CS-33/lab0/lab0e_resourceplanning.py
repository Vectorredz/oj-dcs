from __future__ import annotations
from materials import Recipe, ItemCount
from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    data: ItemCount
    count_needed: int
    children: list[Node | None]

def mats_needed(item: str, recipes: list[Recipe]):
    # create the item as an item count
    # 1. Construct an item tree that makes the item as the root
    nonBaseItems: list[str] = list(map(lambda x: x.item, recipes))

    def build_tree(item: str, count: int, recipes: list[Recipe]):
        # find the direct successor of the root
        root: Node | None = None
        for recipe in recipes:
            if item == recipe.item:
                root = Node(ItemCount(item, count), count, [])
                for ingredient in recipe.ingredients:
                    # it is a base item
                    if ingredient.item in nonBaseItems:
                        child: Node | None = build_tree(ingredient.item, ingredient.count, recipes)
                        root.children.append(child)
                    else:
                        # create the leaf node
                        count_needed = count * ingredient.count
                        leaf = Node(ingredient, count_needed, [])
                        root.children.append(leaf)
        return root

    root = build_tree(item, 1, recipes)

    # find the roots
    needed_itemCounts: list[ItemCount] = []

    def dfs(root: Node | None):
        if root == None:
            return root
        else:
            
            for child in root.children:
                if child and child.children == []:
                    needed_itemCounts.append(
                        ItemCount(child.data.item, child.count_needed)
                    )
                dfs(child)

    dfs(root)

    return frozenset(needed_itemCounts)

print(mats_needed(
    "brush",
    [
        Recipe(
            item="brush",
            ingredients=[
                ItemCount(item="feather", count=1),
                ItemCount(item="stick", count=1),
                ItemCount(item="copper ingot", count=1),
            ],
        ),
        Recipe(
            item="copper ingot",
            ingredients=[
                ItemCount(item="copper nugget", count=9),
            ]
        )
    ],
))
"""
node(bed) -> func(wool, 3, recipes) = node(wool) -> node(string)
"""