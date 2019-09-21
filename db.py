from models.user import User
from models.club import Club
import scraper

db = {
    # User objects
    "users": [],
    # Club objects
    "clubs": []
}


def get_user(username):
    potential_users = [user for user in db["users"] if user.username == username]
    if len(potential_users) > 0:
        return potential_users[0].get_safe_data()


def favorite(username, club_name):
    potential_users = [user for user in db["users"] if user.username == username]
    potential_clubs = [club for club in db["clubs"] if club.name == club_name]
    if len(potential_users):
        if len(potential_clubs) > 0:
            if club_name not in potential_users[0].favorites:
                potential_users[0].favorites.append(club_name)
                return "success"
            # not really success but more that the operation was redundant
            return "success"
        return "Club does not exist"
    return "User does not exist"


def unfavorite(username, club_name):
    potential_users = [user for user in db["users"] if user.username == username]
    if len(potential_users) > 0:
        potential_users[0].favorites = [club for club in potential_users[0].favorites if club_name != club]


def get_clubs():
    clubs = [club.get_safe_data() for club in db["clubs"]]
    for club in clubs:
        club["favorite_count"] = 0
        for user in db["users"]:
            if club["name"] in user.favorites:
                club["favorite_count"] += 1
    return clubs


def create_one_club(club_dict):
    if "name" in club_dict and "description" in club_dict:
        matching_clubs = [club for club in db["clubs"] if club.name == club_dict["name"]]
        if len(matching_clubs) < 1:
            db["clubs"].append(
                Club(
                    club_dict["name"],
                    club_dict["description"],
                    club_dict["tags"] if "tags" in club_dict else None
                )
            )
            return "success"
        return "There is already a club with that name."
    return "Insufficient data to create a club. Both a name and description are required."


def get_initial_users():
    return [User("jen", None, None)]


def populate():
    db["users"] = get_initial_users()
    db["clubs"] = scraper.get_all_clubs()


'''
Tests
populate()
print(get_user("jen"))
favorite("jen", "PennLabs")
print(get_user("jen"))
favorite("jen", "Arun Fan Club")
print(get_user("jen"))
print(get_clubs())
unfavorite("jen", "PennLabs")
print(get_user("jen"))
print(get_clubs())
'''
