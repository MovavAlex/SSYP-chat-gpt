from dataclasses import dataclass

from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from Project.date_base.models.base import Base


@dataclass
class Used_promo_code(Base):
    __tablename__ = 'used_promo_codes'

    id: Mapped[int] = mapped_column(INTEGER,
                                    unique=True,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True
                                    )

    telegram_id: Mapped[int] = mapped_column(INTEGER,
                                             unique=False,
                                             nullable=False
                                             )

    promo_code: Mapped[str] = mapped_column(VARCHAR(10),
                                            unique=False,
                                            nullable=False
                                            )

    def __str__(self) -> str:
        return f"<used_promo_code: {self.id}"
