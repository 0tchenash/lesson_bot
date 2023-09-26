from marshmallow import Schema, fields

class LessonsBaseSchema(Schema):
    id = fields.Int()
    time = fields.Str()
    total_price = fields.Decimal()
    user_id = fields.Int()
    lesson_id = fields.Int()

class ScheduleSchema(Schema):
    id = fields.Int()
    time = fields.Str()
    total_price = fields.Decimal()
    user_id = fields.Int()
    lesson_time = fields.Str()
    day_name = fields.Str()
    lesson_id = fields.Int()
    day_id = fields.Int()
    type = fields.Str()
    price = fields.Decimal()