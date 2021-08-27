import rotation


pg_test1 = rotation.Playground(8, (7,5))

pg_test2 = rotation.Playground(7, (6,3))
pg_test2.add_stick(rotation.Stick('0', [(2,2),(3,2),(4,2),(5,2)]))

pg_test3 = rotation.Playground(10, (3,9))
pg_test3.add_stick(rotation.Stick('0', [(1,1),(1,2)]))
pg_test3.add_stick(rotation.Stick('1', [(1,3),(2,3),(3,3)]))
pg_test3.add_stick(rotation.Stick('2', [(8,8),(7,8),(6,8),(5,8)]))
pg_test3.add_stick(rotation.Stick('3', [(4,8),(4,7),(4,6),(4,5),(4,4),(4,3)]))

pg_test4 = rotation.Playground(8, (7,3))
pg_test4.add_stick(rotation.Stick('0', [(1,6),(2,6)]))
pg_test4.add_stick(rotation.Stick('1', [(3,1),(3,2)]))
pg_test4.add_stick(rotation.Stick('2', [(3,3),(3,4),(3,5),(3,6)]))
pg_test4.add_stick(rotation.Stick('3', [(4,1),(4,2)]))
pg_test4.add_stick(rotation.Stick('4', [(4,6),(5,6),(6,6)]))
pg_test4.add_stick(rotation.Stick('5', [(5,1),(5,2)]))
pg_test4.add_stick(rotation.Stick('6', [(6,1),(6,2),(6,3)]))


def test_playground1():
    assert pg_test1.__str__() == \
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
    assert pg_test2.__str__() == """\
#######
#     #
# 0   #
# 0   #
# 0   #
# 0   #
### ###
"""

def test_playground3():
    assert pg_test3.__str__() == """\
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

def test_playground4():
    assert pg_test4.__str__() == """\
########
#     0#
#     0#
#112222#
#33   4#
#55   4#
#666  4#
### ####
"""

def test_rotate1():
    pg_test1.rotate('CW')
    assert pg_test1.__str__() == """\
########
#      #
#      #
#      #
#      #
       #
#      #
########
"""

def test_rotate2():
    pg_test2.rotate('CCW')
    assert pg_test2.__str__() == """\
#######
#     #
#     #
#      
# 0000#
#     #
#######
"""

def test_rotate3():
    pg_test3.rotate('CCW')
    pg_test3.rotate('CCW')
    assert pg_test3.__str__() == """\
##########
#2       #
#2       #
#2       #
#2       #
#333333  #
      1  #
#     1  #
#     100#
##########
"""

def test_rotate4():
    pg_test4.rotate('CW')
    assert pg_test4.__str__() == """\
########
#6531  #
#6531  #
 6  2  #
#   2  #
#   2  #
#444200#
########
"""

fd_test1 = rotation.Playground(5, (0,1))
fd_test1.add_stick(rotation.Stick('0', [(1,2)]))

def test_falldown1():
    fd_test1.fall_down()
    assert fd_test1.__str__() == """\
#####
#   #
#   #
# 0 #
#####
"""