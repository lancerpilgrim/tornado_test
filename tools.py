import datetime


def extract_obj_attr(obj, filter_func=None):
    r = {}

    def _protective_filter(x):
        return x.startswith("_")

    filter_func = _protective_filter or filter_func
    for k, v in obj.__dict__.items():
        if not filter_func(k):
            r[k] = v
            if isinstance(v, datetime.datetime):
                r[k] = v.strftime("%Y-%m-%d %H:%M:%S")
    return r
