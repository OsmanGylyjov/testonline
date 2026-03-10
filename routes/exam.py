from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Question, Result

exam_bp = Blueprint('exam', __name__)

@exam_bp.route('/dashboard')
@login_required
def dashboard():
    # Fetch all previous exam results for the logged-in user
    history = Result.query.filter_by(user_id=current_user.id).all()
    return render_template('exam/dashboard.html', history=history)

@exam_bp.route('/test', methods=['GET', 'POST'])
@login_required
def test_window():
    questions = Question.query.all()
    
    if request.method == 'POST':
        score = 0
        # Loop through questions to check answers submitted via the form
        for q in questions:
            user_answer = request.form.get(f"question_{q.id}")
            if user_answer == q.correct_answer:
                score += 1
        
        # Save the attempt to the database
        new_result = Result(
            score=score, 
            total_questions=len(questions), 
            user_id=current_user.id
        )
        db.session.add(new_result)
        db.session.commit()
        
        flash(f'Exam submitted! You scored {score}/{len(questions)}')
        return redirect(url_for('exam.dashboard'))
        
    return render_template('exam/test_window.html', questions=questions)