"""
Account Service

This microservice handles the lifecycle of Accounts
"""
# pylint: disable=unused-import
from flask import jsonify, request, make_response, abort
from service.models import Account
from service.common import status
from . import app


######################################################
# Health Endpoint
######################################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################
# GET INDEX
######################################################
@app.route("/")
def index():
    """Root URL response"""
    return jsonify(
        name="Account REST API Service",
        version="1.0",
    ), status.HTTP_200_OK


######################################################
# CREATE A NEW ACCOUNT
######################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Creates an Account"""
    app.logger.info("Request to create an Account")
    check_content_type("application/json")

    account = Account()
    account.deserialize(request.get_json())
    account.create()
    message = account.serialize()

    return make_response(
        jsonify(message),
        status.HTTP_201_CREATED,
        {"Location": f"/accounts/{account.id}"},
    )


######################################################
# LIST ALL ACCOUNTS
######################################################
######################################################
# LIST ALL ACCOUNTS
######################################################
@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Returns all Accounts"""
    app.logger.info("Processing all records")
    accounts = Account.all()
    results = [account.serialize() for account in accounts]
    return jsonify(results), status.HTTP_200_OK


######################################################
# READ AN ACCOUNT
######################################################
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """Reads an Account"""
    app.logger.info("Request to read an Account with id: %s", account_id)
    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found."
        )
    return account.serialize(), status.HTTP_200_OK


######################################################
# UTILITY FUNCTIONS
######################################################
def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")
    if content_type == media_type:
        return
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )

####################################################
######################################################################
# LIST ALL ACCOUNTS
######################################################################
# READ AN ACCOUNT
######################################################################
# ... place you code here to READ an account ...


######################################################################
# UPDASTING ACCOUNT
######################################################################
######################################################
# UPDATE AN EXISTING ACCOUNT
######################################################
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Updates an Account"""
    app.logger.info("Request to update an Account with id: %s", account_id)

    account = Account.find(account_id)
    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found."
        )

    check_content_type("application/json")

    account.deserialize(request.get_json())
    account.update()

    return account.serialize(), status.HTTP_200_OK

# ... place you code here to UPDATE an account ...


######################################################################
# DELETE AN ACCOUNT
######################################################################

# ... place you code here to DELETE an account ...


########################################################

