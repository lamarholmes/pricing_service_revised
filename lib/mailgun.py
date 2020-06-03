from requests import Response, post
from typing import List
import os


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:
    FROM_TITLE = 'Pricing Service'
    FROM_EMAIL = 'https://api.mailgun.net/v3/sandbox80d4921a04d74a7bb40797ef09af8359.mailgun.org'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = None
        domain = None

        if api_key is None:
            raise MailgunException('Failed to load Mailgun API key.')

        if domain is None:
            raise MailgunException('Failed to load Mailgun domain.')
        response = post(f"{domain}/messages",
                        auth=("api", api_key),
                        data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                              "to": email,
                              "subject": subject,
                              "text": text,
                              "html": html})

        if response.status_code != 200:
            print(response.json())
            raise MailgunException('An error occurred while sending e-mail.')
        return response


