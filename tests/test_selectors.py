import pytest

from program import Descent, Sex
from program.errors import (
    UnsupportedDescentError,
    UnsupportedSexError
)
from program.selectors import (
    get_first_names,
    get_last_names,
    get_sexes
)


class TestFirstNameSelector:
    @pytest.mark.parametrize(
        'descent,sex,expected',
        [
            (Descent.ENGLISH, Sex.MALE, ['Alex', 'John', 'Joseph']),
            (Descent.ENGLISH, Sex.FEMALE, ['Alex', 'Ashley']),
            (Descent.ENGLISH, Sex.UNISEX, ['Alex']),
        ]
    )
    def test_get_first_names(self, descent, sex, expected, mock_first_names):
        first_names = get_first_names(descent, sex)
        assert first_names == expected

    @pytest.mark.parametrize(
        'descent,sex,error',
        [
            (Descent.GERMAN, Sex.MALE, UnsupportedSexError),
            (Descent.FRENCH, Sex.MALE, UnsupportedDescentError)
        ]
    )
    def test_first_names_generating_errors(
        self,
        descent,
        sex,
        error,
        mock_first_names
    ):
        with pytest.raises(error):
            get_first_names(descent, sex)


class TestLastNameSelector:
    @pytest.mark.parametrize(
        'descent,sex,expected',
        [
            (Descent.ENGLISH, Sex.UNISEX, ['Abramson', 'Johnson']),
            (Descent.RUSSIAN, Sex.MALE, ['Ivanov', 'Petrov']),
            (Descent.RUSSIAN, Sex.FEMALE, ['Ivanova', 'Petrova']),
        ]
    )
    def test_get_last_names(self, descent, sex, expected, mock_last_names):
        last_names = get_last_names(descent, sex)
        assert last_names == expected

    @pytest.mark.parametrize(
        'descent,sex,error',
        [
            (Descent.RUSSIAN, None, UnsupportedSexError),
            (Descent.RUSSIAN, Sex.UNISEX, UnsupportedSexError),
            (Descent.FRENCH, Sex.MALE, UnsupportedDescentError),
        ]
    )
    def test_get_last_names_unsopported_sex(
        self,
        descent,
        sex,
        error,
        mock_last_names
    ):
        with pytest.raises(error):
            get_last_names(descent, sex)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (Sex.MALE, [Sex.MALE, Sex.UNISEX]),
        (Sex.FEMALE, [Sex.FEMALE, Sex.UNISEX]),
        (Sex.UNISEX, [Sex.UNISEX])
    ]
)
def test_get_sex_list(test_input, expected):
    sexes = get_sexes(test_input)
    assert set(sexes) == set(expected)