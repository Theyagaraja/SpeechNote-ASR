from app.text_processing import (
    extract_keywords,
    normalize_text,
    sentence_count,
    summarize_statistics,
    word_count,
)


def test_normalize_text():
    assert normalize_text("  hello   world \n test ") == "hello world test"


def test_word_count():
    assert word_count("Speech recognition is useful.") == 4


def test_sentence_count():
    assert sentence_count("Hello world. This is a test!") == 2


def test_extract_keywords_excludes_stop_words():
    keywords = extract_keywords("speech speech recognition recognition system")
    assert keywords[:2] == ["speech", "recognition"]
    assert "the" not in keywords


def test_statistics():
    result = summarize_statistics("Speech recognition works.")
    assert result["words"] == 3
    assert result["sentences"] == 1
