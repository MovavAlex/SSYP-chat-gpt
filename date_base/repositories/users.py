from sqlalchemy.ext.asyncio import AsyncSession

from Project.date_base.models import Users


from .abstract import Repository


class PromoCodeRepo(Repository[Users]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Users, session=session)

    async def new(
        self,
        users: str,
        promo_code: str
    ) -> Users:
        new_users = await self.session.merge(
            Users(
                users=users,
                promo_code=promo_code
            )
        )
        return new_users