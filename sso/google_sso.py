from typing import ClassVar, Optional
import httpx
from fastapi_sso.sso.base import DiscoveryDocument, OpenID, SSOBase, SSOLoginError

class GoogleSSO(SSOBase):
    """
    Clase que proporciona inicio de sesión a través de Google OAuth.

    Esta clase extiende SSOBase para implementar el flujo de autenticación de Google,
    utilizando OpenID Connect.
    """

    # URL de descubrimiento de OpenID Connect de Google
    discovery_url = "https://accounts.google.com/.well-known/openid-configuration"
    # Nombre del proveedor
    provider = "google"
    # Alcance predeterminado para la autenticación
    scope: ClassVar = ["openid", "email", "profile"]

    async def openid_from_response(self, response: dict, session: Optional["httpx.AsyncClient"] = None) -> OpenID:
        """
        Retorna un objeto OpenID a partir de la información del usuario proporcionada por Google.

        Args:
            response (dict): Respuesta JSON obtenida del proveedor Google.
            session (Optional[httpx.AsyncClient]): Sesión HTTP opcional para realizar solicitudes adicionales.

        Returns:
            OpenID: Objeto OpenID con la información del usuario autenticado.

        Raises:
            SSOLoginError: Si el correo electrónico del usuario no está verificado.
        """
        if response.get("email_verified"):
            return OpenID(
                email=response.get("email", ""),
                provider=self.provider,
                id=response.get("sub"),
                first_name=response.get("given_name"),
                last_name=response.get("family_name"),
                display_name=response.get("name"),
                picture=response.get("picture"),
            )
        # Si el correo electrónico no está verificado, se lanza un error de inicio de sesión.
        raise SSOLoginError(401, f"User {response.get('email')} is not verified with Google")

    async def get_discovery_document(self) -> DiscoveryDocument:
        """
        Obtiene el documento de descubrimiento que contiene las URLs útiles para OpenID Connect.

        Returns:
            DiscoveryDocument: Documento de descubrimiento con las URLs necesarias.

        Raises:
            httpx.HTTPStatusError: Si la solicitud HTTP falla.
        """
        async with httpx.AsyncClient() as session:
            response = await session.get(self.discovery_url)
            response.raise_for_status()  # Asegura que se manejen los errores HTTP
            content = response.json()
            return content
