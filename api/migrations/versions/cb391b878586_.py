"""empty message

Revision ID: cb391b878586
Revises: f349debf9e15
Create Date: 2019-07-02 19:34:33.725020

"""

# revision identifiers, used by Alembic.
revision = 'cb391b878586'
down_revision = 'f349debf9e15'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from app import db

Base = declarative_base()


class InvitationTemplate(Base):
    __tablename__ = "invitation_template"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True)
    event_id = db.Column(db.Integer(), db.ForeignKey("event.id"), nullable=False)
    template_path = db.Column(db.String(), nullable=False)
    send_for_travel_award_only = db.Column(db.Boolean(), nullable=False)
    send_for_accommodation_award_only = db.Column(db.Boolean(), nullable=False)
    send_for_both_travel_accommodation = db.Column(db.Boolean(), nullable=False)

class Event(Base):

    __tablename__ = "event"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    application_forms = db.relationship('ApplicationForm')

    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def set_name(self, new_name):
        self.name = new_name

    def set_description(self, new_description):
        self.description = new_description

    def set_start_date(self, new_start_date):
        self.start_date = new_start_date

    def set_end_date(self, new_end_date):
        self.end_date = new_end_date

    def get_application_form(self):
        return self.application_forms[0]

class ApplicationForm(Base):
    __tablename__ = 'application_form'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    event_id = db.Column(db.Integer(), db.ForeignKey('event.id'), nullable=False)
    is_open = db.Column(db.Boolean(), nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)

    def __init__(self, event_id, is_open, deadline):
        self.event_id = event_id
        self.is_open = is_open
        self.deadline = deadline


def upgrade():
    Base.metadata.bind = op.get_bind()
    session = orm.Session(bind=Base.metadata.bind)

    # Insert the invitation templates
    general_template = InvitationTemplate(
        event_id=1,
        template_path="Indaba 2019  - Invitation Letter - General.docx",
        send_for_travel_award_only=False,
        send_for_accommodation_award_only=False,
        send_for_both_travel_accommodation=False)

    session.add(general_template)
    session.commit()

    both_template = InvitationTemplate(
        event_id=1,
        template_path="Indaba 2019 - Invitation Letter - Travel & Accomodation.docx",
        send_for_travel_award_only=False,
        send_for_accommodation_award_only=False,
        send_for_both_travel_accommodation=True)

    session.add(both_template)
    session.commit()

    travel_only_template = InvitationTemplate(
        event_id=1,
        template_path="Indaba 2019 - Invitation Letter - Travel Only.docx",
        send_for_travel_award_only=True,
        send_for_accommodation_award_only=False,
        send_for_both_travel_accommodation=False)

    session.add(travel_only_template)
    session.commit()

    accommodation_only_template = InvitationTemplate(
        event_id=1,
        template_path="Indaba 2019 - Invitation Letter - Accomodation Only.docx",
        send_for_travel_award_only=False,
        send_for_accommodation_award_only=True,
        send_for_both_travel_accommodation=False)

    session.add(accommodation_only_template)
    session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
