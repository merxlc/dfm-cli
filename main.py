from requests import Session
from src.answer_handler import AnswerHandler
import time
import sys

if len(sys.argv) == 1:
    print('USAGE:')
    print('  python main.py [number of questions] [start url] [time delay]')
    print('  NOTE: the program will not make any checks to ensure the inputs you put in are valid. It is up to the user to ensure this, and the creator holds no liability if you are banned.')
    sys.exit(1)

session = Session()

with open('credentials', 'r') as file:
    lines = file.read().splitlines()
    email = lines[0]
    password = lines[1]

if email == '[YOUR EMAIL]':
    email = input('Enter email: ')
if password == '[YOUR PASSWORD]':
    password = input('Enter password: ')

login_url = "https://www.drfrostmaths.com/process-login.php?url="
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
}
data = {
    'login-email': email,
    'login-password': password
}
session.post(login_url, headers=headers, data=data)

handler = AnswerHandler(session)
url = sys.argv[2]

QUESTIONS = int(sys.argv[1])

for q in range(1, QUESTIONS+1):
    answer, qnum = handler.answer_question_V4_part1(url)
    res, err = handler.answer_question_V4_part2()
    print('sleeping:')
    time.sleep(int(sys.argv[3]))