import os


def write_to_repository(folder, page_name, content):
    path = "repository/{}/".format(folder)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + page_name, 'w+', newline='', encoding="utf-8") as page:
        page.writelines(content)


def get_folder_name(seed):
    name = ""
    if '.com' in seed:
        name = seed.removesuffix('.com')
    elif '.fr' in seed:
        name = seed.removesuffix('.fr')
    elif '.ac.kr' in seed:
        name = seed.removesuffix('.ac.kr/sc')

    name = name.removeprefix('https://www.')
    return name
