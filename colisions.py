from settings import game_area


def detect_colision(item_a, item_b):
    if (
            (
                item_a.x-item_b.wx < item_b.x and
                item_b.x < item_a.x + item_a.wx
            ) and
            (
                item_a.y-item_b.wy < item_b.y and
                item_b.y < item_a.y + item_a.wy
            )
        ):
        return [item_a, item_b]
    else:
        return None

def left_game_area(item):
    if(
        item.x > game_area[0] or
        item.x+item.wx < 0 or
        item.y > game_area[1] or
        item.y + item.wy < 0
        ):
        return True
    else:
        return False
