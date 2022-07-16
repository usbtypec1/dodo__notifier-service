import httpx

import config
import views

__all__ = (
    'Telegram',
    'send_message',
)


class Telegram:

    def __init__(self, token: str):
        self._token = token
        self._api_base_url = f'https://api.telegram.org/bot{self._token}'

    def send_message(self, chat_id: int | str, text: str) -> bool:
        """Send message to telegram.

        Args:
            chat_id: chat id to send (telegram id or username).
            text: message to send.

        Returns:
            True if ok.
        """
        response = httpx.post(
            url=f'{self._api_base_url}/sendMessage',
            json={
                'text': text,
                'chat_id': chat_id,
                'parse_mode': 'html',
            }
        )
        return response.json()['ok']


def send_message(chat_id: int | str, message_view: views.MessageView) -> bool:
    """Send message to telegram

    Args:
        chat_id: chat id or username.
        message_view: report message

    Returns:
        True on success.
    """
    bot = Telegram(config.TELEGRAM_BOT_TOKEN)
    return bot.send_message(chat_id, message_view.as_text())