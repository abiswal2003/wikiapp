from unittest.mock import Mock

from wikiapp import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    wikipedia.random_page(language="es")
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]

def test_random_page_returns_dictionary() -> None:
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)

def test_random_page_handels_validation_error(mock_requests_get; Mock) -> None:
    mock_requests_gets.return_value.__enter__.return_value.json.return_value = {}
    with pytest.raises(ClickException):
        wikipedia.random_page()
