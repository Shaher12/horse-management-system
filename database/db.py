
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from datetime import datetime
from database.enums import Status, Breed, Color
from database.collections import Horse, HorseOwner, Article, Editor, Post, Group, Contact, GroupContact, Platform, SharePostHistory, ArticleHistory, PostHistory

client = MongoClient(
    "mongodb+srv://admin_hm:UGbZpqFXSkXW1fj5@horsemanagement.rj9o0.mongodb.net/HorseManagement?retryWrites=true&w=majority", server_api=ServerApi('1'), tlsCAFile=certifi.where())
hm_db = client["HorseManagement"]


def init():
    if not HorseOwner.is_exist(hm_db):
        add_horse_owner_samples()
    if not Horse.is_exist(hm_db):
        add_horse_samples()
    if not Editor.is_exist(hm_db):
        add_editor_samples()
    if not Article.is_exist(hm_db):
        add_article_samples()
    if not ArticleHistory.is_exist(hm_db):
        add_article_history_samples()
    if not Post.is_exist(hm_db):
        add_post_samples()
    if not PostHistory.is_exist(hm_db):
        add_post_history_samples()
    if not Group.is_exist(hm_db):
        add_group_samples()
    if not Contact.is_exist(hm_db):
        add_contact_samples()
    if not GroupContact.is_exist(hm_db):
        add_group_contact_samples()
    if not Platform.is_exist(hm_db):
        add_platform_samples()
    if not SharePostHistory.is_exist(hm_db):
        add_share_post_history_samples()


def add_horse(horse: Horse):
    horse_doc = {"unique_id": horse.unique_id, "name": horse.name, "owner_id": horse.owner_id, "weight": horse.weight, "dob": horse.dob,
                 "breed": horse.breed, "diet": horse.diet, "speed": horse.speed, "color": horse.color, "status": int(horse.status)}
    hm_db.Horse.insert_one(horse_doc)


def add_horse_owner(horse_owner: HorseOwner):
    horse_owner_doc = {"username": horse_owner.username, "password": horse_owner.password, "email": horse_owner.email, "first_name": horse_owner.first_name,
                       "last_name": horse_owner.last_name, "phone_num": horse_owner.phone_num, "joining_date": horse_owner.joining_date, "status": int(horse_owner.status)}
    hm_db.HorseOwner.insert_one(horse_owner_doc)


def add_editor(editor: Editor):
    editor_doc = {"username": editor.username, "password": editor.password, "email": editor.email, "first_name": editor.first_name,
                  "last_name": editor.last_name, "phone_num": editor.phone_num, "joining_date": editor.joining_date, "status": editor.status}
    hm_db.Editor.insert_one(editor_doc)


def add_article(article: Article):
    article_doc = {"title": article.title, "editor_id": article.editor_id, "meta_description": article.meta_description, "text": article.text, "review_object": article.review_object,
                   "banner_url": article.banner_url, "horse_id": article.horse_id, "keywords": article.keywords, "is_approved": article.is_approved}
    hm_db.Article.insert_one(article_doc)


def add_article_history(article_history: ArticleHistory):
    article_history_doc = {"article_id": article_history.article_id,
                           "last_update_date": article_history.last_update_date}
    hm_db.ArticleHistory.insert_one(article_history_doc)


def add_post(post: Post):
    post_doc = {"title": post.title, "editor_id": post.editor_id, "meta_description": post.meta_description, "text": post.text, "review_object": post.review_object,
                "banner_url": post.banner_url, "horse_id": post.horse_id, "keywords": post.keywords, "is_approved": post.is_approved}
    hm_db.Post.insert_one(post_doc)


def add_post_history(post_history: PostHistory):
    post_history_doc = {"post_id": post_history.post_id,
                        "last_update_date": post_history.last_update_date}
    hm_db.PostHistory.insert_one(post_history_doc)


def add_contact(contact: Contact):
    contact_doc = {"name": contact.name, "email": contact.email, "phone_num": contact.phone_num,
                   "facebook_acc": contact.facebook_acc, "instagram_acc": contact.instagram_acc, "status": int(contact.status)}
    hm_db.Contact.insert_one(contact_doc)


def add_group(group: Group):
    group_doc = {"name": group.name, "description": group.description}
    hm_db.Group.insert_one(group_doc)


def add_group_contact(group_contact: GroupContact):
    group_contact_doc = {"group_id": group_contact.group_id,
                         "contact_id": group_contact.contact_id}
    hm_db.GroupContact.insert_one(group_contact_doc)


def add_platform(platform: Platform):
    platform_doc = {"name": platform.name,
                    "username": platform.username, "api": platform.api}
    hm_db.Platform.insert_one(platform_doc)


def add_share_post_history(share_post_history: SharePostHistory):
    share_post_history_doc = {"post_id": share_post_history.post_id, "contact_id": share_post_history.contact_id,
                              "platform_id": share_post_history.platform_id, "added_on": share_post_history.added_on}
    hm_db.SharePostHistory.insert_one(share_post_history_doc)


def add_horse_owner_samples():
    add_horse_owner(HorseOwner("Jill", "JillPassword", "Jill@gmail.com", "Jill", "McDonald", "0485189321", datetime.strptime(
        "13-10-1990", "%d-%m-%Y"), Status.ACTIVE))
    add_horse_owner(HorseOwner("Gabrielle", "GabriellePassword", "Gabrielle@gmail.com", "Gabrielle", "Lekon", "0483892782", datetime.strptime(
        "09-03-1972", "%d-%m-%Y"), Status.ACTIVE))


def add_horse_samples():
    add_horse(Horse("A45F90II", "Ziko", HorseOwner.get(hm_db, "Jill"), 240.6, datetime.strptime(
        "13-10-2010", "%d-%m-%Y"), Breed.ANDALUSIAN, "No Diet", 40, Color.SORREL, Status.ACTIVE))
    add_horse(Horse("A4P0925G", "Rocky", HorseOwner.get(hm_db, "Gabrielle"), 310.2, datetime.strptime(
        "06-10-2005", "%d-%m-%Y"), Breed.ARABIAN, "Vegeterian", 50, Color.GREY, Status.NOT_ACTIVE))


def add_editor_samples():
    add_editor(Editor("Shaher", "ShaherPassword", "Shaher@gmail.com", "Shaher", "Aljaber", "0483678453", datetime.strptime(
        "22-05-1990", "%d-%m-%Y"), Status.ACTIVE))
    add_editor(Editor("Paul", "PaulPassword", "Paul@hotmail.com", "Paul", "Tiken", "0484801992", datetime.strptime(
        "28-11-1983", "%d-%m-%Y"), Status.ACTIVE))
    add_editor(Editor("James", "JamesPassword", "James@hotmail.com", "James", "Green", "0481290442", datetime.strptime(
        "10-07-1974", "%d-%m-%Y"), Status.NOT_ACTIVE))


def add_article_samples():
    add_article(Article("White horse running", Editor.get(hm_db, "Shaher"), "Horse running", "White horse running, and it looks beutiful", "Looks nice",
                "https://images.pexels.com/photos/1996333/pexels-photo-1996333.jpeg", Horse.get(hm_db, "A45F90II"), ["White", "First", "Run", "Ziko"], True))
    add_article(Article("Horse standing in nature", Editor.get(hm_db, "Paul"), "Horse standing", "Brown horse standing in the nature and looks away", "Need some edit",
                "https://images.pexels.com/photos/635499/pexels-photo-635499.jpeg", Horse.get(hm_db, "A4P0925G"), ["Nature", "Second", "Mountain", "Rocky"], True))


def add_article_history_samples():
    add_article_history(ArticleHistory(Article.get(hm_db, "White horse running"),
                        datetime.strptime("01-05-2022T10:53:53.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_article_history(ArticleHistory(Article.get(hm_db, "White horse running"),
                        datetime.strptime("02-05-2022T09:30:21.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_article_history(ArticleHistory(Article.get(hm_db, "Horse standing in nature"),
                        datetime.strptime("19-03-2022T11:20:03.000Z", "%d-%m-%YT%H:%M:%S.000Z")))


def add_post_samples():
    add_post(Post("White horse running", Editor.get(hm_db, "Shaher"), "Horse running", "White horse running, and it looks beutiful", "Looks nice",
                  "https://images.pexels.com/photos/1996333/pexels-photo-1996333.jpeg", Horse.get(hm_db, "A45F90II"), ["White", "First", "Run", "Ziko"], True))
    add_post(Post("Horse standing in nature", Editor.get(hm_db, "Paul"), "Horse standing", "Brown horse standing in the nature and looks away", "Need some edit",
                  "https://images.pexels.com/photos/635499/pexels-photo-635499.jpeg", Horse.get(hm_db, "A4P0925G"), ["Nature", "Second", "Mountain", "Rocky"], True))


def add_post_history_samples():
    add_post_history(PostHistory(Post.get(hm_db, "White horse running"), datetime.strptime(
        "13-04-2022T20:59:42.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_post_history(PostHistory(Post.get(hm_db, "White horse running"), datetime.strptime(
        "14-04-2022T19:36:42.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_post_history(PostHistory(Post.get(hm_db, "Horse standing in nature"),
                     datetime.strptime("20-03-2022T19:30:13.000Z", "%d-%m-%YT%H:%M:%S.000Z")))


def add_group_samples():
    add_group(Group("Admin", "Administrators"))
    add_group(Group("Top Owners", "Top horse owners"))
    add_group(Group("Race Bidders", "People who bid in races"))


def add_contact_samples():
    add_contact(Contact("Liza", "Liza@gmail.com", "0484900617",
                "facebook.com/liza", "instagram.com/liza", Status.ACTIVE))
    add_contact(Contact("George", "George@gmail.com", "0484782911",
                "facebook.com/george", "instagram.com/george", Status.ACTIVE))
    add_contact(Contact("Jack", "Jack@gmail.com", "0484179022",
                "facebook.com/jack", "instagram.com/jack", Status.ACTIVE))
    add_contact(Contact("Callum", "Callum@gmail.com", "0482890311",
                "facebook.com/callum", "instagram.com/callum", Status.NOT_ACTIVE))
    add_contact(Contact("Thomas", "Thomas@gmail.com", "0488902821",
                "facebook.com/thomas", "instagram.com/thomas", Status.ACTIVE))


def add_group_contact_samples():
    add_group_contact(GroupContact(
        Group.get(hm_db, "Admin"), Contact.get(hm_db, "Liza")))
    add_group_contact(GroupContact(
        Group.get(hm_db, "Top Owners"), Contact.get(hm_db, "George")))
    add_group_contact(GroupContact(
        Group.get(hm_db, "Top Owners"), Contact.get(hm_db, "Thomas")))
    add_group_contact(GroupContact(
        Group.get(hm_db, "Race Bidders"), Contact.get(hm_db, "Jack")))
    add_group_contact(GroupContact(
        Group.get(hm_db, "Race Bidders"), Contact.get(hm_db, "Callum")))
    add_group_contact(GroupContact(
        Group.get(hm_db, "Race Bidders"), Contact.get(hm_db, "Thomas")))


def add_platform_samples():
    add_platform(Platform("Facebook", "horsemanagement_melbourne",
                 "238kj234h87234u2hiu4ddn23x22rr76u3"))
    add_platform(Platform("Instagram", "hm_melbourne",
                 "43634jmrf34r#GeR45TE%tyhrthFgdfgdfh764gf"))
    add_platform(Platform("Whatsapp", "hm_in_melbourne", "+61482900819"))


def add_share_post_history_samples():
    add_share_post_history(SharePostHistory(Post.get(hm_db, "White horse running"), Contact.get(hm_db, "George"), Platform.get(
        hm_db, "Facebook"), datetime.strptime("13-04-2022T20:59:42.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_share_post_history(SharePostHistory(Post.get(hm_db, "White horse running"), Contact.get(hm_db, "Thomas"), Platform.get(
        hm_db, "Facebook"), datetime.strptime("13-04-2022T20:59:42.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_share_post_history(SharePostHistory(Post.get(hm_db, "Horse standing in nature"), Contact.get(
        hm_db, "Jack"), Platform.get(hm_db, "Instagram"), datetime.strptime("09-04-2022T13:08:24.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
    add_share_post_history(SharePostHistory(Post.get(hm_db, "Horse standing in nature"), Contact.get(
        hm_db, "Thomas"), Platform.get(hm_db, "Instagram"), datetime.strptime("09-04-2022T13:08:24.000Z", "%d-%m-%YT%H:%M:%S.000Z")))
