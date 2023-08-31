from marshmallow import Schema, fields

class DaysSchema(Schema):

    id = fields.Int()
    lesson_date = fields.Str()
    day_name = fields.Str()
    is_works = fields.Boolean()