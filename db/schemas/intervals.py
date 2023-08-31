from marshmallow import Schema, fields

class IntervalsSchema(Schema):
    id = fields.Int()
    lesson_time = fields.Str()
    is_works = fields.Boolean()
