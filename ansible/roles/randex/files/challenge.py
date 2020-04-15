#!/usr/bin/env python
import sys
import select
import re
import random
import string
import base64
import os

# Approximate number of challenges required to be solved before sending flag
CHALLENGES = 2000

FLAG = "libctf{ea979622-62cb-43f6-b086-bd75b45172e4}"

def main():
  for i in range(CHALLENGES):
    n = random.random()
    if n < 0.4:
      challenge_randint()
    elif n < 0.991:
      challenge_regex()
    elif n < 0.995:
      # Some trolling, trollololol
      send('https://www.youtube.com/watch?v=2Z4m4lnjxkY')
    else:
      # Introduce some slight variation in total challenges
      continue
  try:
    send(FLAG)
  except:
    send('You got it but I couldn\'t give you the flag, bummer!') 
  sys.exit(0)

def send(s):
  # URL safe base64 encode sent data
  try:
    sys.stdout.write(base64.urlsafe_b64encode(s)+'\n')
    sys.stdout.flush()
  except:
    sys.exit(1)

def receive():
  # Five second timer for user to respond
  rlist, wlist, xlist = select.select([sys.stdin], [], [], 30) #increased timeout from 5s to 30s during bsidescbr ctf
  if rlist:
    try:
      # Expect response to be URL safe base64 encoded
      r = sys.stdin.readline().replace('\n','')
      return base64.urlsafe_b64decode(r)
    except:
      sys.exit(1)
  else:
    sys.exit(1)

def challenge_regex():
  # Send a random regex, expect user to return matching string
  regex = create_regex()
  send('regex:{0}'.format(regex))
  r = receive()
  if not re.match(regex, r):
    sys.exit(1)

def challenge_randint():
  # Send a seed value and a random number sequence, expect user to return the next number in the sequence
  nums = []
  seed = random.randint(1000000000000,99999999999999)
  random.seed(seed)
  nums.append(str(seed))
  for i in range(random.randint(0, 1000)):
    random.randint(0, 9999)
  for i in range(5):
    nums.append(str(random.randint(0, 9999)))
  send('randint:{0}:{1}:{2}:{3}:{4}:{5}:?'.format(nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]))
  r = receive()
  if r != str(random.randint(0, 9999)):
    sys.exit(1)

def create_regex():
  while True:
    regex = ''
    for i in range(random.randint(10,30)):
      regex += get_token()
    try:
      re.compile(regex)
      return regex
    except:
      continue

def get_token():
  n = random.random()
  if n < 0.4:
    return get_char() + get_modifier()
  elif n < 0.8:
    return get_char_class() + get_modifier()
  else:
    return get_or_group() + get_modifier()

def get_char():
  return random.choice(list(string.ascii_letters + string.digits) + ['\d',  '.'])

def get_modifier():
  n = random.random()
  if n < 0.5:
    return ''
  elif n < 0.7:
    return '*'
  elif n < 0.9:
    return '+'
  else:
    return '{%d}' % random.randint(2,11)

def get_char_class():
  ret = '[%s]' if random.random() < 0.7 else '[^%s]'
  n = random.random()
  if n < 0.4:
    return ret % random.choice(['a-z', 'a-zA-Z', '1-9', 'i-r', 'e-j', 'k-r'])
  else:
    amt = random.randint(2,10)
    c = ''
    for i in range(amt):
      c += get_char()
    return ret % c

def get_or_group():
  word1 = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(random.randint(2,12)))
  word2 = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(random.randint(2,8)))
  return '({0}|{1})'.format(word1, word2)
  
if __name__ == '__main__':
  main()
