from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    user_name = fields.Str()
    phone_number = fields.Str()
    user_telegram_id = fields.Int()