from marshmallow import Schema, fields

class LessonsBaseSchema(Schema):
    id = fields.Int()
    time = fields.Str()
    total_price = fields.Decimal()
    user_id = fields.Int()
    lesson_id = fields.Int()