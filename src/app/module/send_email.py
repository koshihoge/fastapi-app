import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from smtplib import SMTP_SSL
from xmlrpc.client import boolean


def createMIMEText(
    from_email: str,
    to_email: str,
    message: str,
    subject: str,
    filepath: str | None = None,
    filename: str = "",
) -> MIMEMultipart:
    # MIMETextを作成
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Date"] = formatdate()
    msg.attach(MIMEText(message, "plain", "utf-8"))

    # 添付ファイルの設定
    if filepath:
        path = filepath
        with open(path, "r") as fp:
            attach_file = MIMEText(fp.read(), "plain")
            attach_file.add_header("Content-Disposition", "attachment", filename=filename)
            msg.attach(attach_file)
    return msg


def send_email(msg: MIMEMultipart, account: str, password: str, host: str, port: int) -> boolean:
    try:
        # サーバを指定する
        # server = SMTP(host, port)
        context = ssl.create_default_context()
        server = SMTP_SSL(host, port, context=context)

        # Debug情報出力
        server.set_debuglevel(True)

        # ログイン処理
        server.login(account, password)

        # メールを送信する
        server.send_message(msg)

        # 閉じる
        server.quit()

        return True
    except BaseException as e:
        print(e)
        return False


def send_system_mail(
    to_email: str,
    message: str,
    subject: str,
    filepath: str | None = None,
    filename: str = "",
) -> boolean:
    from_email = "xxxx@yyyy.zzz"
    password = "password"
    host = "hostname"
    port = 465

    # MIME形式の作成
    mime = createMIMEText(from_email, to_email, message, subject, filepath, filename)

    # メールの送信
    return send_email(mime, from_email, password, host, port)
