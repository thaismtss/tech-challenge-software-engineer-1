from app.domain import peoples, youngers, olders, gender_distribution, get_people, blood_types, people_search


def test_peoples_youngers():
    peoples_youngers = youngers(2)
    list_dn = []
    for dn in peoples_youngers:
        list_dn.append(dn.get("data_nasc"))
    assert list_dn == ['2002-04-22', '2001-08-19']


def test_peoples_olders():
    peoples_olders = olders(2)
    list_dn = []
    for dn in peoples_olders:
        list_dn.append(dn.get("data_nasc"))
    assert list_dn == ['1942-05-14', '1943-04-13']


def test_get_distribution():
    porct = gender_distribution()
    assert dict(porct) == {'Feminino': '53.3%', 'Masculino': '46.7%'}


def test_get_people():
    people = get_people('957.474.484-12')
    for name in people:
        assert name.get('nome') == 'Carolina Bárbara Vieira'


def test_blood_type():
    blood_type = blood_types()
    assert blood_type.get("A+") == "1"


def test_list_people():
    peoples_list = peoples()
    assert peoples_list[0] == "Anthony Lucas Bento Gomes"
    assert peoples_list[-1] == "Vitória Isis Moreira"


def test_people_search_by_name():
    people = people_search("Vitória")
    for name in people:
        assert name.get("nome") == "Vitória Isis Moreira"
