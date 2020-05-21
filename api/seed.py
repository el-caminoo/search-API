
def generate():
    authors = []
    posts = []
    for i in range(1, 6):
        authors.append({
            "model": "Author",
            "fields": {
                "first_name": "firstName%i",
                "last_name": "lastName%1"
            }
        })
        posts.append({
            "model": "Post",
            "fields": {
                "id": i,
                "url": "/posts/%i",
                "title": "New substitution rules %i",
                "body": "balloteelli is a foolxd",
                "created": "2020-05-15",
                "modified": "2020-05-17",
                "tags": [
                "New",
                "substitution",
                "rules"
                ],
                "author": "user"%i,
                "userId": i
            }
        })
    return objects
