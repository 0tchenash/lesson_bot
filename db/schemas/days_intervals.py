from marshmallow import Schema, fields

class DaysIntervalsSchema(Schema):

    id = fields.Int()
    day_id = fields.Int()
    interval_id = fields.Int()
    is_works = fields.Boolean()

class IntervalsSchema(Schema):

    id = fields.Int()
    lesson_time = fields.Str()

class DaysSchema(Schema):

    id = fields.Int()
    lesson_date = fields.Str()
    day_name = fields.Str()
    is_works = fields.Boolean()