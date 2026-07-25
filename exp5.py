import random
import string

def generate_random_solution(answer):
    return [random.choice(string.printable) for _ in range(len(answer))]

def evaluate(solution, answer):
    diff = 0
    for i in range(len(answer)):
        diff += abs(ord(solution[i]) - ord(answer[i]))
    return diff

def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)
    return solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"

    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)

    while True:
        print("Score:", best_score, "Solution:", "".join(best))

        if best_score == 0:
            break

        new_solution = mutate_solution(best.copy())
        new_score = evaluate(new_solution, answer)

        if new_score < best_score:
            best = new_solution
            best_score = new_score

SimpleHillClimbing()