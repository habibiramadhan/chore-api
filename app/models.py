from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date, Enum, CheckConstraint, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import date

class TransactionCategory(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    transactions = relationship('Transaction', backref="users")

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    date = Column(Date, default=date.today)
    name = Column(String, nullable=False)
    category = Column(Enum(TransactionCategory), index=True, nullable=False)
    description = Column(String)
    nominal = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('nominal > 0', name='check_nominal_gt_zero'),
    )

# Agent
class LLM(Base):
    __tablename__ = 'llm'

    llm_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String, nullable=False)
    model = Column(String, nullable=False)
    temperature = Column(Float, default=1.0)
    pgsearchtools = relationship('PGSearchTool', backref="llm")

# RAG Tools
class Embedder(Base):
    __tablename__ = 'embedder'

    embedder_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String, nullable=False)
    model = Column(String, nullable=False)
    pgsearchtools = relationship('PGSearchTool', backref="embedder")

class Vectordb(Base):
    __tablename__ = 'vectordb'

    vectordb_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String, nullable=False)
    collection_name = Column(String, nullable=False)
    dir_name = Column(String, nullable=False)
    is_allow_reset = Column(Boolean, default=True)
    pgsearchtools = relationship('PGSearchTool', backref="vectordb")

class PGSearchTool(Base):
    __tablename__ = 'pg_search_tool'

    tool_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    table_name = Column(String, nullable=False)
    llm_id = Column(UUID(as_uuid=True), ForeignKey('llm.llm_id'))
    embedder_id = Column(UUID(as_uuid=True), ForeignKey('embedder.embedder_id'))
    vectordb_id = Column(UUID(as_uuid=True), ForeignKey('vectordb.vectordb_id'))