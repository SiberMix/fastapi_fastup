import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_validator import validate_email

from app.config.settings import env



class SenderEmail:
    """
    Отправка сообщений на почту
    """

    def send_email_yandex(self, to: str, text: str, title: str):
        """
        Отправка емайлов через яндекс
        :param to:
        :param password:
        :param gen_login:
        :return:
        """

        smtp_server = os.environ.get("MAIL_HOST")
        smtp_port = os.environ.get("MAIL_PORT")
        email_sender = os.environ.get("MAIL_USER")
        email_password = os.environ.get("MAIL_PASS")
        try:
            emailinfo = validate_email(to, check_deliverability=True, timeout=2)
            msg = MIMEMultipart()
            msg["Subject"] = title
            msg["From"] = email_sender
            msg["To"] = emailinfo.email
            msg.attach(MIMEText(text, "html"))
            server = smtplib.SMTP(smtp_server, smtp_port, timeout=2)
            server.ehlo()
            server.starttls()
            server.login(email_sender, email_password)
            server.sendmail(email_sender, [to], msg.as_string())

            server.quit()
            print(f"Сообщение успешно отправлено на адрес {to}")
            return True

        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
            return False


class Callback:
    """
    API Callback Service
    """
    email_api = SenderEmail()

    def send_to_email(self, to_send, name, phone, email, city_from, city_to, weight, volume, place):
        """
        Отправить callback на почту
        """
        template = env.get_template("email_callback.html")
        text = template.render(
            name=name,
            phone=phone,
            email=email,
            city_from=city_from,
            city_to=city_to,
            weight=weight,
            volume=volume,
            place=place
        )
        result = self.email_api.send_email_yandex(to=to_send, text=text, title="Тиза-Логистик: Заказ обратного звонка с сайта ТИЗА")
        return result
    def send_info_client(self, to_send):
        """
        Отправить письмо клиенту
        """
        template = env.get_template("email_send_client.html")
        text = template.render()
        result = self.email_api.send_email_yandex(to=to_send, text=text, title="Тиза-Логистик: Вы заказали обратный звонок")
        return result