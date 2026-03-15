from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.sql import func

from db.session import Base


class ClinicalIntakeRecord(Base):
    __tablename__ = "clinical_intake_records"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(Text, nullable=False)
    normalized_text = Column(Text, nullable=False)
    extracted_json = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
