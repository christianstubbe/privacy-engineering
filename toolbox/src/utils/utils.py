import re

# TODO: parse the purpose config from a bucket

# TODO: redact text based on sensitive sequences in the output of a query to a database

# TODO: remove background from profile pictures retrieved from cloud storage solutions


def redact_email(text):
    return re.sub(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "[REDACTED_EMAIL]", text
    )


def redact_phone_number(text):
    return re.sub(r"\b\d{10}\b", "[REDACTED_PHONE]", text)
