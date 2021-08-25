import rotation

def test_playground1():
    pg_test = rotation.Playground(8, (7,5))
    assert pg_test.__str__() == \
        """\
########
#      #
#      #
#      #
#      #
#      #
#      #
##### ##
"""

def test_playground2():
    pg_test = rotation.Playground(7, (6,3))
    pg_test.add_stick(rotation.Stick('0', [(2,2),(3,2),(4,2),(5,2)]))
    assert pg_test.__str__() == """\
#######
#     #
# 0   #
# 0   #
# 0   #
# 0   #
### ###
"""

def test_playground3():
    pg_test = rotation.Playground(10, (3,9))
    pg_test.add_stick(rotation.Stick('0', [(1,1),(1,2)]))
    pg_test.add_stick(rotation.Stick('1', [(1,3),(2,3),(3,3)]))
    pg_test.add_stick(rotation.Stick('2', [(8,8),(7,8),(6,8),(5,8)]))
    pg_test.add_stick(rotation.Stick('3', [(4,8),(4,7),(4,6),(4,5),(4,4),(4,3)]))
    assert pg_test.__str__() == """\
##########
#001     #
#  1     #
#  1      
#  333333#
#       2#
#       2#
#       2#
#       2#
##########
"""