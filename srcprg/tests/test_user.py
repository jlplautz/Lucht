def test_new_user_name(new_user):
    assert new_user.name == 'Plautz'


def test_new_user_cpf(new_user):
    assert new_user.cpf == '30172152968'


def test_new_user_email(new_user):
    assert new_user.email == 'plautz@email.com'
