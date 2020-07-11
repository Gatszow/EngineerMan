import requests
import re

data = requests.get('http://www.mg-cc.org/club-information/club-contacts')

# regex for polish numbers:
# [\d]{3}[\s-]?[\d]{3}[\s-]?[\d]{3}
# regex for american numbers:
# (\(?[0-9]{3}\)?(?:-|\s|\.)?[0-9]{3}[-.][0-9]{4})

phones = re.findall(r'(\(?[0-9]{3}\)?(?:-|\s|\.)?[0-9]{3}[-.][0-9]{4})', data.text)
emails = re.findall(r'([\d\w.]+@[\d\w.\-]+\.\w+)', data.text)

print('Phones:\n{}\n\nEmails:\n{}'.format(phones, emails))
