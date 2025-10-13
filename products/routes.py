from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages
from forms import ProductForm, EditProduct
from models import Product, db
from flask_login import login_required, current_user


products_bp = Blueprint('products', __name__, url_prefix='/products')

products_bp.route('/products', methods=['GET', 'POST'])
@login_required
def products():

    return redirect(url_for('view_products'))

@products_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():

    form = ProductForm()

    if form.validate_on_submit():

        new_product = Product(name_product=form.name_product.data,
                              price=form.price.data,
                              description=form.description.data,
                              category=form.category.data,
                              admin_id=current_user.id)
        
        db.session.add(new_product)
        db.session.commit()

        flash('Your product has been added succesfully.')

        return redirect(url_for('products.view_products'))

    return render_template('layouts/partials/add_product.html', form=form)

@products_bp.route('/view_products', methods=['GET', 'POST'])
@login_required
def view_products():

    messages = get_flashed_messages()
    products = Product.query.filter_by(admin_id=current_user.id).all()
    return render_template('layouts/partials/view_products.html', products=products, messages=messages)

@products_bp.route('/edit_products/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_products(product_id):

    product = Product.query.get_or_404(product_id)
    form = EditProduct(request.form, obj=product)
    
    if form.validate_on_submit():
        
        form.populate_obj(product)
        db.session.commit()
        flash('Your product has been uptades succesfully.')
        return redirect(url_for('products.edit_products', product_id=product_id))
    
    return render_template('layouts/partials/edit_product.html', form=form, product=product)

@products_bp.route('/delete_product/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):

    if request.method == 'POST':
    
        product = Product.query.get_or_404(product_id)
    
        db.session.delete(product)    
        db.session.commit()
        flash('The product has been deleted succesfully')
    
    return redirect(url_for('products.view_products'))

