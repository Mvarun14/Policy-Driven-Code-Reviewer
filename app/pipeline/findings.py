class Finding:
    def __init__(self, category, subtype, severity, fix_scope, message, context=None):
        self.category = category
        self.subtype = subtype
        self.severity = severity
        self.fix_scope = fix_scope
        self.message = message
        self.context = context or {}
