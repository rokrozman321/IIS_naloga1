import urllib.request

# check if arso data returns 200
def test():
    url = "https://arsoxmlwrapper.app.grega.xyz/api/air/archive"

    status_code = urllib.request.urlopen(url).getcode()
    website_is_up = status_code == 200

    print("arso je: ", website_is_up)

    assert status_code == 200