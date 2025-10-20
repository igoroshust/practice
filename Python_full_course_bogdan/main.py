def image_info(dictionary: dict) -> str:
    if 'image_id' not in dictionary or 'image_title' not in dictionary:
        raise TypeError('Keys image_id and image_title must be present')
    return f"Image '{dictionary['image_title']}' has id {dictionary['image_id']}"

some_dict = {
    'image_id': 123,
    'image_title': 'Ria',
}

try:
    image_info({'image_id': 123})
except TypeError as e:
    print(e)