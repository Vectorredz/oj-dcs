from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class Comment:
    text: str
    upvote_count: int
    responses: Sequence[Comment] = ()

def winners(comments: Sequence[Comment], threshold: int) -> list[str]:
    texts: list[str] = []
    def total_texts(comments: Comment):
        nonlocal texts
        for response in comments.responses:
            if valid_threshold(response.upvote_count, threshold):
                texts.append(response.text)
            total_texts(response)

    for comment in comments:
        root_text = comment.text
        if valid_threshold(comment.upvote_count, threshold):
            texts.append(root_text)
        total_texts(comment)
    # filter length of comments
    k = sorted(texts, key=lambda c: (len(c), c))
    return sorted(k[-3:])

def valid_threshold(upvotes: int, threshold: int):
    return True if upvotes > threshold else False

    
# print(winners((Comment(text="A", upvote_count=9, responses=
#                        [Comment(text="a", upvote_count=110, responses=[]),
#                         Comment(text="ab", upvote_count=110, responses=[])]), Comment(text='B', upvote_count=200, responses=[])), 10))
    
        
def test_winners():
    assert winners((
            Comment(
                text="Oh my god, I can't even begin to explain how ridiculously terrible C is just because it uses "
                     "1 BYTE instead of 1 BIT for boolean values. Like, who thought this was a good idea?", 
                upvote_count=6,
                responses=(
                    Comment(text="LOL", upvote_count=100),
                )),
            Comment(
                text="What part of you seriously thinks that any part of acting like a feline establishes a reputation "
                     "of appreciation?",
                upvote_count=3,
                responses=(
                    Comment(text="huh", upvote_count=100),
                    Comment(text="LOL", upvote_count=100),
                    Comment(text="LOLOLOL", upvote_count=0),
                ))
        ), 5) == [
            "LOL",
            "Oh my god, I can't even begin to explain how ridiculously terrible C is just because it uses 1 BYTE "
                "instead of 1 BIT for boolean values. Like, who thought this was a good idea?",
            "huh",
        ], f"{winners((
            Comment(
                text="Oh my god, I can't even begin to explain how ridiculously terrible C is just because it uses "
                     "1 BYTE instead of 1 BIT for boolean values. Like, who thought this was a good idea?", 
                upvote_count=6,
                responses=(
                    Comment(text="LOL", upvote_count=100),
                )),
            Comment(
                text="What part of you seriously thinks that any part of acting like a feline establishes a reputation "
                     "of appreciation?",
                upvote_count=3,
                responses=(
                    Comment(text="huh", upvote_count=100),
                    Comment(text="LOL", upvote_count=100),
                    Comment(text="LOLOLOL", upvote_count=0),
                ))
        ), 5)}"

    assert winners((
            Comment(text="hi!", upvote_count=7),
            Comment(text="Hi!", upvote_count=6),
            Comment(text="hi!", upvote_count=5),
            Comment(text="hi!", upvote_count=4),
            Comment(text="hi!", upvote_count=3),
            Comment(text="hi!", upvote_count=2),
        ), 5) == [
            "Hi!",
            "hi!",
        ]

    assert winners((
            Comment(text="hi!", upvote_count=7),
            Comment(text="Hi!", upvote_count=6),
            Comment(text="hi!", upvote_count=5),
            Comment(text="hi!", upvote_count=4),
            Comment(text="hi!", upvote_count=3),
            Comment(text="hi!", upvote_count=2),
        ), 6) == [
            "hi!",
        ]
test_winners()