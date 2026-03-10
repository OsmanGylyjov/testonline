from app import app
from models import db, Question

def seed_database():
    with app.app_context():
        # Check if questions already exist to avoid duplicates
        if Question.query.first() is None:
            q1 = Question(
                text="What is the capital of France?",
                option_a="Berlin", option_b="Madrid", 
                option_c="Paris", option_d="Rome",
                correct_answer="C"
            )
            q2 = Question(
                text="Which language is used for Flask?",
                option_a="Java", option_b="Python", 
                option_c="C++", option_d="JavaScript",
                correct_answer="B"
            )
            q3 = Question(
                text="What does SQL stand for?",
                option_a="Structured Query Language", 
                option_b="Simple Queue Logo", 
                option_c="Strong Quest Logic", 
                option_d="Standard Query List",
                correct_answer="A"
            )
            
            db.session.add_all([q1, q2, q3])
            db.session.commit()
            print("Database seeded with sample questions!")
        else:
            print("Database already has questions.")

if __name__ == '__main__':
    seed_database()