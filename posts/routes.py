from flask import Blueprint, render_template, redirect, url_for, flash, request, get_flashed_messages
from models import Post, db
from forms import PostForm, EditPost
from flask_login import login_required, current_user

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():

    return redirect(url_for('view_posts'))

@posts_bp.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():

    form = PostForm()

    if form.validate_on_submit():

        new_post = Post(name_post=form.name_post.data,
                        post=form.post.data,
                        date=form.date.data,
                        category=form.category.data,
                        admin_id=current_user.id)
        
        db.session.add(new_post)
        db.session.commit()

        flash('Your post has been added succesfully.')

        return redirect(url_for('posts.view_post'))

    return render_template('layouts/partials/add_post.html', form=form)

@posts_bp.route('/view_post', methods=['GET', 'POST'])
@login_required
def view_post():

    messages = get_flashed_messages()
    posts = Post.query.filter_by(admin_id=current_user.id).all()
    return render_template('layouts/partials/view_post.html', posts=posts, messages=messages)

@posts_bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)
    form = EditPost(request.form, obj=post)
    
    if form.validate_on_submit():
        
        form.populate_obj(post)
        db.session.commit()
        flash('Your product has been uptades succesfully.')
        return redirect(url_for('posts.edit_post', post_id=post_id))
    
    return render_template('layouts/partials/edit_post.html', form=form, post=post)

@posts_bp.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):

    if request.method == 'POST':
    
        post = Post.query.get_or_404(post_id)
    
        db.session.delete(post)    
        db.session.commit()
        flash('The post has been deleted succesfully.')
    
    return redirect(url_for('posts.view_post'))

