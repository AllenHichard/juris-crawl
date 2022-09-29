from web import session

cnj = "0710802-55.2018.8.02.0001"
s = session.Session(cnj=cnj)
s.consult_process()
process = s.returned_processes[0]


def test_number_of_query_results():
    assert len(s.results) == 2


def test_class_was_consulted():
    assert process.justice_class is not None


def test_area_was_consulted():
    assert process.area is not None


def test_subject_was_consulted():
    assert process.subject is not None


def test_distribution_date_was_consulted():
    assert process.distribution_date is not None


def test_judge_was_consulted():
    assert process.judge is not None


def test_action_value_was_consulted():
    assert process.action_value is not None


def test_parts_was_consulted():
    assert len(process.parts) > 0


def test_movements_was_consulted():
    assert len(process.movements) > 0
