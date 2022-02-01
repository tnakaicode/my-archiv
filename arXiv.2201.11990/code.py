def update_dict(orig, update):
    """Deep update of a dictionary

    For each entry (k, v) in update such that both orig[k] and v are
    dictionaries, orig[k] is recursively updated to v.

    For all other entries (k, v), orig[k] is set to v.
    """
    for k, v in update.items():
        if isinstance(orig[k], dict) and isinstance(v, dict):
            update_dict(orig[k], v)
        else:
            orig[k] = v