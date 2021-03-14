import re

email = 'someone@geekbrains.ru'
msg = 'wrong email: ' + email


def email_parse(email_address):
    result = {}

    check_mail_re = re.compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    if check_mail_re.match(email_address):
        user_name_re = re.compile(r'\w*@')
        domain_re = re.compile(r'@''\w*''.''\w*')
        user_name = user_name_re.sub('', email)
        domain = domain_re.sub('', email)
        result['username'] = user_name
        result['domain'] = domain
        print(result)
    else:
        raise ValueError(msg)


email_parse(email)
