from marshmallow import Schema, fields

class LessonSchema(Schema):
    __tablename__ = "lesson"

    id = fields.Int()
    type = fields.Str()
    price = fields.Decimal()