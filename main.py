import urllib.parse


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    try:
        assert parse('https://example.com/path/to/page?name=ferret&color=purple') == \
               {'name': 'ferret', 'color': 'purple'}
        assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == \
               {'name': 'ferret', 'color': 'purple'}
        assert parse('http://example.com/') == {}
        assert parse('http://example.com/?') == {}
        assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    except AssertionError as err:
        print(err)


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    try:
        assert parse_cookie('name=Dima;') == {'name': 'Dima'}
        assert parse_cookie('') == {}
        assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
        assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    except AssertionError as err:
        print(err)
