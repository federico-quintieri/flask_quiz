from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    login = fields.Str()
    nickname = fields.Str()
    score = fields.Int()

class QuizSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str()
    answer_a = fields.Str()
    answer_b = fields.Str()
    answer_c = fields.Str()
