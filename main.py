import urllib.parse


def parse(query: str) -> dict:
    parsed_url = urllib.parse.parse_qsl(query)
    if 1 < len(parsed_url) <= 2:
        return {parsed_url[0][0].split('?')[1]: parsed_url[0][1], parsed_url[1][0]: parsed_url[1][1]}
    elif len(parsed_url) > 2:
        return {parsed_url[0][0].split('?')[1]: parsed_url[0][1]}
    elif len(parsed_url) == 0:
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
        assert parse('http://example.com/?name=1') == {'name': '1'}
        assert parse('http://example.com/?name=12') == {'name': '12'}
        assert parse('http://example.com/?name=123') == {'name': '123'}
        assert parse('http://example.com/?name=1234') == {'name': '1234'}
        assert parse('http://example.com/?name=12345') == {'name': '12345'}
        assert parse('http://example.com/?name=11') == {'name': '11'}
        assert parse('http://example.com/?name=22') == {'name': '22'}
        assert parse('http://example.com/?name=23') == {'name': '23'}
        assert parse('http://example.com/?name=234') == {'name': '234'}
        assert parse('http://example.com/?name=13') == {'name': '13'}
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
