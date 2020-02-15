from jwt import decode

SECRET_KEY = 'walnut'


# [helper 함수] 토큰 payload 에서 특정 키 attrs(type: list) 들의 값을 가져와 dict로 반환
def decode_info(token, attrs):
    result = {}
    decoded = jwt.decode(token, SECRET_KEY, algorithms='HS256')
    for attr in attrs:
        result[attr] = decoded[attr]
    return result


# [helper 함수] DB 에서 불러온 리턴값인 query object 중 일부 필드만 객체로 추출
def to_dict(query, attrs):
    result = {}
    for attr in attrs:
        result[attr] = getattr(query, attr)
    return result


# [helper 함수] json 중 일부 프로퍼티만 객체로 추출
def extract(json, attrs):
    result = {}
    for attr in attrs:
        result[attr] = json[attr]
    return result


def to_dict_nested(query, attrs, nested_attrs):
    result = {}
    for attr in attrs:
        value = getattr(query, attr)

        if(type(value) is list):
            result[attr] = to_dict(value, nested_attrs)
        else:
            result[attr] = getattr(query, attr)
    return result
