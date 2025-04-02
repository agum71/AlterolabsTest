# Created by Agum Aditya
# Github: https://github.com/agum71
# Made in Python 3.13.2

import json
with open('comments.json') as file:
    comments = json.load(file)


def optimal_comments_recursive(comments: dict, depth_limit: int):

    # memory for recursive calls
    memory = {}

    def dfs(comment, depth):
        # depth limit reached
        if depth > depth_limit:
            return 0, []

        # check memory to avoid redundant calculations
        if (comment['id'], depth) in memory:
            return memory[(comment['id'], depth)]

        # include child comments
        include_score = comment['score']
        included_comments = [comment['id']]

        # storing child scores with comments
        child_entity = []
        for child in comment['children']:
            child_score, child_comments = dfs(child, depth + 1)
            child_entity.append((child_score, child_comments))

        # Add child scores to the "include" case
        for child_score, child_comments in child_entity:
            include_score += child_score
            included_comments.extend(child_comments)

        # exclude child comments
        exclude_score = sum(child_score for child_score, _ in child_entity)
        excluded_comments = [comment for _,
                             comment in child_entity for comment in comment]

        # Choose the better option
        if include_score > exclude_score:
            result = (include_score, included_comments)
        else:
            result = (exclude_score, excluded_comments)

        # store in memory latest calulation
        memory[(comment['id'], depth)] = result

        return result

    total_score, selected_comments = dfs(comments, 0)
    return selected_comments


# test input
thread = {
    "id": 1, "score": 10, "children": [
        {"id": 2, "score": 5, "children": [
            {"id": 4, "score": -2, "children": []},
            {"id": 5, "score": 8, "children": []}
        ]},
        {"id": 3, "score": -3, "children": [
            {"id": 6, "score": 7, "children": []}
        ]}
    ]
}


if __name__ == '__main__':
    print("running.....")

    # set limit depth
    depth_limit = 2

    # can change comments for custom input like thread
    print(optimal_comments_recursive(thread, depth_limit))
