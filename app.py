import json
import schedulers

with open('./process.json') as proc_file:
  procs = json.load(proc_file)

for proc in procs:
  proc['started'] = 0
  proc['terminated'] = 0
  proc['wait'] = 0

queue = []
current = None
time = 0
while True:
  print('t={}'.format(time))

  # HRRN을 위해서 대기시간 구하기
  for proc in queue:
    proc['wait'] = time - proc['arrival']

  # 도착 프로세스 확인
  arrived = [proc for proc in procs if proc['arrival'] == time]
  arrived = sorted(arrived, key=lambda k: k['id']) 
  queue += arrived

  # 종료 프로세스 확인
  if current: 
    if current['execution'] + current['started'] == time:
      print('p{} terminated'.format(current['id']))
      current['terminated'] = time
      current = None

  # 현재 프로세스 확인
  if not current:
    try:
      # current = schedulers.first_in_first_out(queue)
      # current = schedulers.shortest_job_first(queue)
      current = schedulers.highest_response_ration_next(queue)
    except:
      break
    print('p{} started'.format(current['id']))
    current['started'] = time

  time += 1

print('\n=== results ===')
awt = 0
att = 0
for proc in procs:
  print('#p{}'.format(proc['id']), end='')
  wt = proc['started'] - proc['arrival']
  print(', wait time: {}'.format(wt), end='') # 대기 시간
  tt = proc['terminated'] - proc['arrival']
  print(', termination time: {}'.format(tt)) # 반환 시간
  awt += wt
  att += tt
awt /= len(procs)
att /= len(procs)
print('\nAWT: {}\nATT: {}'.format(awt, att))
