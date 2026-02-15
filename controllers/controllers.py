from flask import render_template, request, redirect, session
from models.models import *
from flask_bcrypt import check_password_hash

def app_routes(app, mysql):
    app.secret_key = "your_secret_key"

    @app.route('/')
    def index():
        users = get_all_users(mysql)
        return render_template('index.html', users=users, edit_user=None)
    
    @app.route('/registration')
    def registration():
        users = get_all_users(mysql)
        return render_template('registration.html', users=users, edit_user=None)
    
    @app.route('/home')
    def home():
        users = get_all_users(mysql)
        return render_template('home.html', users=users, edit_user=None)
    
    @app.route('/studentjourney')
    def studentjourney():
        users = get_all_users(mysql)
        return render_template('studentjourney.html', users=users, edit_user=None)
    
    # ✅ Student Profile Page
    @app.route('/studentprofile', methods=['GET', 'POST'])
    def studentprofile():
        users = get_all_users(mysql)

        if request.method == 'POST':
            fullname = request.form['fullname']
            student_number = request.form['student_number']
            email = request.form['email']
            year_level = request.form['year_level']
            program = request.form['program']

            save_student_profile(mysql, fullname, student_number, email, year_level, program)
            return redirect('/student_strengths')

        return render_template('studentprofile.html', users=users, edit_user=None)
    
    # ✅ Student Strengths
    @app.route('/student_strengths', methods=['GET', 'POST'])
    def student_strengths():
        users = get_all_users(mysql)

        if request.method == 'POST':
            required_fields = [
                'programming', 'webdev', 'database', 'oop',
                'mobile', 'networking', 'cyber', 'data', 'cloud', 'support'
            ]
            for field in required_fields:
                if field not in request.form:
                    return render_template(
                        'StudentStrengths.html', users=users, edit_user=None,
                        error="⚠️ Please answer all questions before continuing."
                    )
            return redirect('/student_strengths1')

        return render_template('StudentStrengths.html', users=users, edit_user=None)
    
    # ✅ Student Strengths 1
    @app.route('/student_strengths1', methods=['GET', 'POST'])
    def student_strengths1():
        users = get_all_users(mysql)

        if request.method == 'POST':
            required_fields = [
                'communication', 'team', 'time',
                'adaptability', 'leadership', 'ethic'
            ]
            for field in required_fields:
                if field not in request.form:
                    return render_template(
                        'StudentStrengths1.html', users=users, edit_user=None,
                        error="⚠️ Please complete all fields before continuing."
                    )
            return redirect('/student_strengths2')

        return render_template('StudentStrengths1.html', users=users, edit_user=None)
    
    # ✅ Student Strengths 2 (With Validation)
    @app.route('/student_strengths2', methods=['GET', 'POST'])
    def student_strengths2():
        users = get_all_users(mysql)

        if request.method == 'POST':
            required_fields = [
                'logical', 'algorithm', 'debugging', 'research', 'technical'
            ]
            for field in required_fields:
                if field not in request.form:
                    return render_template(
                        'StudentStrengths2.html', users=users, edit_user=None,
                        error="⚠️ Please complete all fields before continuing."
                    )
            return redirect('/sample')

        return render_template('StudentStrengths2.html', users=users, edit_user=None)
    
    # ✅ Sample Pages
    @app.route('/sample')
    def sample():
        users = get_all_users(mysql)
        return render_template('sample.html', users=users, edit_user=None)
    
    @app.route('/sample1')
    def sample1():
        users = get_all_users(mysql)
        return render_template('sample1.html', users=users, edit_user=None)
    
    @app.route('/results')
    def results():
        users = get_all_users(mysql)
        return render_template('results.html', users=users, edit_user=None)
    
    @app.route('/endcard')
    def endcard():
        users = get_all_users(mysql)
        return render_template('endcard.html', users=users, edit_user=None)
    
    # ✅ Logout
    @app.route('/logout')
    def logout():
        return redirect('/')
    
    # ✅ Register
    @app.route('/register', methods=['POST'])
    def register():
        register_user(mysql, request.form['name'], request.form['email'], request.form['password'], request.form['phone_number'])
        return redirect('/registration')
    
    # ✅ Login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            user = get_user_by_email(mysql, email)
            if user:
                stored_password = user[3]
                if check_password_hash(stored_password, password):
                    session['user_id'] = user[0]
                    session['email'] = user[1]
                    return redirect('/home')
                else:
                    return "Email or password does not match!"
            else:
                return "Email or password does not match!"
        
        return render_template('index.html')


    # @app.route('/add', methods=['POST'])
    # def add_user_route():
    #     create_user(mysql, request.form['name'], request.form['email'], request.form['password'], request.form['phone_number'])
    #     return redirect('/user_table')

    # @app.route('/delete/<int:user_id>')
    # def delete_user_route(user_id):
    #     delete_user(mysql, user_id)
    #     return redirect('/user_table')

    # @app.route('/edit/<int:user_id>')
    # def edit_user_route(user_id):
    #     edit_user = get_user_by_id(mysql, user_id)
    #     users = get_all_users(mysql)
    #     return render_template('user_table.html', users=users, edit_user=edit_user)

    # @app.route('/update/<int:user_id>', methods=['POST'])
    # def update_user_route(user_id):
    #     update_user(mysql, user_id, request.form['name'], request.form['email'])
    #     return redirect('/user_table')
