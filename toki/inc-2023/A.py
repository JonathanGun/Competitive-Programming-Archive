n, m, k = map(int, input().split())

top_team_per_uni = {}
golden_tickets = []
for i in range(n):
    team, uni = input().split()
    if uni not in top_team_per_uni:
        top_team_per_uni[uni] = team
    if i >= m and k > 0:
        if team == top_team_per_uni[uni]:
            golden_tickets.append(team)
            k -= 1

print(len(golden_tickets))
for team in golden_tickets:
    print(team)
