last_name = input("Enter the bowler's last name: ")
score_one = int(input("Enter the bowler's score one: "))
score_two = int(input("Enter the bowler's score two: "))
score_three = int(input("Enter the bowler's score three: "))
handicap = int(input("Enter the bowler's handicap: "))
def calculate_average(score_one, score_two, score_three, handicap):
    average = (score_one + score_two + score_three) / 3
    handicap_cal= (200 - average) * handicap / 100 
    return average + handicap_cal

average = calculate_average(score_one, score_two, score_three, handicap)
print("Bowler's Last Name:", last_name)
print("Bowler's Average Score:", average)
print("Bowler's average score with Handicap:", average + handicap)