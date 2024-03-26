from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, Numeric, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_type = Column(Enum("company", "individual"))
    company_name = Column(String(100))
    company_registration_number = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    phone_number = Column(String(20))
    address = Column(String(255))
    preferred_method = Column(Enum("SMS", "email"))
    bank_account_number = Column(String(50))
    blocked = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Transactions(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    transaction_token = Column(Integer, unique=True)
    card_id = Column(Integer)
    alias = Column(String)
    account_number = Column(String)
    wallet_id = Column(String)
    provider_id = Column(String)
    user_id = Column(String)
    status = Column(String(20))
    active = Column(Boolean)
    velocity_limit_window = Column(Enum("Day", "Week", "Month", "Lifetime"))
    velocity_amount_limit = Column(Numeric)
    velocity_issued_amount = Column(Numeric)
    velocity_amount_remaining = Column(Numeric)
    termination_date = Column(DateTime)


class Wallets(Base):
    __tablename__ = "wallets"

    wallet_id = Column(Integer, primary_key=True)
    is_parent = Column(Boolean)
    parent_wallet_id = Column(Integer)
    provider_id = Column(String(50))
    alias = Column(String)
    active = Column(Boolean)
    user_id = Column(String)
    notified_users = Column(ARRAY(String))
    available_balance = Column(Numeric)
    total_balance = Column(Numeric)
    overdrawn = Column(Boolean)
    overdraw_allowance = Column(Numeric)
    low_balance_trigger = Column(Numeric)
    low_spendable_balance_trigger = Column(Numeric)
    authorization_webhook_id = Column(String)
    authorization_default_response = Column(Boolean)
    markup_rate_percentage_rate = Column(Numeric(3, 2))
    markup_rate_flat_rate = Column(Numeric(10, 2))
    markup_rate_amount = Column(Numeric(10, 2))


class Provider(Base):
    __tablename__ = "provider"

    provider_id = Column(Integer, primary_key=True)
    bank_account = Column(String)
    active = Column(Boolean)
    available_balance = Column(Numeric)
    total_balance = Column(Numeric)
    overdrawn = Column(Boolean)
    overdraw_allowance = Column(Numeric)
    low_balance_trigger = Column(Numeric)
    low_spendable_balance_trigger = Column(Numeric)
    bin_set = Column(ARRAY(String))
