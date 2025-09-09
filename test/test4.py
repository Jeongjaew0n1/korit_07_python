'''
다음 데이터 분석 코드를 작성하시오.
다음 예시와 같이, 여러 후보자에 대한 투표 결과를 집계하는 프로그램을 작성하시오.
사용자는 먼저 후보자의 수를 입력하고, 그에 맞춰 후보자들의 이름을 입력한다.
이후 투표 횟수와 각 투표 결과를 숫자로 입력받아 최종 결과를 딕셔너리에 저장하여 출력하시오.
지시사항:
1.전체 후보자의 수를 사용자로부터 입력받으시오.
2. for 반복문을 사용하여 후보자 수만큼 후보자들의 이름을 입력받고, candidates 리스트에 저장하시오.
3. 각 후보자의 투표 수를 저장할 딕셔너리(votes)를 생성하고, candidates 리스트의 이름을 키로, 초기 투표 수(0)를 값으로 설정하시오.
4. 전체 투표 횟수를 입력받으시오.
5. for 반복문을 사용하여 투표 횟수만큼 사용자로부터 각 투표 결과를 입력받으시오. 입력은 후보자의 순서 번호(1, 2, 3...)로 받으시오.
6. 입력받은 투표 결과에 따라 해당 후보자의 투표 수를 1씩 증가시키시오.
7. 최종적으로 딕셔너리에 저장된 각 후보자의 투표 수를 출력하시오.

실행 예:
후보자 수를 입력하시오 >>> 3
1번째 후보자의 이름을 입력하시오 >>> 김일
2번째 후보자의 이름을 입력하시오 >>> 김이
3번째 후보자의 이름을 입력하시오 >>> 김삼
전체 투표 횟수를 입력하시오 >>> 5
1번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1
2번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 2
3번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1
4번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 3
5번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1
--- 투표 결과 ---
김일: 3표
김이: 1표
김삼: 1표
'''
candidates = []
candidate_count = int(input('후보자 수를 입력하시오 >>> '))

for i in range(candidate_count):
    candidate_name = input(f'{i + 1}번째 후보자의 이름을 입력하시오 >>> ')
    candidates.append(candidate_name)

votes = {}
for i in range(len(candidates)):
    candidate_name = candidates[i]
    votes[candidate_name] = 0

vote_count = int(input('전체 투표 횟수를 입력하시오 >>> '))
for i in range(vote_count):
    candidate_number = ', '.join([f'{i+1}: {candidates[i]}' for i in range(candidate_count)])
    vote_input = int(input(f"{i+1}번째 투표 ({candidate_number}) >>> "))

    if 1 <= vote_input and vote_input <= candidate_count:
        voted_candidate = candidates[vote_input - 1]
        votes[voted_candidate] += 1
    else:
        print(f"잘못된 투표입니다. 현재 후보자의 수는 {candidate_count}명입니다.")

print('--- 투표 결과 ---')
for i in range(len(candidates)):
    candidate_name = candidates[i]
    print(f"{candidate_name}: {votes[candidate_name]}표")


