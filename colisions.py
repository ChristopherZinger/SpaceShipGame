


def detect_colision(item_a, item_b):
    try:
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
    except:
        print('error occured during colision. colisions.py')
