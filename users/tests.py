import pytest
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_custom_user_creation_form_valid_data():
    form = CustomUserCreationForm(data={
        'email': 'testuser@example.com',
        'username': 'testuser123',
        'password1': 'complexpassword123',
        'password2': 'complexpassword123'
    })
    assert form.is_valid()
    form.save()

    user = get_user_model().objects.get(username='testuser123')
    assert user.email == 'testuser@example.com'
    assert user.username == 'testuser123'

@pytest.mark.django_db
def test_custom_user_creation_form_invalid_password():
    form = CustomUserCreationForm(data={
        'username': 'testuser123',
        'email': 'testuser@example.com',
        'password1': 'complexpassword123',
        'password2': 'complexinvalidpassword123'
    })
    assert not form.is_valid()
    assert 'password2' in form.errors

@pytest.mark.django_db
def test_custom_user_creation_form_missing_fields():
    form = CustomUserCreationForm(data={
        'username': 'testuser123',
        'password1': 'complexpassword123',
        'password2': 'complexpassword123'
    })
    assert not form.is_valid()
    assert 'email' in form.errors

@pytest.fixture
def test_user(db):
    return get_user_model().objects.create(
        email='testuser@example.com',
        username='testuser123',
        password='complexpassword123'
    )


@pytest.mark.django_db
def test_user_change_form_valid(test_user):
    form = CustomUserChangeForm(instance=test_user, data={
        'username': 'updatetestuser123',
        'email': 'updatetestuser@example.com',
    })
    assert form.is_valid()

    form.save()
    test_user.refresh_from_db()
    assert test_user.email == 'updatetestuser@example.com'
    assert test_user.username == 'updatetestuser123'


@pytest.mark.django_db
def test_user_change_form_invalid_email(test_user):
    form = CustomUserChangeForm(instance=test_user, data={
        'email': 'updatetestuser',
    })
    assert not form.is_valid()
    assert 'email' in form.errors