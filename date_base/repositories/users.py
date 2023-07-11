from sqlalchemy.ext.asyncio import AsyncSession
from structures.enums import Role
from date_base.models.users import Users


from .abstract import Repository


class UserRepo(Repository[Users]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Users, session=session)

    async def new(
        self,
        user_id: int,
        user_name: int,
        first_name: int,
        second_name: str,
        refferal_id: int,
        role: Role

    ) -> Users:
        new_users = await self.session.merge(
            Users(
                user_id=user_id,
                user_name=user_name,
                first_name=first_name,
                second_name=second_name,
                refferal_id=refferal_id,
                role=role
            )
        )
        return new_users