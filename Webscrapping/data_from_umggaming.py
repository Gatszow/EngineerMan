
import requests
from bs4 import BeautifulSoup
data = requests.get('https://umggaming.com/leaderboards')
print(data)

# soup = BeautifulSoup(data.text, 'html.parser')
# leaderboard = soup.find('div', {'class': 'anf row'})
