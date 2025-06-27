import requests


def get_list_from_pinyin(initial: str = "*", final: str = "*", tone: str = "*"):

    def lookup_pinyin(initial: str = "*", final: str = "*", tone: str = "*"):
        url = f"https://zi.tools/api/yin/font/search/cvt:cn;{initial};{final};{tone}/cn,auto"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    json: dict[str, dict[str, list]] = lookup_pinyin(initial, final, tone)

    return set(key for key in json["font"].keys() if not key.startswith("_"))


def get_list_from_ids(ids: str):

    def lookup_ids(ids: str):
        url = f"https://zi.tools/api/ids/lookupids/{ids}?replace_token"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    json: dict[str, dict[str, list]] = lookup_ids(ids)

    char_set = set()
    for k, v in json.items():
        if not k.startswith("_"):
            if k == "font":
                char_set.update(key for key in v.keys() if not key.startswith("_"))
            else:
                char_set.update(v["ids_structure_lookup"])
    return char_set


set_one = get_list_from_pinyin("x", "i")
set_two = get_list_from_ids("⿰扌？")
result = set_one & set_two
print(result)
