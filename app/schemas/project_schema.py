from marshmallow import Schema, fields

class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    status = fields.Str()
    created_at = fields.DateTime()
