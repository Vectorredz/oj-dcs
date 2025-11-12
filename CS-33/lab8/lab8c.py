
"""
l - reporters
r - cameras

While (reporters not paired)
    option <- reporter.preference
    if cameras not paired:
        pair reporters and option
        pop reporter 
    else cameras paired:
        if cameras.pref[current] > cameras.pref[operator]:
            reject operator
            pop current, operator
        else:
            pop current
            pair camera to option
return
)
"""
from collections.abc import Sequence, Mapping
from collections import deque, defaultdict

type Ranking = Sequence[str]
type Pair = tuple[str, str]

def get_pairings(reporters: Mapping[str, Ranking] , cameras: Mapping[str, Ranking]) -> list[Pair] | None:
    curr_reporters = deque(reporters.keys())
    curr_cameras = deque(cameras.keys())
    pairs = defaultdict(str)
    _reporters = dict(map(lambda x: (x, deque(reporters[x])), reporters))
    _cameras = dict(map(lambda y: (y, deque(cameras[y])), cameras))
    matched = []
    while(curr_reporters):
        # print(curr_reporters)
        reporter = curr_reporters.popleft()
    
        if (_reporters[reporter]):
            option = _reporters[reporter].popleft()
        else: break;
        # case 0: accept reporter
        if option not in pairs:
            pairs[option] = reporter
            _cameras[option].remove(reporter)
        else:
            # case 1: rank(reporter) > rank(current) -> jilt current
            matched_pair = pairs[option]
            if (cameras[option].index(reporter) < cameras[option].index(matched_pair)):
                # jilt the current match
                # _cameras[option].remove(matched_pair)
                pairs[option] = reporter
                curr_reporters.append(matched_pair)
            # case 2: rank(reporter) < rank(current) -> reject
            else:
                # reject the reporter from cameras
                _cameras[option].remove(reporter)
                # check for another traversal
                curr_reporters.append(reporter)
                
    _matched = defaultdict()
    
    for camera in cameras.keys():
        reporter = pairs[camera]
        _matched[reporter] = camera

    for reporter in reporters.keys():
        if (reporter in _matched):
            matched.append((str(reporter), str(_matched[reporter])))

    # print(matched, pairs)
    return matched if len(matched) == len(reporters.keys()) else None

# get_pairings(
#             {
#     "A": ("O", "M", "N", "L", "P"),
#     "B": ("P", "N", "M", "L", "O"),
#     "C": ("M", "P", "L", "O", "N"),
#     "D": ("P", "M", "O", "N", "L"),
#     "E": ("O", "L", "M", "N", "P")
#             },
#              {
#     "L": ("D", "B", "E", "C", "A"),
#     "M": ("B", "A", "D", "C", "E"),
#     "N": ("A", "C", "E", "D", "B"),
#     "O": ("D", "A", "C", "B", "E"),
#     "P": ("B", "E", "A", "C", "D")
#     })

# assert get_pairings({
#     "Mel": ("Kara", "Atom", "Maki"),
#     "Mike": ("Kara", "Maki"),
#     "Jessica": ("Atom", "Maki"),
# }, {
#     "Kara": ("Mel", "Mike"),
#     "Atom": ("Mel", "Jessica"),
#     "Maki": ("Jessica", "Mel", "Mike"),
# }) == [("Mel", "Kara"), ("Mike", "Maki"), ("Jessica", "Atom")]


# assert get_pairings({
#     "Mel": ("Kara", "Atom", "Maki"),
#     "Mike": (),
#     "Jessica": ("Atom", "Maki",  "Kara"),
# }, {
#     "Kara": ("Mel", "Jessica"),
#     "Atom": ("Mel", "Jessica"),
#     "Maki": ("Jessica", "Mel"),
# }) is None
