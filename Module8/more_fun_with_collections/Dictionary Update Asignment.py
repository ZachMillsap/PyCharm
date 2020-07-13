def get_test_scores():
    scores_dict = {}

    num_scores = int(input("Enter number of scores you want to enter:"))
    for i in range(num_scores):
        test = input("Enter your test")
        scores = input("Enter the scores:")
        scores_dict.update({test:scores})
    return num_scores



def average_scores(num_scores):
   sum_of_scores = 0
   num_scores = len(scores_dict)
   for value in scores_dict.values():
       sum_of_scores += value
   average_scores = sum_of_scores/num_scores
   return average_scores

if __name__ == "__main__":
    scores_dict = {}
    scores=0
    get_test_scores()
    average_score = average_scores(num_scores)
