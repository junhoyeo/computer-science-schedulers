def first_in_first_out(queue):
  return queue.pop(0)

def shortest_job_first(queue):
  proc = sorted(queue, key=lambda k: k['execution'])[0]
  queue.remove(proc)
  return proc

def highest_response_ratio_next(queue):
  def priority(proc):
    return (proc['wait'] + proc['execution']) / proc['execution']
  
  proc = sorted(queue, key=lambda k: priority(k), reverse=True)[0]
  queue.remove(proc)
  return proc
