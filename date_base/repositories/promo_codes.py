from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import DATE

from date_base.models.promo_code import PromoCodes

from .abstract import Repository


class PromoCodeRepo(Repository[PromoCodes]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=PromoCodes, session=session)

    async def new(
        self,
        code: str,
        token: int,
        end_date_time: DATE
    ) -> PromoCodes:
        """
        :param promo_code: Promo code
        :param end_time: End time promo code
        """
        new_promo_code = await self.session.merge(
            PromoCodes(
                code=code,
                token=token,
                end_date_time=end_date_time
            )
        )
        return new_promo_code