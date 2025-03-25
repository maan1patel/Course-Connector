# functions/discussion_functions.py
from models import db
from models.discussion import DiscussionMessage
from flask import jsonify

def post_message(group_id, user_id, message):
    msg = DiscussionMessage(group_id=group_id, user_id=user_id, message=message)
    db.session.add(msg)
    db.session.commit()
    return jsonify({"message": "Message posted successfully"}), 201

def get_messages(group_id):
    messages = DiscussionMessage.query.filter_by(group_id=group_id).all()
    return jsonify([{"id": m.id, "user_id": m.user_id, "message": m.message} for m in messages])
