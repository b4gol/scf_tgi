import json
import logging


def not_in(information: str) -> bool:
    inf = reader("result.json")
    for i in inf:
        if i["#"] == information:
            return True
    return False


def reader(filename: str) -> list:
    """read and return list from json file"""
    with open(filename, "r", encoding="utf-8") as file:
        lst = json.load(file)
    return lst


def add_in_json(filename: str, data: list) -> bool:
    """add list of data in json file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3)
    return True


def scrap(txt: str, min: int, percent: float, max: int) -> bool:
    """function for scrapping message if all be good returned True"""
    try:
        text1 = txt.split("#")
        text1.remove("")
        text1 = [text1[i].split("\n")[:-3] for i in range(len(text1))]
        info_about_price = [text1[i][0].split("|") for i in range(len(text1))]
        info_about_user = [text1[i][1].split("|") for i in range(len(text1))]
        all_in_one = reader("result.json")
        for i in range(len(info_about_price)):
            percents = float(info_about_price[i][2].split("%")[0])
            price = float("".join(info_about_price[i][1].split("'")).split(" ")[1])
            if percents <= percent and float(min) <= price <= float(max):
                all_in_one.append({"#": "#" + info_about_price[i][0],
                                   "min": "".join(info_about_price[i][1].split("'")),
                                   "percent": percents,
                                   "max": "".join(info_about_price[i][3].split("'")),
                                   "bank": info_about_price[i][4],
                                   "user": info_about_user[i][0],
                                   "link": "/deal" + info_about_price[i][0]})
        add_in_json("result.json", list(all_in_one))
        return True
    except Exception as e:
        logging.warning(e)
        return False


def check_json() -> bool:
    try:
        get_info = reader("head_db.json")
        if get_info[-1]["payed"]:
            return True
        else:
            return False
    except Exception as e:
        logging.warning(str(e) + "-- warning in check_json --")
        return False

