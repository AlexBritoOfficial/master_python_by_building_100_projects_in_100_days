from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

if __name__ == "__main__":

    question_bank =  [Question(item["text"], item["answer"]) for item in question_data]
    quiz_brain = QuizBrain(question_list=question_bank)


    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("You've completed the quiz")
    print(f"Your final score was {quiz_brain.user_score}/{len(quiz_brain.question_list)}")