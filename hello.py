import random

from flask import Flask

app = Flask(__name__)

names = [
    "Tokino Sora",
    "Robocosan",
    "Yozora Mel",
    "Aki Rosenthal",
    "Akai Haato",
    "Shirakami Fubuki",
    "Natsuiro Matsuri",
    "Minato Aqua",
    "Murasaki Shion",
    "Nakiri Ayame",
    "Yuzuki Choco",
    "Oozora Subaru",
    "AZKi",
    "Ookami Mio",
    "Sakura Miko",
    "Nekomata Okayu",
    "Inugami Korone",
    "Hoshimachi Suisei",
    "Usada Pekora",
    "Shiranui Flare",
    "Shirogane Noel",
    "Houshou Marine",
    "Amane Kanata",
    "Tsunomaki Watame",
    "Tokoyami Towa",
    "Himemori Luna",
    "Yukihana Lamy",
    "Momosuzu Nene",
    "Shishiro Botan",
    "Omaru Polka",
    "La+ Darknesss",
    "Takane Lui",
    "Hakui Koyori",
    "Sakamata Chloe",
    "Kazama Iroha",
    "Ayunda Risu",
    "Moona Hoshinova",
    "Airani Iofifteen",
    "Kureiji Ollie",
    "Anya Melfissa",
    "Pavolia Reine",
    "Vestia Zeta",
    "Kaela Kovalskia",
    "Kobo Kanaeru",
    "Mori Calliope",
    "Takanashi Kiara",
    "Ninomae Ina’nis",
    "Gawr Gura",
    "Watson Amelia",
    "IRyS",
    "Ceres Fauna",
    "Ouro Kronii",
    "Nanashi Mumei",
    "Hakos Baelz",
    "Shiori Novella",
    "Koseki Bijou",
    "Nerissa Ravencroft",
    "Fuwawa Abyssgard",
    "Mococo Abyssgard",
    "Kiryu Coco",
    "Tsukumo Sana",
    "Friend A (A-chan)",
    "Harusaki Nodoka",
]


@app.route("/")
def home():
    name = random.choice(names)
    letters = list(name)
    random.shuffle(letters)
    anagram = "".join(letters).strip()
    return f"<p>{anagram.lower()}</p>"
