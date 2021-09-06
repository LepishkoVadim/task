import csv

import click
from task import models, db, app


@app.cli.command('fill')
@click.argument('model')
@click.argument('filename')
def fill_products(model, filename):
    """Parsing and filling datatable

    Use: flask fill <model> <filename>
    """
    with open(filename, encoding='UTF-8') as csv_file:
        # reading data in DictReader
        reader = csv.DictReader(csv_file)

        if model.lower() == 'products':
            _fill_products(reader)
        elif model.lower() == 'reviews':
            _fill_reviews(reader)
        else:
            raise ValueError('you have chosen the wrong model name!')


def _fill_products(reader):
    """filling in the product model"""
    for row in reader:
        product = models.Product(title=row['Title'], asin=row['Asin'])
        db.session.add(product)

    # saving products in database
    db.session.commit()
    print('done!')


def _fill_reviews(reader):
    """filling in the reviews model"""
    for row in reader:
        product = models.Review(title=row['Title'], asin=row['Asin'], review=row['Review'])
        db.session.add(product)

    # saving products in database
    db.session.commit()
    print('done!')
