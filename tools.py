import datetime


def extract_log_param(d):
    """
    To extract logger format for a param dict
    :param d: dict
    :return:  str
    >>> extract_log_param({"a": 1})
    '[a=1]'
    """
    param_list = list()
    for k, v in d.items():
        param_list.append("[{0}={1}]".format(k, v))
    return " ".join(param_list)


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
