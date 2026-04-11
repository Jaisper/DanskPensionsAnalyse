from dansk_pensionsanalyse.privacy import sanitize_text


def test_redacts_cpr_email_and_phone():
    text = "Jesper Hansen, cpr 120390-1234, mail jesper@example.com, tlf 12 34 56 78"
    payload = sanitize_text(text)

    assert "120390-1234" not in payload.sanitized_text
    assert "jesper@example.com" not in payload.sanitized_text
    assert "12 34 56 78" not in payload.sanitized_text
    assert "[CPR_REDACTED]" in payload.sanitized_text
    assert "[EMAIL_REDACTED]" in payload.sanitized_text
    assert "[PHONE_REDACTED]" in payload.sanitized_text
