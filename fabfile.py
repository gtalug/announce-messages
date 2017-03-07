import os
import smtplib
from email.mime.text import MIMEText

from dateutil.rrule import rrule, MONTHLY, TU
from dateutil.parser import parse as dateutil_parse

from fabric.api import task, prompt, local
from fabric.utils import abort, fastprint


@task
def new_meeting():
    with open('_templates/meeting.txt.tpl', 'r') as f:
        meeting_template = f.read()

    date_prompt = dateutil_parse(prompt('Date:'))
    title_prompt = prompt('Title:')

    date = list(rrule(MONTHLY, count=1, byweekday=TU, bysetpos=2,
                      dtstart=date_prompt))[0]

    filepath = 'meetings/{0}.txt'.format(date.strftime('%Y-%m'))

    if os.path.isfile(filepath):
        return abort('Meeting already exists.')

    data = {
        'date': date,
        'title': title_prompt,
        'body': '====\nREPLACE\n===='
    }

    with open(filepath, 'w') as f:
        f.write(meeting_template.format(**data))


@task
def send_meeting():
    date = prompt('Date:', validate=r'(\d{4})-(\d{2})')
    subject = prompt('Subject:')
    email_from = 'hi@gtalug.org'
    email_to = 'announce@gtalug.org'

    filepath = 'meetings/{0}.txt'.format(date)

    local('git pull')

    if not os.path.isfile(filepath):
        return abort('There is no meeting at that date.')

    with open(filepath, 'r') as f:
        msg = MIMEText(f.read())

    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    preview = "{0}".format(msg.as_string())

    fastprint(preview)

    send = prompt('Everything look okay?', validate=r'(yes|no)')

    if send == 'yes':
        s = smtplib.SMTP('127.0.0.1')
        s.sendmail(email_from, [email_to], msg.as_string())
        s.quit()
