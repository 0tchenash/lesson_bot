from marshmallow import Schema, fields

class DaysIntervalsSchema(Schema):

    id = fields.Int()
    day_id = fields.Int()
    interval_id = fields.Int()
    is_works = fields.Boolean()