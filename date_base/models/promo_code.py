from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import INTEGER, VARCHAR, DATE
from sqlalchemy.orm import mapped_column, Mapped

from Project.date_base.models.base import Base


@dataclass
class PromoCodes(Base):
    __tablename__ = 'promo_codes'

    # Code
    code: Mapped[str] = mapped_column(VARCHAR(10),
                                      unique=True,
                                      nullable=False,
                                      primary_key=True
                                      )

    # Token
    token: Mapped[int] = mapped_column(INTEGER,
                                       unique=False,
                                       nullable=False
                                       )
    # End_date_time
    end_date_time: Mapped[datetime] = mapped_column(DATE,
                                                    unique=False,
                                                    nullable=False
                                                    )



    def __str__(self) -> str:
        return f"<promo_code: {self.code}"
