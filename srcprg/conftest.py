import pytest

from srcprg.authentication.models import User
from srcprg.driver.models import Driver


@pytest.fixture
def new_user(db):
    user = User.objects.create(
        name='Plautz',
        email='plautz@email.com',
        cpf='30172152968',
    )
    return user


@pytest.fixture
def new_driver(db):
    driver = Driver.objects.create(
        nome='Plautz',
        data_nasc='1958-10-01',
        email='plautz@email.com',
        cpf='30172152968',
        telefone='41996514346',
        cnh='112345678901',
        endereco='Castro Alves, 820',
        bairro='Agua Verde',
        cidade='Curitiba',
        estado='Parana',
        cep='80240270',
    )
    return driver
