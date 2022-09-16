from flask import Flask, request
from flask_restful import Api, Resource, abort
from datetime import date
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/database.db"
db = SQLAlchemy(app)


class AccountModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Account {self.id}:{self.manufacturer}>"
    

api = Api(app=app)


def validate(flag,account_id):
    res = AccountModel.query.filter_by(id=account_id).first()
    if flag == 1:
        if not res:
            return abort(404, Message="404 Account not found...")
    if flag == 2:
        if res:
            return abort(409, Message="409 Account is already exist...")

def check_pass(account_id, password):
    res = AccountModel.query.filter_by(id=account_id).first()
    if res.password != password:
        return abort(401, Message="401 Unauthorized user...")

def required():
    if not (request.form.get("manufacturer") and request.form.get("amount")):
        return abort(400, Message="400 Bad Request...")

class Bank(Resource):
    def get(self, account_id, password):
        validate(1,account_id)
        check_pass(account_id, password)
        result = AccountModel.query.filter_by(id=account_id).first()
        return {
            "account_id":result.id,
            "amount": result.amount,
            "year": result.year,
            "password": result.password,
            "manufacturer": result.manufacturer
        }, 200

    def put(self, account_id, password):
        validate(2,account_id)
        required()
        account = AccountModel(id=account_id,
                               amount=request.form.get("amount"),
                               manufacturer=request.form.get("manufacturer"),
                               password=password,
                               year=date.today().year 
                               )
        db.session.add(account)
        db.session.commit()
        return {
            "account_id":account.id,
            "amount": account.amount,
            "year": account.year,
            "password": account.password,
            "manufacturer": account.manufacturer
        }, 200

    def delete(self, account_id, password):
        validate(1, account_id)
        check_pass(account_id, password)
        result = AccountModel.query.filter_by(id=account_id).first()
        db.session.delete(result)
        db.session.commit()
        return {
            "Message": "Successful deleted..."
        }

api.add_resource(Bank, "/account/<int:account_id>/<string:password>")


if __name__ == "__main__":
    app.run(debug=True)