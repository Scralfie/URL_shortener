from werkzeug.exceptions import BadRequest


urls = [
    {'id': 1, 'name': 'https://www.google.com',},
    {'id': 2, 'name': 'https://www.youtube.com'},
    {'id': 3, 'name': 'https://www.twitter.com'}
]

def index(req):
    return [u for u in urls], 200

def create(req):
    new_url = req.get_json()
    new_url['id'] = sorted([u['id'] for u in urls])[-1] + 1
    urls.append(new_url)
    return new_url, 201

def show_by_id(req, id):
    return find_by_id(id), 200

def update(req, id):
    url = find_by_id(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        url[key] =  val.lower()
    return url, 200

def destroy(req, id):
    url = find_by_id(id)
    urls.remove(url)
    return url, 204

def find_by_id(id):
    try:
        return next(url for url in urls if url['id'] == id)
    except:
        raise BadRequest(f"We don't have a chocolate with id {id}!")
