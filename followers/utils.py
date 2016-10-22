from followers.models import Relationship


def get_followers(user):
    relationships = user.relationship_target.select_related('origin')
    followers = list()

    for relationship in relationships:
        followers.append(relationship.origin)

    return followers


def get_following(user):
    relationships = user.relationship_origin.select_related('target')
    following = list()

    for relationship in relationships:
        following.append(relationship.target)

    return following
