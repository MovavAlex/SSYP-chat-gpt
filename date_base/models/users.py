from dataclasses import dataclass

from sqlalchemy import BigInteger, INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from Project.date_base.models.base import Base
from Project.structures.enums.Role import Role


@dataclass
class Users(Base):
    __tablename__ = 'users'
    # Telegram ID
    user_id: Mapped[int] = mapped_column(BigInteger,
                                         unique=True,
                                         nullable=False,
                                         primary_key=True
                                         )

    # Telegram user client game
    user_name: Mapped[int] = mapped_column(VARCHAR(64),
                                           unique=True,
                                           nullable=False

                                           )
    # Telegram first name
    first_name: Mapped[int] = mapped_column(VARCHAR(64),
                                            unique=True,
                                            nullable=False

                                            )
    # Telegram second name
    second_name: Mapped[str] = mapped_column(VARCHAR(64),
                                             unique=False,
                                             nullable=False
                                             )
    # Telegram role
    role: Mapped[Role] = mapped_column(INTEGER,
                                       unique=False,
                                       nullable=False,
                                       default=Role.user
                                       )
    # Telegram ID by whom the users was invited
    referall_id: Mapped[int] = mapped_column(BigInteger,
                                             unique=False,
                                             nullbase=True
                                             )

    def __str__(self) -> str:
        return f"<user: {self.user_id}"
