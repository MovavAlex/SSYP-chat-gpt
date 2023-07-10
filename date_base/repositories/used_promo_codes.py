from sqlalchemy.ext.asyncio import AsyncSession

from Project.date_base.models.Used_promo_code import Used_promo_code


from .abstract import Repository


class PromoCodeRepo(Repository[Used_promo_code]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Used_promo_code, session=session)

    async def new(
        self,
        user_id: int,
        promo_code: str
    ) -> Used_promo_code:

        new_used_promo_code = await self.session.merge(
            Used_promo_code(
                user_id=user_id,
                promo_code=promo_code
            )
        )
        return new_used_promo_code