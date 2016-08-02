import os

from dateutil.rrule import rrule, MONTHLY, TU
from dateutil.parser import parse as dateutil_parse

from fabric.utils import abort
from fabric.api import task, prompt


@task
def new_meeting():
    with open('_templates/meeting.txt.tpl', 'r') as f:
        meeting_template = f.read()

    date_prompt = dateutil_parse(prompt('Date'))
    title_prompt = prompt('Title')

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
