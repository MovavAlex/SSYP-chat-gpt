from sqlalchemy.ext.asyncio import AsyncSession

from date_base.models.Used_promo_code import Used_promo_code


from .abstract import Repository


class UsedPromoCodeRepo(Repository[Used_promo_code]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Used_promo_code, session=session)

    async def new(
        self,
        id: int,
        telegram_id: int,
        promo_code: str
    ) -> Used_promo_code:

        new_used_promo_code = await self.session.merge(
            Used_promo_code(
                id=id,
                telegram_id=telegram_id,
                promo_code=promo_code
            )
        )
        return new_used_promo_code