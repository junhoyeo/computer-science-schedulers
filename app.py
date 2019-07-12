import json
with open('./process.json') as proc_file:
  procs = json.load(proc_file)

for proc in procs:
  proc['start'] = 0
  proc['delay'] = 0

print(procs)

queue = []
current = None
time = 0
while True:
  print('t={}'.format(time))

  # 도착 프로세스 확인
  arrived = [proc for proc in procs if proc['arrival'] == time]
  arrived = sorted(arrived, key=lambda k: k['id']) 
  queue += arrived

  # 종료 프로세스 확인
  if current: 
    if current['execution'] + current['start'] == time:
      print('p{} terminated'.format(current['id']))
      current = None

  # 현재 프로세스 확인
  if not current:
    try:
      current = queue.pop(0)
    except:
      break
    print('p{} started'.format(current['id']))
    current['start'] = time

  time += 1
