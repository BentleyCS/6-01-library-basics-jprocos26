import HW_6_01 as HW

def test_process_expenses():
    assert HW.process_expenses([100, 200]) == [115.0, 230.0]
    assert HW.process_expenses([50, 100, 150]) == [57.5, 115.0, 172.5]

def test_sanitize_usernames():
    assert HW.sanitize_usernames(["  Alice  ", "BOB"]) == ["alice", "bob"]
    assert HW.sanitize_usernames(["  John ", "  MARY  ", "tom"]) == ["john", "mary", "tom"]

def test_identify_outliers():
    assert HW.identify_outliers([50, 150, 80, 200]) == [150, 200]
    assert HW.identify_outliers([90, 95, 101, 120, 99]) == [101, 120]

