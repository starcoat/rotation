import rotation

def test_playground():
    pg_test = rotation.Playground(8, (7,5))
    assert pg_test.__str__() == '########\n#      #\n#      #\n#      #\n#      #\n#      #\n#      #\n##### ##\n'