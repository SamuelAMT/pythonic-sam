# assert

"""
Assert statements are a convenient way to insert debugging assertions into a program
"""

def assert_function(data: dict):
    assert isinstance(data, dict), 'Invalid JSON'
    assert data, 'No data found...'
    print('Loaded successfully')


if __name__ == "__main__":
    json = {'user': 'sam'}
    assert_function(data=json)
    print(__debug__)
