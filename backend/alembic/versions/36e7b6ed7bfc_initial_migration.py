"""initial migration

Revision ID: 36e7b6ed7bfc
Revises: 
Create Date: 2025-08-04 19:59:09.185101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36e7b6ed7bfc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Base schema for a fresh database. Later migrations evolve columns/types.
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Integer(), nullable=True),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )

    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('author_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    )

    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('author_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('priority', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('assigned_to', sa.Integer(), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False),
    )

    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.UniqueConstraint('name'),
    )

    op.create_table(
        'task_tags',
        sa.Column('task_id', sa.Integer(), sa.ForeignKey('tasks.id'), nullable=False),
        sa.Column('tag_id', sa.Integer(), sa.ForeignKey('tags.id'), nullable=False),
    )

    op.create_table(
        'chats',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    )

    op.create_table(
        'chat_messages',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('chat_id', sa.Integer(), sa.ForeignKey('chats.id'), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('chat_messages')
    op.drop_table('chats')
    op.drop_table('task_tags')
    op.drop_table('tags')
    op.drop_table('tasks')
    op.drop_table('projects')
    op.drop_table('users')
