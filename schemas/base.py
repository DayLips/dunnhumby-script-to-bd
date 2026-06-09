from pydantic import BaseModel, field_validator

class BaseSchema(BaseModel):
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if isinstance(v, str) and (v == '' or v.isspace()):
            return None
        
        if isinstance(v, str):
            v_stripped = v.strip()
            if v_stripped.lower() in ('none', 'unknown', 'null', 'n/a', 'na', '—', '?', '-', 'undefined', 'none/unknown'):
                return None
        
        return v

    class Config:
        from_attributes = True