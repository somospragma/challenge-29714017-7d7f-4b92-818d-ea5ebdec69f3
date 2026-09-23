class CoreBankingException(Exception):
    """
    Excepción personalizada para errores provenientes del core bancario.
    Contiene información sobre el tipo de error y el contexto en que ocurrió.
    """
    def __init__(self, message: str, error_code: str = None, details: dict = None):
        """
        Args:
            message: Mensaje descriptivo del error.
            error_code: Código de error específico del core bancario.
            details: Detalles adicionales sobre el error.
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}

    def __str__(self) -> str:
        base = f"CoreBankingException: {self.message}"
        if self.error_code:
            base += f" [Code: {self.error_code}]"
        if self.details:
            base += f" Details: {self.details}"
        return base

    def to_dict(self) -> dict:
        """Convierte la excepción a un diccionario para serialización."""
        return {
            'message': self.message,
            'error_code': self.error_code,
            'details': self.details,
            'type': self.__class__.__name__
        }