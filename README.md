# Computer Science Process Schedulers
**컴퓨터 시스템 일반** 탐구 활동 - 프로세스 스케줄러 구현하기

## Usage
`./process.json`에 아래와 같이 실행할 프로세스 목록을 저장합니다.

```json
[
  { "id": 0, "arrival": 0, "execution": 9 },
  { "id": 1, "arrival": 1, "execution": 6 },
  { "id": 2, "arrival": 2, "execution": 2 },
  { "id": 3, "arrival": 3, "execution": 4 }
]
```

위에서 각각 `id`는 프로세스 번호, `arrival`은 도착 시간, `execution`은 실행(처리) 시간을 뜻합니다.

## FIFO (First In First Out)
```
t=0
p0 started
t=1
t=2
t=3
t=4
t=5
t=6
t=7
t=8
t=9
p0 terminated
p1 started
t=10
t=11
t=12
t=13
t=14
t=15
p1 terminated
p2 started
t=16
t=17
p2 terminated
p3 started
t=18
t=19
t=20
t=21
p3 terminated

=== results ===
#p0, wait time: 0, termination time: 9
#p1, wait time: 8, termination time: 14
#p2, wait time: 13, termination time: 15
#p3, wait time: 14, termination time: 18

AWT: 8.75
ATT: 14.0
```

## SJF (Shortest Job First)
```
t=0
p0 started
t=1
t=2
t=3
t=4
t=5
t=6
t=7
t=8
t=9
p0 terminated
p2 started
t=10
t=11
p2 terminated
p3 started
t=12
t=13
t=14
t=15
p3 terminated
p1 started
t=16
t=17
t=18
t=19
t=20
t=21
p1 terminated

=== results ===
#p0, wait time: 0, termination time: 9
#p1, wait time: 14, termination time: 20
#p2, wait time: 7, termination time: 9
#p3, wait time: 8, termination time: 12

AWT: 7.25
ATT: 12.5
```
