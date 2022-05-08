from datetime import date


class Group:
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @staticmethod
    def get(db, name: str) -> str:
        group_id = db.Group.find_one(
            {'name': name}, {"_id": 1}).get("_id")
        return group_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Group" in db.list_collection_names()


class Contact:
    name: str
    email: str
    phone_num: str
    facebook_acc: str
    instagram_acc: str
    status: int

    def __init__(self, name: str, email: str, phone_num: str, facebook_acc: str, instagram_acc: str, status: str):
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.facebook_acc = facebook_acc
        self.instagram_acc = instagram_acc
        self.status = status

    @staticmethod
    def get(db, name: str) -> str:
        contact_id = db.Contact.find_one(
            {'name': name}, {"_id": 1}).get("_id")
        return contact_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Contact" in db.list_collection_names()


class GroupContact:
    group_id: str
    contact_id: str

    def __init__(self, group_id: str, contact_id: str):
        self.group_id = group_id
        self.contact_id = contact_id

    @staticmethod
    def is_exist(db) -> bool:
        return "GroupContact" in db.list_collection_names()


class Platform:
    name: str
    username: str
    api: str

    def __init__(self, name: str, username: str, api: str):
        self.name = name
        self.username = username
        self.api = api

    @staticmethod
    def get(db, name: str) -> str:
        platform_id = db.Platform.find_one(
            {'name': name}, {"_id": 1}).get("_id")
        return platform_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Platform" in db.list_collection_names()


class HorseOwner:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    phone_num: str
    joining_date: date
    status: str

    def __init__(self, username: str, password: str, email: str, first_name: str, last_name: str, phone_num: str, joining_date: date, status: str):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.joining_date = joining_date
        self.status = status

    @staticmethod
    def get(db, username: str) -> str:
        owner_id = db.HorseOwner.find_one(
            {'username': username}, {"_id": 1}).get("_id")
        return owner_id

    @staticmethod
    def is_exist(db) -> bool:
        return "HorseOwner" in db.list_collection_names()


class Horse:
    unique_id: int
    name: str
    owner_id: str
    weight: float
    dob: date
    breed: str
    diet: str
    speed: int
    color: str
    status: int

    def __init__(self, unique_id: str, name: str, owner_id: str, weight: float, dob: date, breed: str, diet: str, speed: int, color: str, status: int):
        self.unique_id = unique_id
        self.name = name
        self.owner_id = owner_id
        self.weight = weight
        self.dob = dob
        self.breed = breed
        self.diet = diet
        self.speed = speed
        self.color = color
        self.status = status

    @staticmethod
    def get(db, unique_id: str) -> str:
        horse_id = db.Horse.find_one(
            {'unique_id': unique_id}, {"_id": 1}).get("_id")
        return horse_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Horse" in db.list_collection_names()


class Editor:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    phone_num: str
    joining_date: date
    status: int

    def __init__(self, username: str, password: str, email: str, first_name: str, last_name: str, phone_num: str, joining_date: date, status: int):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.joining_date = joining_date
        self.status = status

    @staticmethod
    def get(db, username: str) -> str:
        editor_id = db.Editor.find_one(
            {'username': username}, {"_id": 1}).get("_id")
        return editor_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Editor" in db.list_collection_names()


class Post:
    title: str
    editor_id: str
    meta_description: str
    text: str
    review_object: str
    banner_url: str
    horse_id: str
    keywords: list
    is_approved: bool

    def __init__(self, title: str, editor_id: str, meta_description: str, text: str, review_object: str, banner_url: str, horse_id: str, keywords: list, is_approved: bool):
        self.title = title
        self.editor_id = editor_id
        self.meta_description = meta_description
        self.text = text
        self.review_object = review_object
        self.banner_url = banner_url
        self.horse_id = horse_id
        self.keywords = keywords
        self.is_approved = is_approved

    @staticmethod
    def get(db, title: str) -> str:
        post_id = db.Post.find_one(
            {'title': title}, {"_id": 1}).get("_id")
        return post_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Post" in db.list_collection_names()


class PostHistory:
    post_id: str
    last_update_date: date

    def __init__(self, post_id: str, last_update_date: date):
        self.post_id = post_id
        self.last_update_date = last_update_date

    @staticmethod
    def is_exist(db) -> bool:
        return "PostHistory" in db.list_collection_names()


class Article:
    title: str
    editor_id: str
    meta_description: str
    text: str
    review_object: str
    banner_url: str
    horse_id: str
    keywords: list
    is_approved: bool

    def __init__(self, title: str, editor_id: str, meta_description: str, text: str, review_object: str, banner_url: str, horse_id: str, keywords: list, is_approved: bool):
        self.title = title
        self.editor_id = editor_id
        self.meta_description = meta_description
        self.text = text
        self.review_object = review_object
        self.banner_url = banner_url
        self.horse_id = horse_id
        self.keywords = keywords
        self.is_approved = is_approved

    @staticmethod
    def get(db, title: str) -> str:
        article_id = db.Article.find_one(
            {'title': title}, {"_id": 1}).get("_id")
        return article_id

    @staticmethod
    def is_exist(db) -> bool:
        return "Article" in db.list_collection_names()


class ArticleHistory:
    article_id: str
    last_update_date: date

    def __init__(self, article_id: str, last_update_date: date):
        self.article_id = article_id
        self.last_update_date = last_update_date

    @staticmethod
    def is_exist(db) -> bool:
        return "ArticleHistory" in db.list_collection_names()


class SharePostHistory:
    post_id: str
    contact_id: int
    platform_id: str
    added_on: date

    def __init__(self, post_id: str, contact_id: str, platform_id: str, added_on: date):
        self.post_id = post_id
        self.contact_id = contact_id
        self.platform_id = platform_id
        self.added_on = added_on

    @staticmethod
    def is_exist(db) -> bool:
        return "SharePostHistory" in db.list_collection_names()
