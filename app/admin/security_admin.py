from typing import Optional

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.config.database import SessionLocal
from app.config.settings import admin_login, admin_password


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        """
        Обработка входа пользователя.
        """
        form = await request.form()
        username, password = form["username"], form["password"]

        if username in admin_login and password == admin_password:
            # Обновление сессии
            request.session.update(
                {"token": "...", "username": username, "group": "admin"}
            )
            return True

    async def logout(self, request: Request) -> bool:
        """
        Обработка выхода пользователя.
        """
        # Очистка сессии
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        """
        Аутентификация пользователя.
        """
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)


authentication_backend = AdminAuth(secret_key="...")
