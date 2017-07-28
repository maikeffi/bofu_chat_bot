
class JsonUtils(object):
    def change_key(obj, old_key, new_key):
        for key in obj.keys():
            if old_key == key:
                obj[new_key] = obj[old_key]
                del obj[old_key]
        return obj